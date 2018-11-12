# -*- coding: utf-8 -*-
import re
import urllib.parse
from urllib import parse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,"html.parser")
        new_data = self._get_new_data(page_url,soup)
        return new_data

    def _get_new_data(self, page_url, soup):
        res_data={}
        res_data['url']=page_url
        title_node=soup.find('header').find("h1")
        res_data['title']=title_node.get_text()
        summary_node = soup.findAll('p')
        res_data['summary']=summary_node
        img_node = soup.findAll('img')
        res_data['imgs']=img_node
        return res_data
