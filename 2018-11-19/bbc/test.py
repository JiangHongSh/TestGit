import urllib.request,http.cookiejar
import re
from bs4 import BeautifulSoup
import time
import socket
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
url ='https://www.bbc.com/news'
headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
request = urllib.request.Request(url, headers = headers)
response = urllib.request.urlopen(request,timeout=20)
if response.getcode()==200:
    html_doc2 = response.read()
    soup = BeautifulSoup(html_doc2, 'html.parser')
    #links = soup.findAll('a',href=re.compile(r"^/news/"))
    links = soup.findAll('a',class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")
    print(links.__len__())
    for link in links:
        print(link)

