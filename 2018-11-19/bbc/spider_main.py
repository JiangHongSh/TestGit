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
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        request = urllib.request.Request(root_url, headers=headers)
        response = urllib.request.urlopen(request, timeout=20)
        html_doc2 = response.read()
        #soup = BeautifulSoup(html_doc2, 'html.parser', from_encoding='utf-8')
        soup = BeautifulSoup(html_doc2, 'html.parser')
        print(html_doc2)
        new_urls = set()
        links = soup.findAll('a',class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")
        print(links.__len__())
        for link in links:
            new_url = link['href']
            name = re.findall(r"/news/(.*).", new_url)
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
    root_url="https://www.bbc.com/news"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
