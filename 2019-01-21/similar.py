import jieba.posseg as pseg
import codecs
from gensim import corpora, models, similarities

stop_words = 'E:/demo/stop_words.txt'
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
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

filenames = ['E://demo/亚马逊CEO离婚1.txt',
             'E://demo/亚马逊CEO离婚2.txt',
             'E://demo/亚马逊CEO离婚3.txt',
             'E://demo/张小龙演讲1.txt',
             'E://demo/张小龙演讲2.txt',
             'E://demo/法国.txt'
            ]
corpus = []
for each in filenames:
    corpus.append(tokenization(each))
#print(len(corpus))

dictionary = corpora.Dictionary(corpus)
#print(dictionary)

doc_vectors = [dictionary.doc2bow(text) for text in corpus]
#print(len(doc_vectors))
#print(doc_vectors)

tfidf = models.TfidfModel(doc_vectors)
tfidf_vectors = tfidf[doc_vectors]

#print(len(tfidf_vectors))
#print(len(tfidf_vectors[0]))

query = tokenization('E://demo/亚马逊CEO离婚1.txt')
query_bow = dictionary.doc2bow(query)
#print(len(query_bow))
#print(query_bow)
index = similarities.MatrixSimilarity(tfidf_vectors)

sims = index[query_bow]
print(list(enumerate(sims)))

lsi = models.LsiModel(tfidf_vectors, id2word=dictionary, num_topics=3)
#lsi.print_topics(8)

lsi_vector = lsi[tfidf_vectors]
#for vec in lsi_vector:
#   print(vec)

query = tokenization('E://demo/亚马逊CEO离婚2.txt')
query_bow = dictionary.doc2bow(query)
#print(query_bow)

query_lsi = lsi[query_bow]
#print(query_lsi)

index = similarities.MatrixSimilarity(lsi_vector)
sims = index[query_lsi]
print(list(enumerate(sims)))



