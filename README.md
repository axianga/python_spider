# python爬虫学习系列  

**照着样本敲代码 + 先读懂代码 + 静下心慢慢来**

**requests/BeautifulSoup/re/os/traceback/urllib/scrapy/**

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

 -通过对抓包工具FIddler的使用，对js文件进行抓取评论URL地址，打开URL发现文字评论段是Unicode编码，也可以通过浏览器开发者模式看，在python中对UNICODe解读，证实是评论内容。页面关系也有相应的URL对应。
 
 
10.[qsbkscrapy1](https://github.com/axianga/python/blob/master/qsbkscrapy1)     (by axiang in 2018.11.6)

 -接触scrapy库，使用基础爬虫模板basic，爬取糗事百科的段子及相关网页。
 
 
11.[qsbkscrapy2](https://github.com/axianga/python/blob/master/qsbkscrapy2)     (by axiang in 2018.11.6)

 -接触scrapy库，使用基础爬虫模板crawl，爬取糗事百科的段子及相关网页。
 
 
12.[tszn1scrapy](https://github.com/axianga/python/blob/master/tszn1scrapy)     (by axiang in 2018.11.8)

 -接触scrapy库，使用基础爬虫模板basic,爬取天善智能课程信息，并保存到txt文件中。
 
