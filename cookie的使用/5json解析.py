import urllib.request
import urllib.parse
import http.cookiejar
import json
import time
"""
	运行它的时候先修改用户名字和密码
"""
url="http://account.chinaunix.net/login/login"
# url="http://account.chinaunix.net/login?url=%2Fucenter%2Fuser%2Findex"
username=input("请输入账号:")
password=input("请输入密码")
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

"""
	bytes 转换成 dict类型 以及运用这些这些类型
"""
data=str(file.read(),encoding="utf-8")
print("获取到的数据以及类型是:",data,type(data))
data=eval(data)
print("eval处理后的数据以及类型是:",data,type(data))
print(data['data']['url'])

"""
	http://account.chinaunix.net/login/sso?url=%2Fucenter%2Fuser%2Findex
"""
"""
	urllib.parse的应用
	主要是urlparse的应用
"""
print("urllib.parse.urlparse的应用path",urllib.parse.urlparse(url).path)
print("urllib.parse.urlparse的应用netloc",urllib.parse.urlparse(url).netloc)
print("urllib.parse.urlparse的应用scheme",urllib.parse.urlparse(url).scheme)
part_url=data['data']['url']

re_url=urllib.parse.urljoin(url,part_url)
print("urllib.parse.urljonin的应用:",re_url)
# # json_data_init=json.loads(data)
# json_data_init=eval(data)
# print(json_data_init,type(json_data_init))
# data=urllib.request.urlopen(req).read()

# json_data=json.dumps(str(data))
# print("json_data",type(json_data))
# text=json.loads(json_data)
# print("json.loads(json_data)",type(text))
# # text[0]
# print("json的具体内容是:",text[1])
"""
	将数据写进当前目录的html
"""
fandle=open("./1.html","w")
fandle.write(str(data))
fandle.close()
# url2="http://www.chinaunix.net/"
#如果改为这个网址就会爬取成功re_url="http://account.chinaunix.net/ucenter/user/index"
# re_url="http://account.chinaunix.net/ucenter/user/index"
req2=urllib.request.Request(re_url)
print("req2",req2)
# # req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
data2=urllib.request.urlopen(req2)
print(data2)
time.sleep(5)
data2=data2.read()
fandle2=open("./2.html","wb")
fandle2.write(data2)
fandle2.close()
