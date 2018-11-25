#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-25 01:17:59
# @Author  : axianga (513135258@qq.com)
# @Link    : https://github.com/axianga/python_spider
# @Version : $Id$
# 爬取链接：http://ip.jiangxianli.com/api/proxy_ips的ip列表
# 验证IP的可用与否，将可用的保存。
# 11月25号-2次版本（可用，代码尚未优化）

import requests
import json
import re
import time

#初始化
global temp_url,ip_url,ip_list,count,evecount,right,failnum,count_ip
ip_url = "http://ip.jiangxianli.com/api/proxy_ips"                #访问代理IP获取地址，此处获得的是json格式，m个代理IP
temp_url = "http://www.baidu.com"    #访问网址，IP查询,用于验证IP是否有效
ip_list = []                            #存储IP的列表
count = 0                              #计算使用IP的个数（第几个ip）
evecount = 0                          #每个IP的访问次数
right = 1                               #统计可以使用的ip
failnum = 1                             #统计访问失败的IP
count_ip = 0                            #访问ip列表的次数
repeat_ip = 0                           #访问成功ip的重复次数



def getIPData():                            #从代理IP处获得是个代理IP，先清空slef.ip_list,再存入ip_list的IP和port中。
    global temp_url,ip_list,ip_url,count_ip
    temp_data = requests.get(url=ip_url).text
    count_ip = count_ip + 1
    ip_list.clear()        #清空IP存储。
    for eve_ip in json.loads(temp_data)["data"]["data"]:        #json.loads(temp_data)["data"]["data"]:处理json文件，获取内容。
        ip_list.append({
            "ip":eve_ip["ip"],                  #获取ip、port 键的值。
            "port":eve_ip["port"] 
            })
        print(str(eve_ip["ip"]) + ":" + str(eve_ip["port"]))
    print(ip_list)
    print('\n')


def yanzheng():                             #验证代理IP是否可用，默认超时5s，requests.get代理IP设置
    print("yanzheng begin:   ")
    global count,right,temp_url,ip_list,count_ip,repeat_ip,failnum

    r = requests.get(url = temp_url,proxies = {"http":"http://"+str(ip_list[count-1]["ip"]) + ":" + str(ip_list[count-1]["port"])},timeout = 5)  #requests.get 代理IP设置
    r.encoding = r.apparent_encoding
    bd = re.compile("<title>(.*?)</title>").findall(r.text)[0]
    print(bd)  
    print(str(ip_list[count-1]["ip"]) + ":" + str(ip_list[count-1]["port"]))

    with open("changeProxy.txt") as f:         #打开文档
        aa = f.read()
    if str(ip_list[count-1]["ip"]) not in aa:       #IP去重，保存新IP
        with open("changeProxy.txt","a+") as f:
            f.write(str(ip_list[count-1]["ip"]) + ":" + str(ip_list[count-1]["port"]))
            f.write('\n')
            print("第{0:}个新IP保存成功，总IP数{2:}个，共爬取IP列表{3:}次，{1:}个重复IP，失效IP{4:}个".format(right,repeat_ip,count_ip*15 - 15 + count,count_ip,failnum - 1),end = "\n\n")
            right = right + 1
    else:
        repeat_ip = repeat_ip + 1
        print("第{1:}个重复IP，总IP数{2:}个，共爬取IP列表{3:}次，{0:}个新IP，失效IP{4:}个".format(right - 1,repeat_ip,count_ip*15 - 15 + count,count_ip,failnum - 1),end = "\n\n")

    if count == 15:                        #程序开始到IP池里最后一个代码,重新开始循环
        getIPData()                        #获取IP
        count = 1                          #计数=1，重新开始算
    else:
        count = count + 1
    ifUsed()

def ifUsed():                       #切换代理IP的跳板，访问请求，m是IP池总数，每一次IP池循环结束开始的地方
    print("ifused begin:    ")
    global count,evecount,failnum,count_ip
    try:
        print("ifUsed try:   ")
        yanzheng()
        #changeProxy()
    except:     #莫名奇妙执行
        print("ifUsed except:    ")
        print("目前失效IP数量：" + str(failnum) + "        共爬取IP数量：" + str(count_ip *15 - 15 + count),end = "\n\n" )
        failnum = failnum + 1
        if count == 15:
            time.sleep(5)
            getIPData()
            count = 1
        else:
            count = count + 1
        ifUsed()

def process():       #主要执行程序，代理IP使用规则，代理池共有m个IP，一个代理IP使用请求访问n次,n、m合理赋值
    global count,evecount
    print("process begin:   ")
    if count == 0 or count == 15:      #程序开始，或则到IP池里最后一个代码
        time.sleep(5)
        getIPData()                        #获取IP
        count = 1                          #计数=1，重新开始算
    else:
        count = count + 1

    ifUsed()            

if __name__ == '__main__':
    process()                     #程序执行

