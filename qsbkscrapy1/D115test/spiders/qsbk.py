  # -*- coding: utf-8 -*-
  # 33 基本爬虫爬取糗事百科段子和网址
import scrapy
from D115test.items import D115TestItem
from scrapy.http import Request
print("begin!")
class QsbkSpider(scrapy.Spider):
    name = "qsbk"
    allowed_domains = ["qiushibaike.com"]
    #start_urls = ['http://qiushibaike.com/']

    def start_requests(self):
      ua = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
      yield Request("http://www.qiushibaike.com/",headers = ua)
     
    def parse(self, response):
      it = D115TestItem()
      it["content"] = response.xpath("//div[@class='content']/span/text()").extract()
      it["link"] = response.xpath("//a[@class ='contentHerf']/@href").extract()
      yield it
print("end!")
