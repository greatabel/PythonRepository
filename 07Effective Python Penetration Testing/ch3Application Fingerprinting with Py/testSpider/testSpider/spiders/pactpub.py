# -*- coding: utf-8 -*-
import scrapy


class PactpubSpider(scrapy.Spider):
    name = "pactpub"
    allowed_domains = ["pactpub.com"]
    start_urls = ['http://pactpub.com/']

    def parse(self, response):
        pass
