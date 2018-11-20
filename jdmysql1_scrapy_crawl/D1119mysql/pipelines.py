# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class D1119MysqlPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host= "127.0.0.1",user = "root",passwd = "root",db = "jd1119")
    
    def process_item(self, item, spider):    
        #for i in range(0,len(item["title"])):
        title = item["title"]
        url = item["url"]
        shop = item["shop"]
        shoplink = item["shoplink"]
        price = item["price"]
        comment = item["comment"]
        sql = "insert into goodsinfo(title,url,shop,shoplink,price,comment) values('"+title+"','"+url+"','"+shop+"','"+shoplink+"','"+price+"','"+comment+"')"
        self.db.query(sql)
        #db.close()
        print("该商品信息已保存到数据库")
        print("------------------------")
        return item
    
    def close_spider(self):
        self.db.close()
   