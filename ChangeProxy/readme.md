#代理IP


18.1[changeproxy.py](https://github.com/axianga/python/blob/master/ChangeProxy/changeproxy.py)                  （代理IP更换，爬虫必备）
(by axianga in 2018.11.20)   

    --scrapy爬虫框架,代理IP更换，此段功能放在middlewares.py中.
    --需要在settings.py中开启DOWNLOADER_MIDDLEWARES，将原middlewares.py的DOWNLOADER_MIDDLEWARES注释掉，用changeproxy取代。
    --代理ip需要购买，较为可靠，免费的IP效率低。
    
18.2[changeproxyR2.py](https://github.com/axianga/python/blob/master/ChangeProxy/changeproxyR2.py)                  （代理IP更换验证）
(by axianga in 2018.11.25)   

    --验证IP的可用与否，将可用的保存到txt。（可用，代码尚未优化）
