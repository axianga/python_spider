#scrapy爬虫框架
#代理IP更换，合理优化，此段功能放在middlewares.py中，并在settings.py中开启DOWNLOADER_MIDDLEWARES，将类名称换为此名称。
impore requests
import json
class ChangeProxy(object):         					# 程序运行：__init__  到  process_request

	def __init__(self):								#初始化
		self.get_url = "获取代理IP地址"			   	#访问代理IP获取地址，此处获得的是json格式，m个代理IP
		self.temp_url = "http://up.chinaz.com/getip.aspx"    #访问网址，IP查询
		self.ip_list = []
		self.count = 0								#计算使用IP的个数（第几个ip）
		self.evecount = 0							#每个IP的访问次数

	def getIPData(self):                      		#从代理IP处获得是个代理IP，先清空slef.ip_list,再存入self.ip_list的IP和port中。
		temp_data = requests.get(url=self.get_url).text()
		self.ip_list.clear()		#清空IP存储。
		for eve_ip in json.loads(temp_data)["result"]:	    #json.loads(temp_data)["result"]:处理json文件，获取result里面的内容。
			self.ip_list.append({
				"ip":eve_ip["ip"],					#获取ip、port 键的值。
				"port":eve_ip["port"] 
				})

	def changeProxy(self,request):      			#更改为代理IP
		request.meta["proxy"] = "http://" + str(self.ip_list[self.count-1]["ip"]) + ":" + str(self.ip_list[self.count-1]["port"])
	
	def yanzheng(self):								#验证代理IP是否可用，默认超时5s
		requests.get(url = self.temp_url,proxies = {"http://"+str(self.ip_list[self.count-1]["ip"]) + ":" + str(self.ip_list[self.count-1]["port"])},timeout = 5)	

	def ifUsed(self,request):						#切换代理IP的跳板，访问请求，m是IP池总数，每一次IP池循环结束开始的地方

		try:
			self.changeProxy(request)
			self.yanzheng()
		except:
			if self.count == m:
				self.getIPData()
				self.count = 1
			self.count = self.count + 1
			self.ifUsed(request)

	def process_request(self,request,spider):    	#主要执行程序，代理IP使用规则，代理池共有m个IP，一个代理IP使用请求访问n次,n、m合理赋值
		
		if self.count == 0 or self.count == m:     	#程序开始，或则到IP池里最后一个代码
			self.getIPData()		               	#获取IP
			self.count = 1			               	#计数=1，重新开始算

		if self.evecount == n:
			self.count = self.count + 1
			self.evecount= 0
		else:
			self.evecount = self.evecount + 1

		self.ifUsed(request）			
