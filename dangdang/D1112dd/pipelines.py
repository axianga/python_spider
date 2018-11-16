# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class D1112DdPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1", user = "root", passwd = "root", db="dd")
        for i in range(0,len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            sql = "insert into ddbook(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"
            conn.query(sql)
            #print(str(i+1))
            print(title)
            #print(link)
            #print(comment)
        conn.close()
        print("save data to the database:dd table:ddboook!")
        return item
