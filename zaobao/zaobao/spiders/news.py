# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["zaobao.com"]
    start_urls = ['http://www.zaobao.com/special/report/politic/fincrisis']

    def parse(self, response):
        for href in response.css('.main-content a::attr(href)'):
            full_url=response.urljoin(href.extract())
            yield scrapy.Request(full_url,callback=self.parse_question)
    def parse_question(self,response):
        yield{
            'title':response.css('h1::text').extract()[0],
            'time':response.css('.trackme .datestamp::text').extract(),
            'body':response.css('.article-content-container').extract()[0],
            'link':response.url,
            }
