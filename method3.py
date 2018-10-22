import urllib.request,http.cookiejar
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response = urllib.request.urlopen("http://www.baidu.com/")
print(response.getcode())
