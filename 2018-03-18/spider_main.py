import re
import urllib.parse
import html_downloader
import html_outputer
import html_parser
from bs4 import BeautifulSoup
import math
import jieba.posseg as pseg
import codecs

import pymongo
from nltk.corpus import stopwords
from collections import Counter



class SpiderMain(object):
    def __init__(self):
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self, root_url):
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        request = urllib.request.Request(root_url, headers=headers)
        response = urllib.request.urlopen(request, timeout=20)
        if response.getcode() == 200:
            html_doc2 = response.read()
            #soup = BeautifulSoup(html_doc2, 'html.parser', from_encoding='utf-8')
            soup = BeautifulSoup(html_doc2, 'html.parser')
            new_urls = set()
            links = soup.findAll('a',class_="title-link")
            print(links.__len__())
            print(links)
            for link in links:
                new_url = link['href']
                name = re.findall(r"/news/(.*).", new_url)
                if not name :
                    continue
                print(name[0])
                new_full_url = urllib.parse.urljoin(root_url, new_url)
                new_urls.add(new_full_url)
                new_urls.add(new_full_url)
                print(new_full_url)
                html_cont = self.downloader.download(new_full_url)
                new_data=self.parser.parse(new_full_url,html_cont)
                self.outputer.collect_data(new_data,name)
                self.outputer.output_html()
            print("over")

def tokenization(content):   #去除文章中的停用词和停用词性
    result = []
    words = pseg.cut(content)
    for word, flag in words:
        word = word.lower()
        flag = flag.lower()
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

def tf(word, count):   #TFIDF实现
    return count[word] / sum(count.values())

def n_containing(word, count_list):  #TFIDF实现
    return sum(1 for count in count_list if word in count)

def idf(word, count_list):  #TFIDF实现
    return math.log(len(count_list) / (1 + n_containing(word, count_list)))

def tfidf(word, count, count_list):  #TFIDF实现
    return tf(word, count) * idf(word, count_list)

def repeat(cosine):  #去除重复元素
    #cosine = list(set(cosine))  set去重打乱了顺序，虽然不影响结果，但不好观察结果
    cosine2 = []   #达到去重效果，且没改变顺序，方便观察结果
    for item in cosine:
        if item not in cosine2:
            cosine2.append(item)
    return cosine2

def conversion(cosine,matrixs):  #生成词频向量
    vectors = []
    for item in cosine:
        if item in matrixs:
            vectors.append(1)
        else:
            vectors.append(0)
    return vectors

#计算余弦相似度
def cosine_similarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA**0.5)*(normB**0.5)), 5)

if __name__=="__main__":
    root_url="https://www.bbc.com/news/world"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

    #去重
    stop_words = 'D:/demo/stop_words2.txt'
    stopwords = codecs.open(stop_words, 'r', encoding='gb18030').readlines()
    stopwords = [w.strip() for w in stopwords]  # 停用词
    stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']  # 停用词性

    # 连接到Mongodb数据库，查询出新闻数据
    mongo_uri = 'localhost'
    mongo_db = 'news'
    client = pymongo.MongoClient(mongo_uri)
    db = client[mongo_db]
    p = db['bbc_news']
    news = p.find()  # 新闻数据
    news_length = news.count()  # 数据的长度

    # 文章的提取出20个关键字
    countlist = []
    filenames = []
    for item in news:
        filenames.append(item['_id'])
        tokens = tokenization(item['content'])
        count = Counter(tokens)
        print(count.most_common(20))
        countlist.append(count)

    # 每篇新闻TDIDF值前十的词
    matrixs = locals()
    for i, count in enumerate(countlist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, count, countlist) for word in count}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        matrixs['matrix' + str(i)] = []
        for word, score in sorted_words[:10]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
            matrixs['matrix' + str(i)].append(word)

    # print(matrixs.keys())
    # for i, count in enumerate(countlist):
    #    print(matrixs['matrix' + str(i)])

    sim_delete = []
    i = 0
    while (i < news_length):
        j = i + 1
        while (j < news_length):
            matrixs['cosine' + str(i * j + j)] = []
            for item in matrixs['matrix' + str(i)]:
                matrixs['cosine' + str(i * j + j)].append(item)
            for item in matrixs['matrix' + str(j)]:
                matrixs['cosine' + str(i * j + j)].append(item)
            print('matrix' + str(i) + ' and ' + 'matrix' + str(j))
            matrixs['cosine' + str(i * j + j)] = repeat(matrixs['cosine' + str(i * j + j)])
            vector1 = conversion(matrixs['cosine' + str(i * j + j)], matrixs['matrix' + str(i)])
            print(vector1)
            vector2 = conversion(matrixs['cosine' + str(i * j + j)], matrixs['matrix' + str(j)])
            print(vector2)
            sim = cosine_similarity(vector1, vector2)
            if (sim > 0.5):
                sim_delete.append(j)
            print('sim ' + str(cosine_similarity(vector1, vector2)))
            j = j + 1
        i = i + 1

    print(sim_delete)
    ids = []
    for delete in sim_delete:
        news2 = p.find().limit(1).skip(delete)
        for item in news2:
            ids.append(item['_id'])

    for id in ids:
        if p.remove({'_id': id}):
            print('id: ' + str(id) + ' 删除成功')


