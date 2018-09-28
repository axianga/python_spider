#打印淘宝搜索商品的信息
#D9-25 利用re库打印淘宝商品价格名称信息
import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encording = r.apparent_encoding
        return r.text
    except:
        print("getHTMLTest error")

def parsePage(ilt,html):
    try:
        # 以列表类型返回全能匹配的子串
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        #正则表达式的最小匹配
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
            print("出现异常！")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))
    
def main():
    goods = "水杯"
    depth = 1
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i) #i 打印的页数 第一页为i=0
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)


main()
