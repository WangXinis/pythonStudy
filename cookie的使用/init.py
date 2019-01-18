import browsercookie
from scrapy.http import Request
# chrome_cookiejar = browsercookie.chrome()
firefox_cookiejar=browsercookie.firefox()
response=Request("http://www.zhihu.com",meta={'cookiejar':'account1'})
url=response.url
response1=Request(url)
print(response1.body)
# print(firefox_cookiejar)