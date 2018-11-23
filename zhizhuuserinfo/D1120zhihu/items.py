# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class D1120ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    uname = scrapy.Field()
    url_token = scrapy.Field()
    headline = scrapy.Field()
    follower_count =scrapy.Field()
    answer_count =scrapy.Field()
    articles_count =scrapy.Field()
    uid = scrapy.Field()
    gender =scrapy.Field()
    utype = scrapy.Field()
    url = scrapy.Field()
