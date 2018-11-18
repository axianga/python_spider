# 爬取糗事百科的段子
# 多线程爬取,分成两个线程
# 一个线程爬取偶数页，一个线程爬取奇数页
# 将爬取的内容进行保存，需要分开保存，保存到同一个文件夹会乱码

import urllib.request
import re
import urllib.error
import threading

headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
openr = urllib.request.build_opener()
openr.addheaders = [headers]
urllib.request.install_opener(openr)

class One(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		for i in range(1,36,2):
			url = "http://www.qiushibaike.com/8hr/page/" + str(i) +'/'
			try:
				data = urllib.request.urlopen(url,timeout = 10).read().decode("utf-8","ignore")
			except urllib.error.URLError as e:
				if hasattr(e,"code"): 
					print(e.code)
				if hasattr(e,"reason"):
					print(e.reason)
			except Exception as e:
				print(e)	
			pat ='<div class="content">.*?<span>(.*?)</span>.*?</div>'
			joke = re.compile(pat,re.S).findall(data)
			for j in joke:
				with open('C:/apython/CacheFiles/qsbkjoke2-1.txt','a',encoding = "utf-8") as f:
					f.write(str(j))
					#f.write('\n')
			print("  1号线程第{}页段子保存完成\n".format(i),end =" ")  

class Two(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		for i in range(0,36,2):
			url = "http://www.qiushibaike.com/8hr/page/" + str(i) +'/'
			try:
				data = urllib.request.urlopen(url,timeout = 10).read().decode("utf-8","ignore")
			except urllib.error.URLError as e:
				if hasattr(e,"code"): 
					print(e.code)
				if hasattr(e,"reason"):
					print(e.reason)
			except Exception as e:
				print(e)	
			pat ='<div class="content">.*?<span>(.*?)</span>.*?</div>'
			joke = re.compile(pat,re.S).findall(data)
			for j in joke:
				with open('C:/apython/CacheFiles/qsbkjoke2-2.txt','a',encoding = "utf-8") as f:
					f.write(str(j))
					#f.write('\n')
			print("2号线程第{}页段子保存完成\n".format(i),end =" ")  

one = One()
one.start()
two = Two()
two.start()
