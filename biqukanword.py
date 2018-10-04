# 2018.9-29			 (by axiang)
# 寻找到小说章节正文，并去掉空格标签对 ，首行缩进两个字，四个空格。保存
import requests
from bs4 import BeautifulSoup

def main():
	url = "http://www.biqukan.com/1_1094/5403177.html"
	r = requests.get(url, timeout= 30)
	r.raise_for_status()
	print(r.encoding)
	soup = r.text
	booksoup = BeautifulSoup(soup, 'lxml')

	booktext = booksoup.find_all('div', class_ = "showtxt")
	print(booktext)
	with open("E://runcachefile//biqubook10.1a1.txt",'a',encoding = "utf-8") as f1:
		f1.write(str(booktext))
		print("download f1 finished!\n")
	chapter = booktext[0].text.replace('\xa0'*8,'\n    ')
	print(chapter)

	with open("E://runcachefile//biqubook10.4b3.txt",'a',encoding = "utf-8") as f2:
		f2.write(str(chapter))
		print("download f2 finished!/\n")

main()  
