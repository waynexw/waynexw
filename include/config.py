# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTO_REPLY_CONTENT = """

# # obtain the config data from local json files. -wayneW
# # with open("./routes/data1.json", 'r', encoding='utf-8') as f:
# # 打开数据库连接
# db = pymysql.connect(**config)
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
# # SQL 查询语句
# sql = "SELECT * FROM book_info;"
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()

# # json_data = json.load(f)
# # print(json_data)
# # BOOK_REQUESTS = json_data
#    BOOK_REQUESTS = results
# except:
#    print ("Error: unable to fetch the data")
 
# 关闭数据库connection
finally:
 #cursor.close()
 #conn.close()
db.close()
