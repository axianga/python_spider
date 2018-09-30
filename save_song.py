# 2018.9-4   by axiang 
# 网易云音乐歌词、歌曲爬取
# 爬取特定链接MP3,存取到特定名字
import requests    #常用网页请求库
from bs4 import BeautifulSoup     #常用解析库
import os                #os库下面有大概介绍

#获取网页源码
#url ="https://music.163.com/discover/toplist?id=3779629" 
#fv = { 'User-agent':"Mozilla/5.0"}                          # headers 模仿浏览器访问
#r = requests.get(url, headers = fv )                        # requests.get()获得页面源码

#保存网页源码为txt,分析
#with open('F:\python\music1.txt','a+',encoding = 'utf-8') as f:
   # f.write(r.text)
   # print('保存完成')
  
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
 

'''
-----------------------------------------------------------------------------
os库常用函数
       提供了访问多个操作系统的功能.它的子模块也提供了操作文件和目录
       以及处理路径的方法,掌握os模块,可以让python代码做到平台无关,增强了代码的
       可移植性.可以通过help命令和dir命令了解os模块所有定义的常量和函数.


os.getcwd()         ##返回程序的当前路径
os.getlistdir(path) ##返回指定目录下的所有文件和目录名
os.remove()         ##删除一个文件
os.removedirs(path) ##删除多个目录
os.chdir(path)      ##更改工作区目录
os.mkdir(path)      ##创建一个文件夹
os.rmdir(path)      ##删除一个文件夹
os.rename(oldname,newname) ##重命名12345678



os.path库常用操作

os.path.isfile(path)    ##检测路径是否为文件
os.path.isdir()         ##检测路径是否文文件夹
os.path.exists()        ##检测路径是否存在
os.path.splitext()      ##分离文件名和扩展名
os.path.split()         ##返回一个路径的目录名和文件名
os.path.dirname()       ##获得路径的路径名
os.path.basename()      ##获得文件名
os.path.getsize()       ##获得文件大小
os.path.join(path,name) ##返回绝对路径
os.walk(path)           ##自顶向下遍历一个目录，返回一个三元组12345678910

os.walk()使用范例：

import os
for root,dirs,files in os.walk(path):
    for name in files:
        print(os.path.join(root,name))

-------------------------------------------------------------------------
'''
'''
-----------------------------------------------------------------------------------------------------------------------
with open() as f:
with open('F:\python\music1.txt','a+',encoding = 'utf-8') as f:

r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被
      写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的
      内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果
      该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不
      存在，创建新文件用于读写。
--------------------------------------------------------------------------------------------------------------------------
'''
'''
-----------------------------------------------------------------------
  r.text返回的是Unicode型的数据。 
  r.content返回的是bytes型也就是二进制的数据。 
  也就是说，如果你想取文本，可以通过r.text。 
  如果想取图片，文件，则可以通过r.content。 
 （r.json()返回的是json格式数据）
-----------------------------------------------------------------------
''''''''
