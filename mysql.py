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
