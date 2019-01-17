from scrapy.selector import Selector

"""
    直接创建Selector对象
"""
text = """
    <html>
        <body>
            <h1>Hello World</h1>
            <h1>Hello Scrapy</h1>
            <b>Hello python</b>
            <ul>
                <li>C++</li>
                <li>Java</li>
                <li>python</li>
            </ul>
        </body>
    </html>
"""

selector = Selector(text=text)
print(selector)
from scrapy.http import HtmlResponse
# 通过Response对象创建Selector对象
response = HtmlResponse(url="http://www.example.com",body=text,encoding="utf-8")
print(response)
selector=Selector(response=response)
print(selector)

selector_list=selector.xpath("//h1")
print(selector_list)
for sel in selector_list:
    print(sel.xpath('./text()'))

print (selector_list.xpath('./text()').extract())
print(selector.xpath('.//ul').css('li').xpath('./text()').extract())

print("*"*20,"下一部分")
sl=selector.xpath(".//li")
print(type(sl))
print(sl)
print(sl[0].extract())
print("+"*50)
sl=selector.xpath(".//li/text()")
print(sl)
print(sl[1].extract())


print(sl.extract())
print("*"*50)
sl=selector.xpath(".//b/text()")
print(sl.extract())
print(sl.extract()[0])
print(sl.extract_first())
