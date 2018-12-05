import requests
import re
import json
from lxml import etree
import pymysql


global hotel,id_list,count_down,count_rep 
hotel = {}
id_list = []
count_down = 1
count_rep = 1 
def getHTMLText(url):
    headers = {
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, __skcy',
            'Access-Control-Allow-Methods': 'POST,GET,PUT,PATCH,DELETE,OPTIONS',
            'Access-Control-Allow-Origin': 'https://hotel.meituan.com',
            'Access-Control-Max-Age': '1728000',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=utf-8',
            'M-SpanName': '/HotelSearch'
        }
    r = requests.get(url,headers = headers)
    r.raise_for_status()
    #print(r.encoding)
    #r.ecoding = r.apparent_encoding
    return r.text

def parse(text,db):
    global hotel,id_list,count_down,count_rep
    html = json.loads(text)["data"]["searchresult"]
    for every in html:

        hotel["id"] = str(every["poiid"])
        hotel["classify"] = every["hotelStar"]
        hotel["address"] = every["addr"]
        hotel["lowestprice"] = str(every["lowestPrice"])
        hotel["avgScore"] = str(every["avgScore"])
        hotel["name"] = every["name"]
        hotel["evaluateNumber"] = str(every["markNumbers"])
        hotel["historySale"] = every["historySaleCount"] 
        hotel["special"] = str(str(every["poiAttrTagList"]).replace('[','').replace(']','').replace('\'','').replace('"',''))
        hotel["sevice"] = str(str(every["serviceDesc"]).replace('[','').replace(']','').replace('\'','').replace('"',''))
        hotel["specialTags"] = str(str(every["specialTags"]).replace('\'','').replace('[','').replace(']',''))
        hotel["starttime"] = str(str(every["forward"]["poiExtendsInfosDesc"]).replace('\'','').replace('[','').replace(']',''))
        if hotel["id"] not in id_list:
            try:
                inserttomysql(hotel,db)
                print("第{}条信息保存完成。".format(count_down))
                count_down = count_down + 1
                id_list.append(hotel["id"])
            except Exception as e:
                print(e)
                print("第{}条酒店信息重复".format(count_rep))
                count_rep = count_rep + 1

    return hotel

def inserttomysql(i,db):
    sql = "insert into hotel(id,classify,address,avgScore,lowestprice,name,evaluateNumber,historySale,special,sevice,specialTags,starttime) values('"+i["id"]+"','"+i["classify"]+"','"+i["address"]+"','"+i["avgScore"]+"','"+i["lowestprice"]+"','"+i["name"]+"','"+i["evaluateNumber"]+"','"+i["historySale"]+"','"+i["special"]+"','"+i["sevice"]+"','"+i["specialTags"]+"','"+i["starttime"]+"')"
    db.query(sql)

def main():
    db = pymysql.connect(host= '127.0.0.1',user = 'root',passwd = 'root', db = 'mt')
    for i in range(1,2):
        url = 'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=C7F23F3327D79FA0BEC042A97DEC2D4D8DFCF78C80D20CA1C4AFCA686FDD0F39%401543835469928&cityId=20&offset=' + str(i*20) + '&limit=20&startDay=20181204&endDay=20181205&q=&sort=defaults&X-FOR-WITH=k3xPx16Pg44b6dIK89FZX%2FPm3L97jdCrfrx%2B6G6CKgmB4vD%2BNNwxg9xLyteBC1Rc2pQTzky33uoUzPNF79giLDSkhjgS%2FrufY%2FpQGxtc5eUax%2BU3xW3ImUwmFOXseuq9%2FP5%2BeH0GKZCWOzAG0WRQIQ%3D%3D'
        r = getHTMLText(url)
        t = parse(r,db)
    db.close()

if __name__ == '__main__':
    main()