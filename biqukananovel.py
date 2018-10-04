# 2018.10.4         (by axiang)
# 爬取小说的内容，节省时间给a[15:18]赋值，只爬取了三章。同理可以爬取想要的章节内容。
#count 后面修改没用上，本打算用作计算已下载章节数。
import requests
from bs4 import BeautifulSoup

def getHtmlText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		#r.encoding = r.apparent_encoding
		#print(r.encoding)
		return r.text
	except:
		print('getHtmlText error!\n')

def savethenovel(serverURL,novelURL,fpath):
	orginaltext = getHtmlText(novelURL)
	ot_soup = BeautifulSoup(orginaltext,"lxml")
	#print(ot_soup)  #检查解析网页响应情况
	ot = ot_soup.find_all('div', class_= 'listmain')
	#print(ot)       #检查获取的章节a 标签响应情况
	a_soup = BeautifulSoup(str(ot),"lxml")
	a = a_soup.find_all('a')

	count = 0
	for each in a[15:18]:
		html = serverURL + each.get('href')
		chp = getHtmlText(html)
		chp_soup = BeautifulSoup(chp,'lxml')
		chpc = chp_soup.find_all('div',class_= 'showtxt')
		novel = chpc[0].text.replace('\xa0'*8,'\n    ')
		with open(fpath,'a',encoding = "utf-8") as f1:
			f1.write(each.string)
			f1.write(str(novel) + '\n\n')
			count = count + 1
			print("\r已下载:{:.2f}%".format(count*100/(len(a[15:18]))),end= "")


def main():
	novelURL = 'http://www.biqukan.com/1_1094/'
	serverURL = 'http://www.biqukan.com/'
	fpath = 'E://runcachefile//ynyh2b1.txt'
	savethenovel(serverURL,novelURL,fpath)

main()
