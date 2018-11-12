# -*- coding: utf-8 -*-
import scrapy
from D1112dd.items import D1112DdItem
from scrapy.http import Request


class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://www.dangdang.com/']

    def parse(self, response):
        item = D1112DdItem()
        item["title"] = response.xpath("//a[@class='pic']/@title").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comment"] = response.xpath("//a[@dd_name='单品评论']/text()").extract()
        yield item
        for i in range(2,3):
            url = "http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA%D3%EF%D1%D4&act=input&page_index="+ str(i)
            yield Request(url,callback = self.parse)