#导入包转换链接中的中文字符
import urllib.parse
import os

import pymongo

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.names = []


    def collect_data(self,data,name):
        if data is None:
            return
        self.datas=data
        self.names=name


    def output_html(self):
        content = ''
        summary_node = self.datas['summary']
        for summary in summary_node:
            content = '%s %s'%(content, summary.get_text())

        img_url = ''
        imgs_node = self.datas['imgs']
        for img in imgs_node:
            img_url = '%s##%s'%(img_url,img)

        mongo_uri = 'localhost'
        mongo_db = 'news'
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db]
        p = db['bbc_news']
        bbc_news = {
            'title': self.datas['title'],
            'content' : content,
            'img' : img_url
        }
        p.insert(bbc_news)
        client.close()
