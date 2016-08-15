# -*- coding: utf-8 -*-

import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    start_urls = [
        "http://www.chinadmoz.org/industry/4/",
        "http://www.chinadmoz.org/industry/2/"
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2]
        with open(filename, 'w+') as f:
            f.write(response.body)
