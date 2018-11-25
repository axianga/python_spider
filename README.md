# python爬虫学习系列  

**目前接触库：/requests/BeautifulSoup/re/os/traceback/urllib/**

**--/scrapy/pymysql/threading/**  

**learning** **/scrapy-redis/**  **验证码处理**

---------------------------------------------------------------

1.1.[save-song.py](https://github.com/axianga/python/blob/master/save_song.py)                   （抓包分析）
(by axianga in 2018.9.3)

    --通过抓包工具fiddler或浏览器自带抓取到网页歌曲链接，保存音乐到本地。简单抓取原理。
    
1.2.[get58pic.py](https://github.com/axianga/python/blob/master/get58pic.py)                     （网页源码分析）
(by axianga in 2018.10.22)

    --查找到图片链接，保存图片到本地。
      
2.[stockInfo-easy.py](https://github.com/axianga/python/blob/master/stockInfo-easy.py)           （网页源码分析)
(by axianga in 2018.9.28)
 
    --爬取东方财富股票列表和百度股票信息。
  
3.[taobaogoodsinfo.py](https://github.com/axianga/python/blob/master/taobaogoodsinfo.py)         （网页源码分析）
(by axianga in 2018.9.25)

    --利用re库打印淘宝商品价格名称信息。
  
4.[stockInfo-easy2.py](https://github.com/axianga/python/blob/master/stockInfo-easy2.py)         （网页源码分析）
(by axianga in 2018.9.29)

    --爬取东方财富股票列表和百度股票信息，     
    --增加显示保存进度，修改获取网页编码方式赋值 （2号项目的版本的升级优化）。

5.[biqukanword.py](https://github.com/axianga/python/blob/master/biqukanword.py)                 （网页源码分析）
(by axianga in 2018.9.29)

    --笔趣网上的小说单章正文爬取保存。 
 
6.[biqukanchapter.py](https://github.com/axianga/python/blob/master/biqukanchapter.py)           （网页源码分析）
(by axianga in 2018.10.1)

    --笔趣网上的小说爬取每章章节名字和链接爬取保存。

7.[biqukananovel.py](https://github.com/axianga/python/blob/master/biqukananovel.py)              （网页源码分析）
(by axianga in 2018.10.4)

    --笔趣网上爬取小说的内容，节省时间给a\[15:18]赋值，只爬取了三章。同理可以爬取想要的章节内容。
8.[BDWKdownload.py（借鉴，实用）](https://github.com/axianga/python/blob/master/BDWKdownload.py)  (by axianga in 2018.10.6)

    --输入百度文库的URL，保存到该py文件同目录下，图片格式保存到图片文件夹，文档保存为文档。（👍）

9.[txvideocomment.py](https://github.com/axianga/python/blob/master/txvideocomment.py)            （抓包分析解码）
(by axianga in 2018.10.24)

    --通过对抓包工具FIddler的使用，对js文件进行抓取评论URL地址，打开URL发现文字评论段是Unicode编码，
    --在python中对Unicode 解读，证实是评论内容。页面关系也有相应的URL对应。 
 
10.[qsbkscrapy1](https://github.com/axianga/python/blob/master/qsbkscrapy1)                      （scrapy，basic,qsbk）
by axianga in 2018.11.6)

    --接触scrapy爬虫框架，使用基础爬虫模板basic，爬取糗事百科的段子及相关网页。
 
11.[qsbkscrapy2](https://github.com/axianga/python/blob/master/qsbkscrapy2)                       （scrapy,crawl,qsbk）
(by axianga in 2018.11.6)

    --接触scrapy爬虫框架，使用基础爬虫模板crawl，爬取糗事百科的段子及相关网页。
 
12.[tszn1scrapy](https://github.com/axianga/python/blob/master/tszn1scrapy)                       （scrapy,basic,txt） 
(by axianga in 2018.11.8)

    --接触scrapy爬虫框架，使用基础爬虫模板basic,爬取天善智能课程信息，并保存到txt文件中。
 
13.[dblogin](https://github.com/axianga/python/blob/master/dblogin)                               （scrapy,basic,db登陆请求）
(by axianga in 2018.11.11)

    --豆瓣模拟登陆scrapy爬虫框架，basic爬虫模板，半自动登陆验证码,爬取登陆后的信息
 
14.[dangdang1](https://github.com/axianga/python/blob/master/dangdang1)                          （scrapy,basic,dd）
(by axianga in 2018.11.12)

    --当当商城爬取商品信息，运用scrapy爬虫框架，basic爬虫模板，打印输出。
 
15.[dangdang](https://github.com/axianga/python/blob/master/dangdang)                             （scrapy,basic,pymysql）
(by axianga in 2018.11.16)

    --当当商城爬取商品信息，scrapy爬虫框架，basic爬虫模板，运用pymysql，将爬取到的数据保存到mysql数据库中，
    --数据库集成环境运用phpstudy，可视化操作采用navicat for mysql。

16.[qsbk_threading.py](https://github.com/axianga/python/blob/master/qsbk_threading.py)            （多线程threading，txt）
(by axianga in 2018.11.18)

    --爬取糗事百科的段子,多线程爬取,分成两个线程,一个线程爬取偶数页，一个线程爬取奇数页，运用多线程库/threading/
    --将爬取的内容进行保存，需要分开保存，保存到同一个文件夹会乱码。
   
17.[jd_scrapy_crawl](https://github.com/axianga/python/blob/master/jd_scrapy_crawl)               （scrapy,crawl,抓包分析）
(by axianga in 2018.11.18)   

    --运用scrapy爬虫框架，crawl爬虫模板，爬取jd商城商品页面。爬取商品名字信息、店铺、价格、好评率，
    --通过fiddler抓取的好评率、价格，目前价格容易出现问题，出现不稳定的时候，需要重新抓取，优化链接地址。
 
18.1[changeproxy.py](https://github.com/axianga/python/blob/master/ChangeProxy/changeproxy.py)                  （代理IP更换，爬虫必备）
(by axianga in 2018.11.20)   

    --scrapy爬虫框架,代理IP更换，此段功能放在middlewares.py中.
    --需要在settings.py中开启DOWNLOADER_MIDDLEWARES，将原middlewares.py的DOWNLOADER_MIDDLEWARES注释掉，用changeproxy取代。
    --代理ip需要购买，较为可靠，免费的IP效率低。
    
18.2[changeproxyR2.py](https://github.com/axianga/python/blob/master/ChangeProxy/changeproxyR2.py)                  （代理IP更换验证）
(by axianga in 2018.11.25)   

    --验证IP的可用与否，将可用的保存到txt。（可用，代码尚未优化）


19.[jdmysql1_scrapy_crawl](https://github.com/axianga/python/blob/master/jdmysql1_scrapy_crawl)      （scrapy,crawl,pymysql） 
(by axianga in 2018.11.20)   

    --运用scrapy爬虫框架，crawl爬虫模板，爬取jd商城商品页面。爬取商品名字信息、店铺、价格、好评率，
    --通过fiddler抓取的好评率、价格，目前价格容易出现问题，出现不稳定的时候，需要重新抓取，优化链接地址。
    --将抓取的数据处理优化，保存到MySQL数据库中。
    
 
20.[zhihuuserinfo](https://github.com/axianga/python/blob/master/zhihuuserinfo/)                (scrapy,basic,抓包分析，json，pymysql）
(by axianga in 2018.11.23)   

    --对zhihu的用户信息爬取,抓取xhr存储的用户信息api，保存到mysql数据库中。
    --（无代理IP设置，爬到一定程度可能会被ban）
    
    
    
    
