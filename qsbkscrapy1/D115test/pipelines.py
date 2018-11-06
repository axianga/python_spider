# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class D115TestPipeline(object):
    def process_item(self, item, spider):
    	for i in range(0,len(item["content"])):
    		print(item["content"][i])
    		print(item["link"][i])
    	return item
