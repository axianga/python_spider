# python爬虫学习系列  

****

**库的使用：/requests/BeautifulSoup/re/os/traceback/urllib/**

**--/scrapy/pymysql/threading/**

**查看网页源码，查看网络请求。抓包工具Fiddler使用。**

**Git简单操作学习，上传到github文件多的时候使用**

---------------------------------------------------------------

1.[save-song.py](https://github.com/axianga/python/blob/master/save_song.py)
(by axiang in 2018.9.3)

  查找到网页歌曲资源链接信息，并进行保存--
  
2.[stockInfo-easy.py](https://github.com/axianga/python/blob/master/stockInfo-easy.py)     (by axiang in 2018.9.28)
 
  爬取东方财富股票列表和百度股票信息--
  
3.[taobaogoodsinfo.py](https://github.com/axianga/python/blob/master/taobaogoodsinfo.py)    (by axiang in 2018.9.25)

  利用re库打印淘宝商品价格名称信息
  
4.[stockInfo-easy2.py](https://github.com/axianga/python/blob/master/stockInfo-easy2.py)     (by axiang in 2018.9.29)

  爬取东方财富股票列表和百度股票信息--
  
  增加显示保存进度，修改获取网页编码方式赋值 （2的版本的升级版）

5.[biqukanword.py](https://github.com/axianga/python/blob/master/biqukanword.py)     (by axiang in 2018.9.29)

  笔趣网上的小说单章正文爬取保存--
 
6.[biqukanchapter.py](https://github.com/axianga/python/blob/master/biqukanchapter.py)     (by axiang in 2018.10.1)

  笔趣网上的小说爬取每章章节名字和链接爬取保存--

7.[biqukananovel.py](https://github.com/axianga/python/blob/master/biqukananovel.py)     (by axiang in 2018.10.4)

  笔趣网上爬取小说的内容，节省时间给a\[15:18]赋值，只爬取了三章。同理可以爬取想要的章节内容--

8.[BDWKdownload.py](https://github.com/axianga/python/blob/master/BDWKdownload.py)     (by axiang in 2018.10.6)

  输入百度文库的URL，保存到该py文件同目录下，图片格式保存到图片文件夹，文档保存为文档--



9.[txvideocommant.py](https://github.com/axianga/python/blob/master/txvideocommant.py)     (by axiang in 2018.10.24)

  -通过对抓包工具FIddler的使用，对js文件进行抓取评论URL地址，打开URL发现文字评论段是Unicode编码，也可以通过浏览器开发者模式看，
 
   在python中对UNICODe 解读，证实是评论内容。页面关系也有相应的URL对应。
 
 
10.[qsbkscrapy1](https://github.com/axianga/python/blob/master/qsbkscrapy1)     (by axiang in 2018.11.6)

   -接触scrapy库，使用基础爬虫模板basic，爬取糗事百科的段子及相关网页。
 
 
11.[qsbkscrapy2](https://github.com/axianga/python/blob/master/qsbkscrapy2)     (by axiang in 2018.11.6)

   -接触scrapy库，使用基础爬虫模板crawl，爬取糗事百科的段子及相关网页。
 
 
12.[tszn1scrapy](https://github.com/axianga/python/blob/master/tszn1scrapy)     (by axiang in 2018.11.8)

   -接触scrapy库，使用基础爬虫模板basic,爬取天善智能课程信息，并保存到txt文件中。
 
 
13.[dblogin](https://github.com/axianga/python/blob/master/dblogin)     (by axiang in 2018.11.11)

   -豆瓣模拟登陆scrapy，basic爬虫模板，半自动登陆验证码,爬取登陆后的信息
 
14.[dangdang1](https://github.com/axianga/python/blob/master/dangdang1)     (by axiang in 2018.11.12)

   -当当商城爬取商品信息，scrapy，basic爬虫模板，打印输出。
 
15.[dangdang](https://github.com/axianga/python/blob/master/dangdang)     (by axiang in 2018.11.16)

   -当当商城爬取商品信息，scrapy，basic爬虫模板，运用pymysql，将爬取到的数据保存到mysql数据库中，
 
   数据库集成环境运用phpstudy，可视化操作采用navicat for mysql.

16.[qsbk_threading.py](https://github.com/axianga/python/blob/master/qsbk_threading.py)     (by axiang in 2018.11.18)

   --爬取糗事百科的段子,多线程爬取,分成两个线程,一个线程爬取偶数页，一个线程爬取奇数页

   将爬取的内容进行保存，需要分开保存，保存到同一个文件夹会乱码
   
17.[jd_scrapy_crawl](https://github.com/axianga/python/blob/master/jd_scrapy_crawl)     (by axiang in 2018.11.18)   

    --运用scrapy爬虫框架，crawl爬虫模板，爬取jd商城商品页面。爬取商品名字信息、店铺、价格、好评率.   
    --通过fiddler抓取的好评率、价格，目前价格容易出现问题，暂时不稳定。需要优化。
