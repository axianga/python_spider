# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class D116Tszn1Pipeline(object):
    def __init__(self):
        self.fh = open("c:/apython/SpiderFiles/In2018/D116Tszn1/1.txt",'a')
    def process_item(self, item, spider):
        '''
        print(item["title"])
        print(item["link"])
        print(item["stu"])
        print("--------------------------------------------------")
        '''
        self.fh.write(item["title"][0]+"\n"+ item["link"][0] + "\n" + item["stu"][0] + "\n" + "--------------------------")
        return item

    def close_spider(self):
        self.fh.close()
