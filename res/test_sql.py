# Aim to precreat proper running environment at the client end via creat new database using MySQL, kindly note that the client may need to pre-install the MySQL before using this code. -wayneW
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


