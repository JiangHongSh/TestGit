# -*- coding: utf-8 -*-
import re
import urllib.parse
from urllib import parse
import requests
import os
from bs4 import BeautifulSoup
from skimage.measure import compare_ssim
import cv2
from PIL import Image

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
        title_node=soup.find("h1")
        res_data['title']=title_node.get_text()
        #summary_node = soup.find('div',class_='vxp-media__summary' or'story-body__inner' or 'vxp-media__summary').findAll('p')
        summary_node = soup.find('div',attrs = {"class": ["story-body__inner", "vxp-media__summary"]}).findAll('p')
        res_data['summary']=summary_node
        img_node = soup.findAll('img')
        href = []
        for imgs in img_node:
            href.append(imgs['src'])
            print(imgs['src'])
        href = list(set(href))
        #res_data['imgs']=href
        images = []
        root = "D:/images/"
        for img in href:
            path = root + img.split('/')[-1]
            try:
                r = requests.get(img)
                with open(path, 'wb')as f:
                    f.write(r.content)
                    f.close()
            except BaseException :
                print("爬取失败")
                continue
            images.append(path)
        try:
            for img in images :
                for imgc in images :
                    print(img)
                    print(imgc)
                    crop_size = (256, 256)
                    imageA = cv2.imread(img)
                    imageB = cv2.imread(imgc)
                    img_newA = cv2.resize(imageA, crop_size, interpolation = cv2.INTER_CUBIC)
                    img_newB = cv2.resize(imageB, crop_size, interpolation = cv2.INTER_CUBIC)
                    grayA = cv2.cvtColor(img_newA, cv2.COLOR_BGR2GRAY)
                    grayB = cv2.cvtColor(img_newB, cv2.COLOR_BGR2GRAY)
                    (score, diff) = compare_ssim(grayA, grayB, full=True)
                    print("SSIM: {}".format(score))
                    a = 0.9
                    b = 1.0
                    if(float(score)> 0.9 and float(score)< 1.0) :
                        print(img)
                        print(imgc)
                        os.remove(imgc)
                        print("remove:"+imgc)
                        continue
        except BaseException:
            print("已删除或删除失败")
        res_data['imgs'] = images
        return res_data
