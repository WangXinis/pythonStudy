# -*- coding: utf-8 -*-
import scrapy
# from HouseRenting.user_agents import agents
# import random
import time
import re
import requests
import http.cookiejar
from PIL import Image
import json
from bs4 import BeautifulSoup

class BrowserCookiesSpider(scrapy.Spider):
    name = 'browser_cookies'
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
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        print(response)
#     def parse(self, response):
#         # 主页爬取的具体内容
#         all_urls = response.css('a::attr(href)').extract()
#         all_urls = [parse.urljoin(response.url, url) for url in all_urls]
#         # 去除javascript
#         all_urls = filter(lambda x: True if x.startswith("https") else False, all_urls)
#         for url in all_urls:
#             pass

#     def start_requests(self):
#         t = str(int(time.time() * 1000))
#         captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + '&type=login&lang=en'
#         return [scrapy.Request(url=captcha_url, headers=self.header, callback=self.parser_captcha)]

#     def parser_captcha(self, response):
#         with open('captcha.jpg', 'wb') as f:
#             f.write(response.body)
#             f.close()
#         try:
#             im = Image.open('captcha.jpg')
#             im.show()
#             im.close()
#         except:
#             print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
#         captcha = input("please input the captcha\n>")
#         return scrapy.FormRequest(url='https://www.zhihu.com/#signin', headers=self.header, callback=self.login, meta={
#             'captcha': captcha
#         })

#     def login(self, response):
#         xsrf = response.xpath("//input[@name='_xsrf']/@value").extract_first()
#         if xsrf is None:
#             return ''
#         post_url = 'https://www.zhihu.com/login/phone_num'
#         post_data = {
#             "_xsrf": xsrf,
#             "phone_num": '${username}',
#             "password": '${password}',
#             "captcha": response.meta['captcha']
#         }
#         return [scrapy.FormRequest(url=post_url, formdata=post_data, headers=self.header, callback=self.check_login)]

#     # 验证返回是否成功
#     def check_login(self, response):
#         js = json.loads(response.text)
#         if 'msg' in js and js['msg'] == '登录成功':
#             for url in self.start_urls:
#                 yield scrapy.Request(url=url, headers=self.header, dont_filter=True)

# # 作者：Xia0JinZi
# # 链接：https://www.jianshu.com/p/889844521249
# # 來源：简书
# # 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。