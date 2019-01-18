# -*- coding: utf-8 -*-
import scrapy


class BrowserincookiesSpider(scrapy.Spider):
    name = 'browserincookies'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'Host': 'bj.zu.anjuke.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    def start_request(self):
        url="http://www.zhihu.com/settings/profile"
        return [scrapy.Request(url,meta={'cookiejar':'chrome'},headers=self.headers,callback=process_request)]
    def parse(self, response):
        print("返回的响应是:"+str(response))
        print("*"*20)
    def process_request(self, request, spider):
    # 在这里做修改操作
        request._set_url(request.url)