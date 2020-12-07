import scrapy
import json
import os
from scrapy_splash import SplashRequest
from scrapy.exceptions import CloseSpider
import datetime

#########################################################################################################
# first start the splash container, $ sudo docker run -it -p 8050:8050 --rm scrapinghub/splash          #
# then run this with the scrapy crawl aw -s JOBDIR=crawls/aw-'number' -o filepath/filename.jl' command  #
#########################################################################################################

# This is the first scraped ad from the last session.
kill_id = os.environ.get('kill_id_aw')


class AcademicWorkSpider(scrapy.Spider):
    name = 'aw'
    # user-input:
    start_urls = ['https://jobs.academicwork.se/it-jobb/?C=IT&s=date']
    page = 1

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url=url,
                callback=self.parse,
                endpoint='render.html',
                args={
                    'wait': 10,
                },
            )

    def parse(self, response):
        for link in response.xpath(
                '//div[@class="list-job-body"]/a/@href').getall():
            annons_url = response.urljoin(link)
            yield scrapy.Request(
                url=annons_url,
                callback=self.job_info,
            )

        self.page += 1
        next_page = f'https://jobs.academicwork.se/it-jobb/?C=IT&p={self.page}&s=date'
        yield SplashRequest(url=next_page,
                            callback=self.parse,
                            endpoint='render.html',
                            args={
                                'wait': 10,
                            })

    def job_info(self, response):
        job_obj = {}
        ad_id = response.xpath('//div[@class="jobbid"]/text()').get()
        if ad_id == kill_id:
            raise CloseSpider(
                "start of last session is reached, spider is therefor killed.")
        else:
            ad_id_str = str(ad_id)
            job_title = response.xpath('//h1/text()').get()
            contact_info = response.xpath(
                '//div[@class="consultant-text"]/p/text()').get()
            contact_info_str = str(contact_info)
            mail = response.xpath(
                '//a[contains(@href, "mailto")]/text()').get()
            job_obj['id'] = ad_id_str.replace('Annons-ID: ', '')
            job_obj['title'] = job_title
            job_obj['name'] = contact_info_str.replace(
                ' eller någon av kollegorna i rekryteringsteamet svarar dig gärna på',
                '')
            job_obj['mail'] = mail
            yield job_obj