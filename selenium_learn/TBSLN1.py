# 12.12 selenium 浏览器测试抓取淘宝商品信息
from selenium import webdriver                                               # webdriver：驱动浏览器
from selenium.common.exceptions import TimeoutException                      # TimeoutException：超时异常
from selenium.webdriver.common.by import By                                  # By：选择器
from selenium.webdriver.support import expected_conditions as EC             # EC：配合WebDriverWait 赋予等待，具体执行命令
from selenium.webdriver.support.wait import WebDriverWait                    # WebDriverWait：最长等待时间，具体条件
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo

browser = webdriver.Chrome()                                                 # 选择Chrome浏览器
wait = WebDriverWait(browser,10)                                             # 等待最大时长10s
KEYWORD = '机械手表'                                                         # 输入关键字

def index_page(page):                                                        # 抓取索引页
    '''
    抓取索引页
    ：param page：页码
    '''
    print("正在爬取第{:}页".format(page))
    try:
        url = "https://s.taobao.com/search?q=" + quote(KEYWORD)             # url赋值，quote解码
        browser.get(url)                                                    # Chrome访问url
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))                # 获取页码输入框
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))       # 跳转页码确定按钮
            input.clear()                                                                # 清空输入框内容
            input.send_keys(page)                                                        # 发送页码到输入框中
            submit.click()                                                               # 点击跳转页码确定按钮
        wait.until(EC.text_to_be_prsent_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span')))                      # 通过高亮显示，判断跳转的页码是否为当前的页码
        wait.until(EC.presence_of_element_located((BY.CSS_SELECTOR,'.mainsrp-itemlist div.items .item')))                          # 查找页面商品信息
        get_products()                                                      # 执行prodccts函数，获得商品数据
    except TimeoutException:
        index_page(page)

def get_products():
    '''
    提取商品数据
    '''
    html = browser.page_source                                              # 获取网页源码
    doc = pq(html)                                                          # pyquery解析
    items = doc('#mainsrp-itemlist div.items .item').items()                # pyquery 的生成器items(),遍历灵活                                                        # 查找商品信息
    for item in items:                                                      # 遍历所有商品
        product = {                                                         # 本来items是以列表形式存储的，现在改为键值对，以词典存储。
                'image': item.find('.pic .img').attr('data-src'),
                'price': item.find('.price').text(),
                'deal': item.find('.deal-cnt').text(),
                'title': item.find('title').text(),
                'shop': item.find('.shop').text(),
                'location': item.find('.location').text()
        }
    print(product)
    save_to_mongo(product)                                                  # 保存到mongoDB数据库中


MONGO_URL = 'localhost'                                                     # mongoDB地址
MONGO_DB =  'taobao'                                                        # mongoDB 数据库名称
MONGO_COLLECTION = 'goodsinfo'                                               # mongoDB 数据库的表格
client = pymongo.MongoClient(MONGO_URL)                                     # 链接mongDB
db = client[MONGO_DB]

def save_to_mongo(result):                                                  # 保存到mongoDB 
    '''
    保存至MOngoDB
    ：param result：结果
    '''
    try:
        if db[MONGO_COLLECTION].insert(result):
            print("存储到MongoDB成功")
    except Exception:
        print("存储到MongoDB失败")

MAX_PAGE = 100
def main():
    '''
    遍历每一页
    '''
    for i in range(1,MAX_PAGE + 1):
        index_page(i)

if __name__ == '__main__':
    main()













