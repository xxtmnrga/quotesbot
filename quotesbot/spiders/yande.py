# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'yandere'
    start_urls = [
        'https://yande.re/post',
    ]

    def parse(self, response):
        for quote in response.xpath('//a[@class="thumb"]'):
            yield {
                'imgurl': quote.xpath('./img/@src').extract_first(),
            }
        image_urls = scrapy.Field()
        next_page_url = response.xpath('//a[@class="next_page"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

