 # -*- coding: utf-8 -*-
 # 33 scrapy自动爬取实战糗事百科
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from D115qsbkauto.items import D115QsbkautoItem

class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    #start_urls = ['http://www.qiushibaike.com/']

    def start_requests(self):
        ua = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        yield Request("http://www.qiushibaike.com/",headers = ua)
     

    rules = (
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = D115QsbkautoItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i["content"] = response.xpath("//div[@class='content']/text()").extract()
        i["link"] = response.xpath("//link[@rel ='canonical']/@href").extract()
        print(i["content"])
        print(i["link"])
        return i
