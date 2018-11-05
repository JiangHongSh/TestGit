# -*- coding: utf-8 -*-
from urllib import request
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        response = request.urlopen(url)
        if response.getcode() != 200:
            return
        else:
            return response.read().decode('utf-8')
