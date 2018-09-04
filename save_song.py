# 2018.9-4   by axiang 
# 网易云音乐歌词、歌曲爬取
# 爬取特定链接MP3,存取到特定名字
import requests
from bs4 import BeautifulSoup
import os

#获取网页源码
#url ="https://music.163.com/discover/toplist?id=3779629" 
#fv = { 'User-agent':"Mozilla/5.0"}
#r = requests.get(url, headers = fv )

#保存网页源码为txt,分析
#with open('F:\python\music1.txt','a+',encoding = 'utf-8') as f:
   # f.write(r.text)
   # print('保存完成')
   # f.close()

#下载特定歌曲
url = input('输入MP3网址：')
fv = { 'User-agent':"Mozilla/5.0"}
r = requests.get(url, headers = fv )

#保存到指定文件夹，没有文件夹创建
root = "F://get_down网易云音乐//"
song_name = input('请输入歌曲保存名字：')
path = root + song_name + '.mp3' #url.split('/')[-1]保存为网页最后一个/名字
if not os.path.exists(root):
    os.mkdir(root)
if not os.path.exists(path):
    with open(path,'wb') as f:
        f.write(r.content)
        print('保存完成')
        f.close()
else:
    print('file was exists!')
 
