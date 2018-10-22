import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')

#200表示获取成功
print(response.getcode())

print(response.read())

cont = response.read()
