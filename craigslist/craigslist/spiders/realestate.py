import scrapy


class RealestateSpider(scrapy.Spider):
    name = "realestate"
    allowed_domains = ["newyork.craigslist.org"]
    start_urls = ["https://newyork.craigslist.org/d/real-estate/search/rea"]
    """
    def parse(self, response):
        print("\n")
        print("HTTP STATUS: "+str(response.status))
        print(response.css("title::text").get())
        print("\n")
        """
    def parse(self, response):
        allAds = response.css("p.result-info")

        for ad in allAds:
            date = ad.css("time::text").get()
            title =  ad.css("a.result-title.hdrlnk::text").get()
            price = ad.css("span.result-price::text").get()
            link = ad.css("a::attr(href)").get()

            print("====NEW PROPERTY===")
            print(date)
            print(title)
            print(price)
            print(link)

            print(\n")
