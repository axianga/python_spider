#D9-28，照着样本敲代码系列-by axiang
#爬取东方财富股票列表和百度股票信息
#vesion 1
import requests                 # 常用网页请求库
from bs4 import BeautifulSoup   # 常用网页解析库
import traceback                # python异常处理之 traceback库
import re                       # 正则表达式，筛选文本作用

def getHTMLText(url):           # 定义请求网页源码格式，返回r.text
    try:
        r = requests.get(url)
        r.raise_for_status()    #  status_code 是 200 时，返回none，不成功时会抛出一个 HTTPError异常。
        r.encoding = r.apparent_encoding    # 编码赋值
        return r.text   
    
    except:
        print("getHTMLText_empty")
        return ""

def getStockList(lst, stock_list_url):  #获东方财富股票名称和代码，将代码存放到lst
    html = getHTMLText(stock_list_url)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])             ## 【0】？
        except:
            continue

def getStockInfo(lst, stockURL, fpath):    # 将上面得到的代码，加到百度股票网页中，获得该股票网页，再用BeautifulSoup获得相应的信息
    for stock in lst:                   # 取出第一个股票信息网页 解析存储
        url = stockURL + stock +".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})          #attrs from bs4

            name = stockInfo.find_all(attrs = {'class':'bets-name'})[0]   # bs4 的find_all  【0】？
            infoDict.update({'股票名称':name.text.split()[0]})      #【0】？

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding = 'utf-8') as f:             # 将股票信息保存到文本fpath，编码方式'utf-8'
                f.write( str(infoDict) + '\n')

        except:
            traceback.print_exc()    #返回异常信息
            continue
    #traceback.print_exc()函数只是traceback.print_exception()函数的一个简写形式，而它们获取异常相关的数据都是通过sys.exc_info()函数得到的
        
def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    fpath = "D:/stockinfo9.28.txt"
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, fpath)

main()

'''
------------------------------------------------------------------------
r 的 status_code 是 200 ，当我们调用 raise_for_status() 时，得到的是：
>>> r.raise_for_status()
None
-------------------------
find_all( name , attrs , recursive , string , **kwargs )                   # from bs4
------------------------------------------------------------
