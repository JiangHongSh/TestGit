# -*- coding: utf-8 -*-
import url_manager, html_downloader, html_parser, html_outputer
import urllib.parse
import re
import urllib.parse
from urllib import parse
from bs4 import BeautifulSoup

class SpiderMain(object):
    def __init__(self):
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self, root_url):
        response = urllib.request.urlopen(root_url)
        html_doc2 = response.read()
        #soup = BeautifulSoup(html_doc2, 'html.parser', from_encoding='utf-8')
        soup = BeautifulSoup(html_doc2, 'html.parser',from_encoding='GBK')
        print(html_doc2)
        new_urls = set()
        links = soup.findAll('a',class_="Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 Td(n) C(#0078ff):h C(#000)")
        for link in links:
            new_url = link['href']
            name = re.findall(r"/news/(.*)-", new_url)
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

if __name__=="__main__":
    root_url="https://www.yahoo.com/news/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
