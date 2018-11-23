#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-23 20:26:50
# @Author  : axianga (513135258@qq.com)
# @Link    : https://github.com/axianga/python_spider
# @Version : $Id$


import re

thisurl = 'https://www.zhihu.com/api/v4/members/chen-jun-15-6/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=40&limit=20'
pat1 = "&offset=(.*?)&"
print(thisurl)
oldoffset = int(re.compile(pat1).findall(thisurl)[0])
print(oldoffset)
newoffset = oldoffset + 20
print(newoffset)
print(type(newoffset))
url = thisurl.replace(pat1,str(80))
print(thisurl)
print(type(thisurl))
print(type(url))