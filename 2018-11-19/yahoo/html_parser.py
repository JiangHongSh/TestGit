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
        href = []
        for imgs in img_node:
            href.append(imgs['src'])
        href = list(set(href))
        href.remove('https://s.yimg.com/nn/lib/metro/DailyFantasy_BN_Baseball_300x250-min.jpg')
        href.remove('https://s.yimg.com/ny/api/res/1.2/Fq07rVpvW_neeURxQB3w2Q--~A/YXBwaWQ9aGlnaGxhbmRlcjtzbT0xO3c9ODQ7aD04NDtpbD1wbGFuZQ--/http://l.yimg.com/os/creatr-images/GLB/2017-06-07/710c91c0-4b9c-11e7-8912-374be9390b1b_H-1-.png.cf.jpg')
        res_data['imgs']=href


        return res_data
