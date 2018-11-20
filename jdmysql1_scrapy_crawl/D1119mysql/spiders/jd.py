# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from D1119mysql.items import D1119MysqlItem
import urllib.request
import re


class JdSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://www.jd.com/']
    
    # follow = True:对首页爬取到的网页进行爬取后，对子网页继续爬取
    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),    
    )

    def parse_item(self, response):
        try:
            item = D1119MysqlItem()
            #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
            #i['name'] = response.xpath('//div[@id="name"]').extract()
            #i['description'] = response.xpath('//div[@id="description"]').extract()
            thisurl = response.url
            pat = r"item\.jd\.com/(.*)\.html"
            x = re.search(pat,thisurl)
            if(x):
                thisid = re.compile(pat).findall(thisurl)[0]
                #print("goods url:  " + thisurl)
                item["url"] = thisurl
                titleraw = response.xpath("//div[@class='sku-name']/text()")[0].extract()
                item["shop"] = response.xpath("//div[@class='name']/a/text()")[0].extract()
                item["shoplink"] = response.xpath("//div[@class='name']/a/@href")[0].extract()
                #title商品名称处理，
                item["title"] = ''.join(titleraw).replace('\n','').replace(' ','')
                #print(title)
                #print(shop)
                #print(shoplink)
                priceurl = "https://p.3.cn/prices/mgets?callback=jQuery689703&type=1&area=1_72_2799_0&pdtk=&pduid=15423739186521491528917&pdpin=&pin=null&pdbp=0&skuIds=J_" + thisid
                commenturl = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4790&productId=" + thisid  + "&score=0&sortType=5&page=0&pageSize=10"
                #print(priceurl)
                #print(commenturl)
                pricedata = urllib.request.urlopen(priceurl).read().decode("utf-8","ignore")
                commentdata = urllib.request.urlopen(commenturl).read().decode("utf-8","ignore")
                pricepat = '"p":"(.*?)"'
                commentpat = '"goodRateShow":(.*?),'
                item["price"] = re.compile(pricepat).findall(pricedata)[0]
                item["comment"] = re.compile(commentpat).findall(commentdata)[0]
                #print(price)
                #print(comment)
                if (len(item["title"]) and len(item["shop"]) and len(item["shoplink"]) and len(item["price"]) and len(item["comment"])):
                    print("good-info:   ")
                    print(item["url"])
                    print(item["title"])
                    print(item["shop"])
                    print(item["shoplink"])
                    print(item["price"])
                    print(item["comment"])
                    print("------------------------")
                    yield item
                else:
                    pass
                    #print("获得的商品页面数据不齐全--------------------------------------------")
            else:
                pass
                #print("获取的页面不是商品页面:  " + thisurl)

            return item

        except Exception as e:
            print(e)





        
