import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://www.baidu.com')
html_doc2 = response.read()

soup = BeautifulSoup(html_doc2,'html.parser',from_encoding='utf-8')
print('获取所有的链接')
links = soup.find_all('a')
for link in links:
  print(link.name,link['href'],link.get_text())
