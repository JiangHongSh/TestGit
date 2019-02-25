import math
import jieba.posseg as pseg
import codecs
from nltk.corpus import stopwords
from collections import Counter


stop_words = 'E:/demo/stop_words2.txt'
stopwords = codecs.open(stop_words,'r',encoding='gb18030').readlines()
stopwords = [ w.strip() for w in stopwords ]
#print(stopwords)

stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']
#print(stop_flag)
def tokenization(filename):
    result = []
    with open(filename, 'r') as f:
        text = f.read()
        words = pseg.cut(text)
    for word, flag in words:
        word = word.lower()
        flag = flag.lower()
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

filenames = ['E://demo/Brazil1.txt',
             'E://demo/Brazil2.txt',
             'E://demo/Climate change-copy.txt',
             'E://demo/Nasa Mars.txt',
            ]

countlist = []

for filename in filenames:
    tokens = tokenization(filename)
    count = Counter(tokens)
    print (count.most_common(20))
    countlist.append(count)

def tf(word, count):
    return count[word] / sum(count.values())

def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)

def idf(word, count_list):
    return math.log(len(count_list) / (1 + n_containing(word, count_list)))

def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)

for i, count in enumerate(countlist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, count, countlist) for word in count}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))



