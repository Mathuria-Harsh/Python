import pymysql

mydb = pymysql.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists tkin")
mydb.commit()

mydb = pymysql.connect(host="localhost", user="root", passwd="", database="tkin")
mycursor = mydb.cursor()

mycursor.execute("""create table if not exists data (id int primary key auto_increment, 
                name varchar(100), 
                email varchar(40), 
                mobile varchar(10), 
                password varchar(255) NOT NULL, 
                cpassword varchar(255) NOT NULL, 
                gender ENUM('Male', 'Female', 'Other'),
                dob DATE,
                check_1 BOOLEAN,
                check_2 BOOLEAN)""")
mydb.commit()

print("Created")