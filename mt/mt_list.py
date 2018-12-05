#12月3号
#爬取美团分类信息(url = "https://gz.meituan.com/")。

import requests
from lxml import etree

def getHTMLText(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh,zh-CN;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'uuid=6adef61f84e44688a7c4.1543753266.1.0.0; _lxsdk_cuid=1676edd7e308c-0e723f8ea27f8c-6313363-130980-1676edd7e325; ci=20; rvct=20; client-id=eaef9472-8f15-47dc-aaf4-e26c55200d79; IJSESSIONID=ndjrhuxlf9q71jdhxd99ihxye; iuuid=C7F23F3327D79FA0BEC042A97DEC2D4D8DFCF78C80D20CA1C4AFCA686FDD0F39; cityname=%E5%B9%BF%E5%B7%9E; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=C7F23F3327D79FA0BEC042A97DEC2D4D8DFCF78C80D20CA1C4AFCA686FDD0F39; __mta=50298649.1543753305420.1543800712915.1543800795470.22; _lxsdk_s=16771858275-338-d03-9a3%7C%7C23',
        'Host': 'gz.meituan.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    r = requests.get(url,headers = headers,verify = False)
    r.raise_for_status()
    print(r.encoding)
    r.ecoding = r.apparent_encoding
    with open('mt_html.txt','w',encoding = 'utf-8') as f:
        f.write(r.text)
    return r.text

def parse(text):
    html = etree.HTML(text)
    mt_list = html.xpath('//div[@class="category-nav-content-wrapper"]/ul/li/span/span/a/text()')
    list_menu = html.xpath('//div[@class="detail-content"]/a/text()')
    print(mt_list)
    print(list_menu)
    with open("mt_list.txt",'a',encoding = "utf-8") as f:
        f.write("美团全部分类："+ '\n'+ str(mt_list) + "\n\n")
        f.write("美团全部分类字段："+ '\n'+ str(list_menu) + "\n\n")


def main():
    url = "https://gz.meituan.com/"
    r = getHTMLText(url)
    parse(r)
    print('finished')

if __name__ == '__main__':
    main()