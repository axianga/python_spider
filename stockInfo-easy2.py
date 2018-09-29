#D9-28-2018  （by axiang）
#爬取东方财富股票列表和百度股票信息
#增加显示文件保存进度，优化网页编码获取方式
#vesion 2
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url,encoding = "utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = encoding
        return r.text
    
    except:
        print("getHTMLText_empty")
        return ""

def getStockList(lst, stock_list_url):
    html = getHTMLText(stock_list_url,"GB2312")
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock +".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs = {'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding = 'utf-8') as f:
                f.write( str(infoDict) + '\n')
                count = count+1
                print("\r当前进度:{:.2f}%".format(count*100/len(lst)),end = "")

        except:
            count = count + 1
            print("\r当前进度：{:.2f}%".format(count*100/len(lst)),end = "")
            continue
    
        
def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    fpath = "D:/stockinfo9.29a.txt"
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, fpath)

main()
