#12月2号，爬取美团美食类的子类及美食店铺名称
import requests
import re
import pymysql

def getHTMLText(url):           #模仿头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh,zh-CN;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'uuid=6adef61f84e44688a7c4.1543753266.1.0.0; _lxsdk_cuid=1676edd7e308c-0e723f8ea27f8c-6313363-130980-1676edd7e325; ci=20; rvct=20; IJSESSIONID=ndjrhuxlf9q71jdhxd99ihxye; iuuid=C7F23F3327D79FA0BEC042A97DEC2D4D8DFCF78C80D20CA1C4AFCA686FDD0F39; cityname=%E5%B9%BF%E5%B7%9E; _lxsdk=C7F23F3327D79FA0BEC042A97DEC2D4D8DFCF78C80D20CA1C4AFCA686FDD0F39; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; client-id=b3311601-dc4c-4a34-80ac-a8354fed3a0d; __mta=50298649.1543753305420.1543934660962.1543975627282.26; _lxsdk_s=1677c1e57ad-713-221-8b%7C%7C7',
        'Host': 'gz.meituan.com',
        'Referer': url,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    r = requests.get(url,headers = headers)
    r.raise_for_status()
    #print(r.encoding)
    r.ecoding = r.apparent_encoding
    return r.text

def parse(text):

    pat = '{"poiId":(.*?),"frontImg":".*?","title":"(.*?)","avgScore":(.*?),"allCommentNum":(.*?),"address":"(.*?)","avgPrice":(.*?),"dealList":.*?,"hasAds":.*?,"adsClickUrl":".*?","adsShowUrl":".*?"}'
    meishi_info = re.compile(pat).findall(text)
    for item in meishi_info:
        yield {
            'id':item[0],
            'title':item[1],
            'avgScore':item[2],
            'comments':item[3],
            'address':item[4],
            'avgPrice':item[5],
        }

def inserttomysql(i,db):
    sql = "insert into meishi(id,title,avgScore,comments,address,avgPrice) values('"+i["id"]+"','"+i["title"]+"','"+i["avgScore"]+"','"+i["comments"]+"','"+i["address"]+"','"+i["avgPrice"]+"')"
    db.query(sql)

def main():
    global url,count_down,count_rep,id_list
    count_down = 0
    count_rep = 0
    id_list = []
    db = pymysql.connect(host = "127.0.0.1",user = "root",passwd = "root", db = "mt")
    for i in range(2):
        url = "https://gz.meituan.com/meishi/pn" + str(i) + "/"
        r = getHTMLText(url)
        for item in parse(r):
            if item["id"] not in id_list:
                try:
                    inserttomysql(item,db)
                    count_down = count_down + 1
                    print("第{}条信息保存完成。".format(count_down))
                    id_list.append(item["id"])
                except Exception as e:
                    print(e)
                    count_rep = count_rep + 1
                    print("第{}条信息重复".format(count_rep))              
    db.close()
    print('finished')

if __name__ == '__main__':
    main()