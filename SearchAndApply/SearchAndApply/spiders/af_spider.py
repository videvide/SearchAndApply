import scrapy
import os
from scrapy_splash import SplashRequest
from scrapy.exceptions import CloseSpider

#################################################################################################
# first start the splash container, $ sudo docker run -it -p 8050:8050 --rm scrapinghub/splash  #
# then run this with the JOBDIR=crawls/'crawlname-number' and -o 'filepath/filename'.jl options #
#################################################################################################

# This is the first scraped ad from the last session.
kill_id = os.environ.get('kill_id_af')


class PlatsBankenSpider(scrapy.Spider):
    name = 'af'
    # user-input:
    start_urls = [
        'https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF'
    ]
    page = 1

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url=url,
                callback=self.parse,
                endpoint='render.html',
                args={
                    'wait': 15,
                },
            )

    def parse(self, response):
        for link in response.xpath(
                '//pb-feature-search-result-card/div/div/h4/a/@href').getall():
            annons_url = response.urljoin(link)
            yield SplashRequest(
                url=annons_url,
                callback=self.get_info,
                endpoint='render.html',
                args={
                    'wait': 10,
                },
            )
        self.page += 1
        next_page = f'https://arbetsformedlingen.se/platsbanken/annonser?page={self.page}&p=4:apaJ_2ja_LuF'
        yield SplashRequest(
            url=next_page,
            callback=self.parse,
            endpoint='render.html',
            args={
                'wait': 10,
            },
        )

    def get_info(self, response):
        job_obj = {}
        ad_id = response.xpath('//pb-section-job-about/div/h2[1]/text()').get()
        if ad_id == kill_id:
            raise CloseSpider(
                "start of last session is reached, spider is therefor killed.")
        else:
            ad_title = response.xpath(
                '//pb-section-job-quick-info/h1/text()').get()
            contact_name = response.xpath(
                '//pb-section-job-contact/div/div/ul/li/div[2]/div[1]/text()'
            ).get()
            contact_email = response.xpath(
                '//pb-section-job-contact/div/div/ul/li/div/div/a/@href').get(
                )
            apply_email = response.xpath(
                '//a[contains(@href, "@") and contains(@href, ".se")]/@href'
            ).get()
            apply_email_str = str(apply_email)
            apply_email_split = apply_email_str.split('?', 1)
            clean_apply_email = apply_email_split[0]
            job_obj['id'] = ad_id
            job_obj['title'] = ad_title
            job_obj['name'] = contact_name
            job_obj['contact-mail'] = contact_email
            job_obj['apply-mail'] = apply_email
            yield job_obj
