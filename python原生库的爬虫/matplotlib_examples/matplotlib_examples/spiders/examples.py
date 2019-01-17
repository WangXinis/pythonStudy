# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MatplotlibExamplesItem
class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"}
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        # print("我是响应"+str(response))
        print("爬取的网页的标题是:",response.xpath('/html/head/title/text()').extract())
        le=LinkExtractor(restrict_css='div.toctree-wrapper.compound li.toctree-l2')
        links=le.extract_links(response)
        print("连接的长度是:",len(links))
        for link in links:
            yield scrapy.Request(link.url,callback=self.parse_example)
    def parse_example(self,response):
        href=response.css('a.reference.external::attr(href)').extract_first()
        url=response.urljoin(href)
        example = MatplotlibExamplesItem()
        example['file_urls']=[url]
        return example
