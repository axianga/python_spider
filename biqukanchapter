# 2018.10.1  (by axiang)
#  寻找到小说的章节名称和连接，打印出章节名字和连接。保存
import requests
from bs4 import BeautifulSoup

def main():
	server = 'http://www.biqukan.com/'
	target = 'http://www.biqukan.com/1_1094/'
	r1 = requests.get(target)
	r1.raise_for_status()
	r1t = r1.text
	div_bs = BeautifulSoup(r1t,'lxml')
	#print(div_bs)
	div = div_bs.find_all('div', class_= 'listmain') # 寻找<div class="listmain>```</div>"
	#print(div)
	a_bs = BeautifulSoup(str(div),'lxml')
	a = a_bs.find_all('a')
	#print(a,'\n\n\n')
	for every in a:
		print(every.string,server + every.get('href'))
		cname = every.string 
		chref = server + every.get('href')
		with open('E://runcachefile//novelchapters104a2.txt','a',encoding ='utf-8') as f1:
			f1.write(cname + '        ' + chref +'\n')
	print('downloader finished!')

main()
