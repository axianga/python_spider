#10月22日
# http://www.58pic.com 爬取图片实战
import  urllib.request
import re
for i in range(1,3):
	Pageurl = 'http://www.58pic.com/haibaomoban/0/id-'+str(i)+'.html'
	Data = urllib.request.urlopen(Pageurl, timeout = 10).read().decode("utf-8","ignore")
	Pat = '<img  src="(.*?\.jpg)!'
	Imglist = re.compile(Pat).findall(Data)
	for j in range(0,2):   #   range(0,len(Imglist))
		try:
			Thisimg = Imglist[j]
			#Thisimgurl = Thisimg + ".jpg"
			File = "C:/apython/CacheFiles/58pic/1/" + str(i) + str(j) + ".jpg"
			urllib.request.urlretrieve(Thisimg,File)
			print("\r第{}页第{}个图片爬取成功".format(str(i),str(j+1)),end = "  ")
		except urllib.error.URLError as e:
			if hasattr(e,"code"):
				print(e.code)
			if hasattr(e,"reason"):
				print(e.reason)
		except Exception as er:
			print(er)
