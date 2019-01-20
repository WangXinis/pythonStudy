"""
in this file,I upgrade 3th file
if you login it ,you can scrapy all the web page.
because I add cookie function in this file.
"""

import urllib.request
import urllib.parse
import http.cookiejar
import urllib.parse
"""
	运行它的时候先修改用户名字和密码
	爬取CHINAUNIX
"""
# 必须首先执行myCookie() 函数，然后进行配置
def myCookie():
	#创建cookie对象
	mycookie=http.cookiejar.CookieJar()
	# print(mycookie)
	# 创建cookie的管理器
	mycookie_handle=urllib.request.HTTPCookieProcessor(mycookie)
	# print(mycookie_handle)
	# 创建http请求管理器
	http_handle = urllib.request.HTTPHandler()
	 
	# 创建https管理器
	https_handle = urllib.request.HTTPSHandler()
	# 创建求求管理器，将上面3个管理器作为参数属性
	# 有了opener，就可以替代urlopen来获取请求了
	opener = urllib.request.build_opener(mycookie_handle,http_handle,https_handle)
	print(type(opener))
	return opener
def login():
	opener = myCookie() 
	url="http://account.chinaunix.net/login/login"
	username=input("请输入账号:")
	password=input("请输入密码")
	post_data=urllib.parse.urlencode({
		"username":username,
		"password":password
		}).encode('utf-8')
	print('你填写的数据是:',post_data)
	req=urllib.request.Request(url,post_data)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
	# data=urllib.request.urlopen(req).read()  #这一条数据必须更改了
	response=opener.open(req)
	data=response.read()
	print(data,"的数据类型是:",type(data))
	# fandle=open("./1.html","wb")
	# fandle.write(data)
	# fandle.close()
	# 将data转化成字典类型
	data_dict=eval(str(data,encoding='utf-8'))
	print(data_dict,"的数据类型是",type(data_dict))
	part_url=data_dict['data']['url']
	re_url=urllib.parse.urljoin(url,part_url)
	print("重构的url是:",re_url)
	req=urllib.request.Request(re_url)
	response2=opener.open(req)
	data=response2.read()
	with open("1.html","wb") as file:
		file.write(data)
def scrapyIt(url2="http://www.chinaunix.net/"):
	# req2=urllib.request.Request(url2)
	# req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
	# data2=urllib.request.urlopen(req2).read()
	# fandle2=open("./2.html","wb")
	# fandle2.write(data2)
	# fandle2.close()
	# 上面这一部分根本就没有用到cookie,所以才会出现错误
	print("您要爬取的网站是:",url2)
login()
scrapyIt(url2="http://account.chinaunix.net/ucenter/user/index")
# login()
# scrapyIt()
"""
 in 12th file ， I upgrade it that is a file before.
 now,the trail still afailure
"""