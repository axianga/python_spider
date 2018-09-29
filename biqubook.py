# first learn
# D9-29 2018   (by axiang)
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
	with open("E://runningfile//biqubook9.29a1.txt",'a',encoding = "utf-8") as f:
		f.write(str(booktext))

main()  
