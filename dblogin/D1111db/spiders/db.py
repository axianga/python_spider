# -*- coding: utf-8 -*-
# 11.11号 豆瓣模拟登陆scrapy，basic爬虫模板，半自动登陆验证码
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request

class DbSpider(scrapy.Spider):
    name = "db"
    allowed_domains = ["douban.com"]
    #模拟浏览器
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    '''start_urls = ['http://www.douban.com/']'''

    #第一次爬取使用方法
    def start_requests(self):
        return [Request("https://accounts.douban.com/login",
                        callback = self.parse,
                        headers= self.header,
                        meta = {"cookiejar":1},)]     #1：开启

    def parse(self, response):    #parse回调函数
        url = "https://www.accounts.douban.com/login"    #豆瓣登录网址，post请求
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract() #获取验证码图片地址
        print(captcha)
        #判断有无验证码，即爬取的captcha是否存在
        if len(captcha) > 0:
            print("此时有验证码！")
            localpath ="c:/yzm.jpg"    #保存验证码图片
            urllib.request.urlretrieve(captcha[0],filename = localpath)
            print("请查看本地验证码图片并输入验证码：")
            captcha_value = input()
            data = {
                    "form_email":"513135258@qq.com",
                    "form_password":"*********",
                    "captcha-solution":captcha_value,
                    "redir":"https://www.douban.com/people/187186241/",
            }
        else:
            print("此时没有验证码。")
            data = {
                    "form_email":"513135258@qq.com",
                    "form_password":"*********",
                    "redir":"https://www.douban.com/people/187186241/"
            }
        print("登陆中···")
        return [FormRequest.from_response(response,
                                          meta ={"cookiejar":response.meta["cookiejar"]},
                                          headers = self.header,
                                          formdata = data,
                                          callback = self.next,
                                          dont_filter=True    #start_requests中的url域名不能与allowed-domains不一致，否则会被过滤掉，添加dont_filter=True停用过滤功能
                                          )]

    def next(self,response):
        print("此时已经登录完成，并爬取了个人中心的数据")
        title = response.xpath("/html/head/title/text()").extract()
        print(title)