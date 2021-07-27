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

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)
