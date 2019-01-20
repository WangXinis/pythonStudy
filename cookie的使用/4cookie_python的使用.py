import urllib.request
import urllib.parse
import http.cookiejar
"""
	运行它的时候先修改用户名字和密码
"""
url="http://account.chinaunix.net/login/login"
username=input("请输入账号:")
password=input("请输入密码")
# url="http://account.chinaunix.net/login?url=%2Fucenter%2Fuser%2Findex"
post_data=urllib.parse.urlencode({
	"username":username,
	"password":password
	}).encode('utf-8')
# print(post_data)
req=urllib.request.Request(url,post_data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
#使用http.cookiejar.CookieJar()创建CookieJar对象
cjar=http.cookiejar.CookieJar()
#使用HTTPCookieProcessor创建cookie处理器，并且用它作为参数构建opener对象
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file=opener.open(req)
data=file.read()
print(data)
data=urllib.request.urlopen(req).read()
fandle=open("./1.html","wb")
fandle.write(data)
fandle.close()
url2="http://www.chinaunix.net/"
req2=urllib.request.Request(url2)
# req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
data2=urllib.request.urlopen(req2).read()
fandle2=open("./2.html","wb")
fandle2.write(data2)
fandle2.close()
