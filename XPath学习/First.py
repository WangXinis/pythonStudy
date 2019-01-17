# from scrapy.selector import Selector
from scrapy.http import HtmlResponse
body="""
    <div class="container d-flex clearfix">
		<div class="title-box">
			<h6 class="title-blog">
				<a href="https://blog.csdn.net/bjweimengshu">程序员小灰的博客</a>
			</h6>
			<p class="description"></p>
		</div>
		<div class="opt-box d-flex justify-content-end">
			<a class="btn btn-sm" href="https://blog.csdn.net/bjweimengshu/rss/list">
					<svg class="icon" aria-hidden="true">
						<use xlink:href="#csdnc-rss"></use>
					</svg>RSS订阅</a>
					</div>
	</div>
"""
reponse=HtmlResponse(url="http://www.example.com",body=body,encoding='utf-8')
result=reponse.xpath('/html//div').extract()
print(result)