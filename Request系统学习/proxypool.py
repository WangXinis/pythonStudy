import json
import requests
from requests.exceptions import ConnectionError,HTTPError
from pyquery import PyQuery as pq
#测试代理是否可用
TEST_URL="http://weixin.sougou.com"

# 构造请求头
base_header={
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	# 'Accept-Encoding':' gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9'}
# 抓取代理 
# 封装代理页面
def get_page(url,options={}):
	headers = dict(base_header,**options)
	print('正在抓取',url)
	try:
		response = requests.get(url,headers=headers)
		print('抓取成功',url,response.status_code)
		if response.status_code == 200 :
			#最重要的代码
			return response.text
	except (ConnectionError,HTTPError):
		print("抓取失败url is ",url)
		return None
#获取代理的IP
def get_xcidaili(page_count=2):
	start_url='https://www.xicidaili.com/nn/{page}'
	urls = [start_url.format(page=page) for page in range(1,page_count)]
	print(urls)
	for url in urls:
		print('Crawling url is ',url)
	html = get_page(url)
	if html:
		doc=pq(html)
		results=doc('#ip_list tr').items()
		for result in results:
			ip=result.find('td:nth-child(2)').text()
			port=result.find('td:nth-child(3)').text()
			if ip and port :
				yield ':'.join([ip,port])
def test_proxy(proxy,timeout=8):
	proxies = {
	'http':'http://'+proxy,
	'https':'https://'+proxy,
	}
	try:
		#
		response =requests.get(TEST_URL,proxies=proxies,verify=False,timeout=timeout)
		if response.status_code == 200:
			print("Successful",proxy)
			return True
		else:
			print("Useless",proxy)
	except Exception:
		print('Useless',proxy)
		return False
def save_proxy_ip(timeout=8):
	proxys=[]
	for proxy in get_xcidaili(page_count=4):
		print("代理是:",proxy)
		if proxy and test_proxy(proxy,timeout=timeout):
			proxys.append(proxy)
			with open('proxys_ip.txt','w+',encoding='utf-8') as f:
				f.write(',\n'.join(proxys))
def main():
	save_proxy_ip(timeout=1)
main()