from scrapy.selector import Selector
from scrapy.http import HtmlResponse
text="""
    <ul>
        <li>python学习手册<b>价格 99.00元</b></li>
        <li>python核心编程<b>价格88.00元</b></li>
        <li>python基础教程<b>价格80.00元</b></li>
    </ul>
"""
selector=Selector(text=text)
result=selector.xpath('.//li/b/text()')
print(result)
print(result.extract())
for x in result.extract():
    print(x)
result1=selector.xpath(".//li/b/text()").re('\d{2}.\d{2}')
print(result1)
result1=selector.xpath(".//li/b/text()").re_first('\d{2}.\d{2}')
print(result1)

print("""
    Response 内置的 Selector
""")
body="""
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
response=HtmlResponse(url="http://www.example.com",body=body,encoding="utf=8")
print(response.selector)