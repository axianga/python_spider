# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from D1116jd.items import D1116JdItem
import urllib.request
import re


class JdSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://www.jd.com/']
    
    # follow = True:对首页爬取到的网页进行爬取后，
    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),    
    )

    def parse_item(self, response):
        try:
            i = D1116JdItem()
            #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
            #i['name'] = response.xpath('//div[@id="name"]').extract()
            #i['description'] = response.xpath('//div[@id="description"]').extract()
            thisurl = response.url
            pat = r"item\.jd\.com/(.*)\.html"
            x = re.search(pat,thisurl)
            if(x):
                thisid = re.compile(pat).findall(thisurl)[0]
                print("goods url:  " + thisurl)
                title = response.xpath("//div[@class='sku-name']/text()").extract()
                shop = response.xpath("//div[@class='name']/a/text()").extract()
                shoplink = response.xpath("//div[@class='name']/a/@href").extract()
                #print(title)
                #print(shop)
                #print(shoplink)
                priceurl = "https://p.3.cn/prices/mgets?callback=jQuery7244950&skuIds=J_" + thisid
                commenturl = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4790&productId=" + thisid  + "&score=0&sortType=5&page=0&pageSize=10"
                #print(priceurl)
                #print(commenturl)
                pricedata = urllib.request.urlopen(priceurl).read().decode("utf-8","ignore")
                commentdata = urllib.request.urlopen(commenturl).read().decode("utf-8","ignore")
                pricepat = '"p":"(.*?)"'
                commentpat = '"goodRateShow":(.*?),'
                price = re.compile(pricepat).findall(pricedata)
                comment = re.compile(commentpat).findall(commentdata)
                #print(price)
                #print(comment)
                if (len(title) and len(shop) and len(shoplink) and len(price) and len(comment)):
                    print("good-info:   ")
                    print(title[0])
                    print(shop[0])
                    print(shoplink[0])
                    print(price[0])
                    print(comment[0])
                    print("------------------------")
                else:
                    pass
                    #print("获得的商品页面数据不齐全--------------------------------------------")
            else:
                pass
                #print("获取的页面不是商品页面:  " + thisurl)

            return i

        except Exception as e:
            print(e)





        
