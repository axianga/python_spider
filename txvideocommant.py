# 爬取腾讯视频评论，通过抓取评论的js文件，获取评论URL地址，分析其中的内容是Unicode编码，
# 通过输出源码发现' 'content":"(.*?)",'里面是评论内容。
# 并且下一页网址是：'"last":"(.*?)",'在里面的属性中
# 网址后缀需要加1
# 通过此处获得评论
import urllib.request
import re
import urllib.error

headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
openr = urllib.request.build_opener()
openr.addheaders = [headers]
urllib.request.install_opener(openr)
commentid = "6404918292604500679"
commantpage = 1
count = 1
url = "http://video.coral.qq.com/varticle/2657538333/comment/v2?callback=_varticle2657538333commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + commentid + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1540348787635"
for i in range(0,2):
	data = urllib.request.urlopen(url,timeout = 10).read().decode()
	patcom = '"content":"(.*?)",'
	comdata = re.compile(patcom).findall(data)
	for j in comdata[0:3]:
		print("第{}条评论内容是：".format(count))
		print(eval('u"'+ j + '"'))
		count = count + 1

	patnext = '"last":"(.*?)",'
	nextid = re.compile(patnext).findall(data)[0]
	print(nextid)
	url = "http://video.coral.qq.com/varticle/2657538333/comment/v2?callback=_varticle2657538333commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + nextid + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=" + str(1540348787635+commantpage)
	commantpage = commantpage + 1
	print(url)
