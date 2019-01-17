from scrapy.selector import Selector
import chardet
file=open("test.html","r",encoding="utf-8")
result=file.read()
# print(result)
print(chardet.detect(result))
# //*[@id="4001"]/div[1]/h3/a[1]/text()