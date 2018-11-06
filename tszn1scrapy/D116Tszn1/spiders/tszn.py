# -*- coding: utf-8 -*-
import scrapy
from D116Tszn1.items import D116Tszn1Item
from scrapy.http import Request

class TsznSpider(scrapy.Spider):
    name = "tszn"
    allowed_domains = ["hellobi.com"]
    start_urls = ['https://edu.hellobi.com/course/1']

    def parse(self, response):
        item = D116Tszn1Item()
        item["title"] = response.xpath('//div[@class="course-info"]/h1/text()').extract()
        item["link"] = response.xpath('//ul[@class="nav nav-tabs"]/li[@class="active"]/a/@href').extract()
        item["stu"] = response.xpath('//span[@class="course-view"]/text()').extract()
        yield item
        for i in range(2,297):
            url = "https://edu.hellobi.com/course/" + str(i)
            yield Request(url,callback = self.parse)