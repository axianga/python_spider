# 链接mongodb数据库，插入数据测试
import pymongo

MONGO_URL = "localhost"
MONGO_DB = "taobao"
MONGO_COLLECTION = "goodsinfo"
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
try: 
    for i in range(1,10):
        result = {str(i):str(i*i)}
        db[MONGO_COLLECTION].insert_one(result)
        print("保存第{}条数据成功".format(i))
        
except Exception as e:
    print(e)
