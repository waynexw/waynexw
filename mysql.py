# infos of mysql connection. --Pip3 install mysql_connector_python

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password123") 
print(mydb)

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password123")
mycursor=mydb.cursor()
mycursor.execute("create database harshdb")

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password123")
mycursor=mydb.cursor()
mycursor.execute("show databases")
for db in mycursor:
  print(db)
    
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password123",database="harshdb")
mycursor=mydb.cursor()
sqlformula = "Insert into employee(name,sal) values(%s,%s)"//'values has placeholders
employees = [("harshit",200000),("rahul", 30000),("avinash", 40000),("amit", 50000),]//Created an array of emplpoyees
mycursor.executemany(sqlformula, employees)//Passing the data
mydb.commit()//SQL statement used for saving the changes

db.close


# Decide to use json or MySQL database - wayneW.
with open("./routes/env_conf.json", 'r', encoding='utf-8') as ec:
    json_data = json.load(ec)
  # print(json_data)
DB_TYPE = json_data['DB_TYPE']
DB_NAME = json_data['DB_NAME']

print(DB_TYPE)
print(DB_NAME)

# BOOK_REQUESTS = json_data
   BOOK_REQUESTS = results
except:
   print ("Error: unable to fetch the data")

DB_TYPE = str(os.getenv('dbtype')) # use sys env viriables to set DB_TYPE

initializaed local database via creation a new database
DB_NAME = "abc"
DB_NAME = str(os.getenv('dbname'))   
if DB_NAME == "None":
    DB_NAME = "text_db"

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="www",  # please adjust the user name as same as the local MySQL's user name  -wayneW
  password="5566"  # change the password as you defined in your MySQL database  -wayneW
)

# set env viarables in config.ini to instead

if DB_TYPE == 'mysql':
  mydb = mysql.connector.connect(
  host = json_data['host'],
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
  # print (tmp[0], DB_NAME) note that print result is ['bl_book'] bl_book. But when add[] around DB_NAME, will see the result is ['bl_book'] ['bl_book'], so tmp[i] == [DB_NAME] go right.

  # while statement to check whether the pre-build database name exist in the mysql database lists.  
  i = 0
  while i < num:
    # if tmp[i] == "[" + "'" + DB_NAME + "'" + "]":
    if tmp[i] == [DB_NAME]:  # 启示 字符串数据自带引号
      db_exist = 'yes'
      break
    i = i + 1
  # print (db_exist)
