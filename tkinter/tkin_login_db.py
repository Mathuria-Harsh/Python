import pymysql

mydb = pymysql.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists tkin")
mydb.commit()

mydb = pymysql.connect(host="localhost", user="root", passwd="", database="tkin")
mycursor = mydb.cursor()

mycursor.execute("""create table if not exists login (
                id int primary key auto_increment, 
                email varchar(40),
                password varchar(255) NOT NULL)""")
mydb.commit()

print("Created")