# -*- coding: utf-8 -*-
#对zhihu的用户信息爬取,抓取xhr存储的用户信息api，并发现规律。
#两种更换新url方法，一种是更换下一页，另一种是更换有关注的新用户。
#新用户是从已获取的用户中依次筛选可用的,
#返回的item可以添加去重，piplelines存储到设置mysql数据类型，可以自动去重

import scrapy
import json
from D1120zhihu.items import D1120ZhihuItem
import re
from scrapy.http import Request
import time


class ZhihuSpider(scrapy.Spider):                               # 爬虫信息
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    # start_urls = ['https://www.zhihu.com/api/v4/members/kong-cheng-ji-5-87/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20']

    start_urls = ['https://www.zhihu.com/api/v4/members/kong-cheng-ji-5-87/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20']



    def __init__(self):
        self.count_url_token = 0                                 # url_token 计数
        self.count_follower = 0                                  # follower_account 计数
        self.lst_url_token = []                                  # 列表存放url_token数量，用来更换用户。
        self.lst_follower =[]                                    # 记录已保存用户关注数量
        self.lst_url = []                                        # 去重复的列表url唯一量
        
    def parse(self, response):
        temp_data = json.loads(response.body.decode("utf-8"))["data"]        # 爬取数据

        for ever_user in temp_data:   #将爬取到的数据存到item
            #print(ever_user,end ='\n\n')

            if (temp_data):                                               #判断爬取的数据是否为空，空则不执行
            #存储follower_count的list

                item = D1120ZhihuItem()                                          #item赋值
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

                if item["url"] not in self.lst_url:                             #item去重复，把

                    self.lst_url_token.append(ever_user["url_token"])                #存储url_token的list，新用户网页的参数，
                    self.lst_follower.append(ever_user["follower_count"])          #用来确定是否可以用来当新用户网页访问
                    self.lst_url.append(ever_user["url"])                      #去重的判定条件
                    yield item 
            
        thisurl = response.url                                              #相应url
        pat1 = "&offset=(.*?)&"                                         
        oldoffset = int(re.compile(pat1).findall(thisurl)[0])               #获得当前url代表的页数参数

        if (len(temp_data) < 20 or oldoffset > 50):     # 数量不足，换用户，设置oldoffset > 50，是加快验证更换新用户网页的可行性，即爬到第三页关注的用户信息
            for follower in range(self.count_follower,len(self.lst_follower)):
                if (self.lst_follower[follower] > 5):                       #self.lst_follower[follower] > 5,代表用户有关注量，可以进行新用户页面派遣用户信息
                    self.count_follower = follower
                    break

            new_page_url = "https://www.zhihu.com/api/v4/members/" + str(self.lst_url_token[self.count_follower]) + "/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20"
            self.count_follower = self.count_follower + 1                   #新的用户计数加1，new_page_url 新用户页面。
            time.sleep(2)                                                   # 两秒爬取一个网页
            yield scrapy.Request(url = new_page_url, callback = self.parse, dont_filter =True)

        else:                                                               # 同一用户，跳到下一页    
            newoffset = oldoffset + 20
            newurl = thisurl.replace("&offset=" + str(oldoffset) + "&","&offset="+str(newoffset)+"&")
            time.sleep(2)                                # 两秒爬取一个网页
            yield scrapy.Request(url = newurl, callback = self.parse, dont_filter = True)