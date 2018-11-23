# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 存储到mysql数据库中用insert函数，需要插入的数据类型为str，把int改为str，不能整数类型。mysql表中需要设置相对应的数据是什么。

import pymysql

class D1120ZhihuPipeline(object):
    def __init__(self):    #初始化链接数据库
        self.db = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="spiderdata")
        self.count = 1

    def process_item(self, item, spider):#将item值存进数据库中
        uname = item["uname"]
        url_token = item["url_token"]
        headline = item["headline"]
        follower_count = str(item["follower_count"])
        answer_count =str(item["answer_count"])
        articles_count =str(item["articles_count"])
        uid = item["uid"]
        gender =str(item["gender"])
        utype = item["utype"]
        url = item["url"]

        #insertsql = "insert into zhihu_userinfo(name,url_token,headline,follower_count,answer_count,articles_count,id,gender,type,url) values('"+uname+"','"+url_token+"','"+headline+"','"+follower_count+"','"+answer_count+"','"+articles_count+"','"+uid+"','"+gender+"','"+utype+"','"+url+"')"
        insertsql = "insert into test(name,id) values('"+uname+"','"+url+"')"
        self.db.query(insertsql)
        print("第{:}条数据存储成功".format(self.count))
        self.count = self.count + 1

        return item

    def close_spider(self):   #结束，关闭数据库
        self.db.close()
