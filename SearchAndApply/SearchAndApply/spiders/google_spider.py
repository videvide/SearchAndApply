import scrapy
import json
import os

####################################################################################
# run this with the 'scrapy crawl google' command, data will be stored from program #
####################################################################################
email_file = os.environ.get('email_file')


class GoogleSpider(scrapy.Spider):
    name = 'google'
    start_urls = ['https://www.google.com/search?q=digital+byr%C3%A5']

    def parse(self, response):
        link_file = 'links.txt'
        for link in response.xpath('//div[@class="rc"]/div/a/@href').getall():
            if 'google' not in link:
                with open(link_file, 'a') as f:
                    f.write(f"{link}\n")
                yield scrapy.Request(link, callback=self.get_emails)

        next_page = response.xpath('//a[@id="pnnext"]/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def get_emails(self, response):
        for email in response.xpath(
                "//a[contains(@href, 'mailto')]/@href").getall():
            with open(email_file, 'a+') as f:
                f.write(f"{email}\n")
