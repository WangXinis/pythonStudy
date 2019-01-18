import browsercookie
from scrapy.downloadermiddlewares.cookies import CookiesMiddleware
class BrowserCookiesMiddleware(CookiesMiddleware):
	def __init__(slef,debug=False):
		super().__init__(debug)
		self.load_browser_cookies()
	def load_browser_cookies(self):
		# 加载Chrome浏览器中的Cookie
		jar = self.jars['chrome']
		chrome_cookiejar = browsercookie.chrome()
		for cookie in chrome_cookiejar:
			jar.set_cookie(cookie)
		# 加载Chrome浏览器中的Cookie
		jar = self.jars['firefox']
		firefox_cookiejar = browsercookie.firefox()
		for cookie in firefox_cookiejar:
			jar.set_cookie(cookie)