import requests
url = "http://www.baidu.com"
url="http://www.zhihu.com/settings/account"
try:
	r = requests.get(url)
	print(r.status_code)
	r.raise_for_status()
	r.encoding = r.apparent_encoding # 如果出现HTML出现乱码再加入该语句
	print(r.text)
except Exception as e:
	print("爬取失败，错误为：" + str(e))

# import requests
# r = requests.get("http://www.zhihu.com/settings/account")
# r.encoding = r.apparent_encoding
# print(r.status_code)
# print(r.text)