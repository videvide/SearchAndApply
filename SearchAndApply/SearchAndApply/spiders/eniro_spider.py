import scrapy
import json
from scrapy_splash import SplashRequest

####################################################################################
# run this with the 'scrapy crawl eniro' command, data will be stored from program #
####################################################################################
email_file = os.environ.get('email_file')


class EniroSpider(scrapy.Spider):
    name = 'eniro'
    start_urls = ['https://www.eniro.se/webbyr%C3%A5/f%C3%B6retag']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html',
                                args={
                                    'wait': 1,
                                })

    def parse(self, response):
        for link in response.xpath('//a[@class="homePage"]/@href').getall():
            yield SplashRequest(url=link,
                                callback=self.get_emails,
                                endpoint='render.html',
                                args={
                                    'wait': 5,
                                })

        next_page = response.xpath('//a[@class="nav nextPage"]/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def get_emails(self, response):
        for email in response.xpath(
                "//a[contains(@href, 'mailto')]/@href").getall():
            if email:
                with open(email_file, 'a+') as f:
                    f.write(f"{email}\n")
