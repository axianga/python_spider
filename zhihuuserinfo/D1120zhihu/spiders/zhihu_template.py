# -*- coding: utf-8 -*-
# 学习材料。

import scrapy
import json
from D1120zhihu.items import D1120ZhihuItem
import re
from scrapy.http import Request


class ZhihuSpider(scrapy.Spider):     #爬虫信息
    name = 'zhihu_template'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/members/chen-jun-15-6/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=40&limit=20']


    def parse(self, response):      #解析网页
        temp_data = json.loads(response.body.decode("utf-8"))["data"]        #爬取数据

        count = len(temp_data)      #当前页面爬取的用户数量
        if count < 20:
            pass

        else:                       #大于20，跳到还有下一页
            page_offset = int(re.findall("&offset=(.*?)&",response.url)[0])
            new_page_offset = page_offset + 20
            next_page_url = response.url.replace("&offset=" + str(page_offset) + "&","&offset=" + str(new_page_offset) +"&")
            yield scrapy.Request(url = next_page_url,callback = self.parse)

        for ever_user in temp_data:   #将爬取到的数据存到item
            
            item = D1120ZhihuItem()
            item["uname"] = ever_user["name"]
            item["url_token"] = ever_user["url_token"]
            item["headline"] = ever_user["headline"]
            item["follower_count"] = ever_user["follower_count"]
            item["answer_count"] = ever_user["answer_count"]
            item["articles_count"] = ever_user["articles_count"]
            item["uid"] = ever_user["id"]
            item["gender"] = ever_user["gender"]
            item["utype"] = ever_user["type"]
            item["url"] = ever_user["url"]
            
            with open("userinfo.txt",) as f:
                user_list = f.read()

            if ever_user["url_token"] not in user_list:
                with open("userinfo.txt","a") as f:
                    f.write(ever_user["url_token"] + "\n")  

                yield item 
 
                new_url = "https://www.zhihu.com/api/v4/members/" + ever_user["url_token"] + "/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20"
                yield scrapy.Request(url = new_url,callback = self.parse)