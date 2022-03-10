# pre-creat a proper running environment at client-end via creat new database by MySQL, kindly note that the client may need to pre-install the MySQL before using this code. -wayneW
# READ ME: before run app.py, you may help yourself adjust some codes in this file, including line 22, 23, 32 and 33 line as the detailed instruction below. -wayneW
# Some problem: after you run the app.py successfully, you may annotate line 19 to 60 as you have already created the database, or the app.py cannot run correctly. -wayneW

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="www",  # please edit the user name as local database user name  -wayneW
  password="5566"  # change the password as you defined in your local database  -wayneW
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydb")  # mydb is created to record the bookinfo. -wayneW

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="www",   # please edit the user name as local database user name  -wayneW
  password="5566",  # change the password as you defined in your local database  -wayneW
  database="mydb"   
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE `book_info` (\
  `uuid` varchar(45) NOT NULL,\
  `title` varchar(45) NOT NULL,\
  `email` varchar(40) NOT NULL,\
  `timestamp` varchar(30) NOT NULL,\
  PRIMARY KEY (`uuid`),\
  UNIQUE KEY `uuid_UNIQUE` (`uuid`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='for Swagger'")

sql = "INSERT INTO `book_info` (`uuid`, `title`, `email`, `timestamp`)\
 VALUES ('8c36e86c-13b9-4102-a44f-646015d4d981', 'Proceedings of Artworks', 'wayneW@196.com', '1626859035.678335');"
#  INSERT INTO `book`.`book_info` (`uuid`, `title`, `email`, `timestamp`)\
#  VALUES ('95cfcu04-acb2-99af-d8d2-7612fab56335', 'Sound of Music', 'foxtel@siinga.com', '1526866035.977766');"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

mydb.close() 

import uuid
import json  
import pymysql  # need to install pymysql first -wayne W 
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint

from validate_email import validate_email
REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

# define the database-link parameter. -wayne W
config = {
"host":"127.0.0.1", # 地址
"port":3306, # 端口
"user":"www", # 用户名
"password":"5566", # 密码
"database":"book", # 数据库名;如果通过Python操作MySQL,要指定需要操作的数据库
"charset":"utf8"
}

# 引入 virables then set the names of databases:

import os
import uuid
import json  
import pymysql  # need to install pymysql first -wayne W
import mysql.connector 
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint

from validate_email import validate_email
REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

# initializaed local database via creation a new database

# DB_NAME = "abc"
DB_NAME = str(os.getenv('dbname1'))
if DB_NAME == "None":
    DB_NAME = "mydb"

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="www",  # please adjust the user name as same as the local MySQL's user name  -wayneW
  password="5566"  # change the password as you defined in your MySQL database  -wayneW
)

mycursor = mydb.cursor()
# 可以加一条判断 如果数据库已经存在 则跳过此步骤
mycursor.execute("CREATE DATABASE " + DB_NAME)  # mydb is created to record the bookinfo. -wayneW

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="www",   # please adjust the user name as same as local database user name  -wayneW
  password="5566",  # change the password as you defined in your local database  -wayneW
  database=DB_NAME  
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE `book_info` (\
  `uuid` varchar(45) NOT NULL,\
  `title` varchar(45) NOT NULL,\
  `email` varchar(40) NOT NULL,\
  `timestamp` varchar(30) NOT NULL,\
  PRIMARY KEY (`uuid`),\
  UNIQUE KEY `uuid_UNIQUE` (`uuid`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='for Swagger'")

sql = "INSERT INTO `book_info` (`uuid`, `title`, `email`, `timestamp`)\
 VALUES ('8c36e86c-13b9-4102-a44f-646015d4d981', 'Proceedings of Artworks', 'wayneW@196.com', '1626859035.678335');"
#  INSERT INTO `book`.`book_info` (`uuid`, `title`, `email`, `timestamp`)\
#  VALUES ('95cfcu04-acb2-99af-d8d2-7612fab56335', 'Sound of Music', 'foxtel@siinga.com', '1526866035.977766');"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

mydb.close() 


"""The Endpoints to manage the BOOK_REQUESTS"""
# READ ME: before run app.py, kindly ensure that your client has already installed the MySQL database (like mysql-installer-web-community editoin) properly, and you have done with the initialization process.\ 
# Pre-setting the Environment Variables in line 27: str(os.getenv('dbname'), before you run the app.py successfully,  -wayneW
# In CMD, tap 'set dbname = bl-book ( database's name is up to U)', or if this variable is not worked. You'd better setting system env variables.
# When you want to set a system env viriables please goto 'windows setting'->'about'->'senior setting'->'Env Viriables', and built a new sys variables, for instance. let dbname=bl-book-
# -Then you can check this system env variables using statement in Admin CMD like 'echo %dbname%'. If the check is OK, the program will be functionaly released.
# If sys env variable is OK, but program yet isn't work, then try to restart VS Code, thus it should work correctly.
# I notice that mysql database are not sensitive to case, so I set dbname = BL_book, but in fact the data name was set to bl_book.
import os
import uuid
import json  
import pymysql  # need to install pymysql first -wayne W
import mysql.connector 
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint
from validate_email import validate_email

REQUEST_API = Blueprint('request_api', __name__)

def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

# Decide to use json or MySQL database - wayneW.
with open("./routes/env_conf.json", 'r', encoding='utf-8') as ec:
    json_data = json.load(ec)
  # print(json_data)
DB_TYPE = json_data['DB_TYPE']
DB_NAME = json_data['DB_NAME']

# print(DB_TYPE)
#   print(DB_NAME)

# # BOOK_REQUESTS = json_data
#    BOOK_REQUESTS = results
# except:
#    print ("Error: unable to fetch the data")

# DB_TYPE = str(os.getenv('dbtype')) # use sys env viriables to set DB_TYPE

# initializaed local database via creation a new database
# DB_NAME = "abc"
# DB_NAME = str(os.getenv('dbname'))   
# if DB_NAME == "None":
#     DB_NAME = "text_db"

# mydb = mysql.connector.connect(
#   host="127.0.0.1",
#   user="www",  # please adjust the user name as same as the local MySQL's user name  -wayneW
#   password="5566"  # change the password as you defined in your MySQL database  -wayneW
# )

if DB_TYPE == 'mysql':
  mydb = mysql.connector.connect(
  host = str(json_data['host']),
  port = str(json_data['port']),
  user = str(json_data['user']), 
  password = str(json_data['password']),
  charset = str(json_data['charset'])
  )

  mycursor = mydb.cursor()
  sql = "show databases;"  # get the mysql database list.
  mycursor.execute(sql)
  results = mycursor.fetchall()
  db_exist = 'no'    # set a variable to save the status of whether the pre-build database exist.
  num = len(results)
  tmp = json.dumps(results)
  tmp = json.loads(tmp)   # format the batabase lists.
  # print (tmp[0], DB_NAME)  # print result is ['bl_book'] bl_book. But when add[] around DB_NAME, will see the result is ['bl_book'] ['bl_book'], so tmp[i] == [DB_NAME] go right.

  # while statement to check whether the pre-build database name exist in the mysql database lists.  
  i = 0
  while i < num:
    # if tmp[i] == "[" + "'" + DB_NAME + "'" + "]":
    if tmp[i] == [DB_NAME]:  # 启示 字符串数据自带引号
      db_exist = 'yes'
      break
    i = i + 1
  # print (db_exist)
  if db_exist == 'yes':  
    print(mycursor.rowcount, "The database exists already.") # qqq Acertain the exist of the database. -wayneW
    
  else:
    mycursor.execute("CREATE DATABASE " + DB_NAME)  # Database named DB_NAME is created to record the bookinfo. -wayneW

    # mydb = mysql.connector.connect(
    #  host="127.0.0.1",
    #  user="www",   # please adjust the user name as same as local database user name  -wayneW
    #  password="5566",  # change the password as you defined in your local database  -wayneW
    #  database=DB_NAME  
    # )
    mydb = mysql.connector.connect(
    host = str(json_data['host']),
    port = str(json_data['port']),
    user = str(json_data['user']), 
    password = str(json_data['password']),
    charset = str(json_data['charset']),
    database = DB_NAME
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE `book_info` (\
    `uuid` varchar(45) NOT NULL,\
    `title` varchar(45) NOT NULL,\
    `email` varchar(40) NOT NULL,\
    `timestamp` varchar(30) NOT NULL,\
    PRIMARY KEY (`uuid`),\
    UNIQUE KEY `uuid_UNIQUE` (`uuid`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='for Swagger'")

    sql = "INSERT INTO `book_info` (`uuid`, `title`, `email`, `timestamp`)\
    VALUES ('8c36e86c-13b9-4102-a44f-646015d4d981', 'Proceedings of Artworks', 'wayneW@196.com', '1626859035.678335');"
    #  INSERT INTO `book`.`book_info` (`uuid`, `title`, `email`, `timestamp`)\
    #  VALUES ('95cfcu04-acb2-99af-d8d2-7612fab56335', 'Sound of Music', 'foxtel@siinga.com', '1526866035.977766');"

    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mydb.close() 

# define the database-link parameter. -wayne W


else:
  # # get the data from local json file. -wayne W
  with open("./routes/j_data.json", 'r', encoding='utf-8') as f:
    json_data = json.load(f)
    # print(json_data)
    BOOK_REQUESTS = json_data
    f.close
  #except:
  if json_data == '':
    print ("Error: unable to fetch the data")

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
# # 关闭数据库连接
# finally:
# #cursor.close()
# #conn.close()
#    db.close()


@REQUEST_API.route('/request', methods=['GET'])
def get_records():
    """Return all book requests
    @return: 200: an array of all known BOOK_REQUESTS as a \
    flask/response object with application/json mimetype.
    """
    # print ("begin")  # How to debug in a smart way.
    # a = os.getenv('ENV_WINDIR')
    # b = os.environ.get('WINDIR')
    # c = os.environ('ENV_PORT')
    # d = os.getenv('windir')
    # print (a)
    # print (b)
    # print (c)
    # print (d)
    # print ("end")
    if DB_TYPE == 'mysql':
        config = {
        "host":str(json_data['host']), 
        "port":json_data['port'], 
        "user":str(json_data['user']), 
        "password":str(json_data['password']), 
        "database":str(json_data['DB_NAME']),
        "charset":str(json_data['charset'])
        }
        db = pymysql.connect(**config)
        cursor = db.cursor()
        sql = "SELECT * FROM book_info;"
        try:
          cursor.execute(sql)
          results = cursor.fetchall()
          BOOK_REQUESTS = results
        
        finally:
          return jsonify(BOOK_REQUESTS)
          db.close()
    
    else:
        with open("./routes/j_data.json", 'r', encoding='utf-8') as f:
          json_data = json.load(f)
        # print(json_data)
          BOOK_REQUESTS = json_data
          return jsonify(BOOK_REQUESTS)
          f.close
