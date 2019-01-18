import urllib.request
import urllib.parse
"""
	运行它的时候先修改用户名字和密码
"""
url="http://account.chinaunix.net/login/login"
post_data=urllib.parse.urlencode({
	"username":"******",
	"password":"******"
	}).encode('utf-8')
print(post_data)
req=urllib.request.Request(url,post_data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
data=urllib.request.urlopen(req).read()
fandle=open("./1.html","wb")
fandle.write(data)
fandle.close()
url2="http://www.chinaunix.net/"
req2=urllib.request.Request(url2)
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
data2=urllib.request.urlopen(req2).read()
fandle2=open("./2.html","wb")
fandle2.write(data2)
fandle2.close()
