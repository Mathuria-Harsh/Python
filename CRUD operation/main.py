from crud_operation import *

mydb = pymysql.connect(host="localhost", user="root", passwd="", database="signup")
mycursor = mydb.cursor()

while True:
    menu = """
            Press 1 for Insert data
            Press 2 for Update data
            Press 3 for Delete data
            Press 4 for Fetch data
            Press 5 for Exit
        """

    print(menu)
    choice = int(input("Enter choice: "))

    if choice==1:
        name = input("Enter name: ")
        subject = input("Enter subject: ")

        query = "insert into data (name, subject) values('%s', '%s')"
        args = (name, subject)

        mycursor.execute(query % args)
        mydb.commit()                       # means save
        print("Data inserted")

    elif choice==2:
        id = int(input("Enter ID: "))
        name = input("Enter name: ")
        subject = input("Enter subject: ")

        query = "update data set name='%s',subject='%s' where id='%s'"
        args = (name,subject,id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data updated")
    
    elif choice==3:
        id = int(input("Enter ID: "))

        query = "delete from data where id='%s'"
        args = (id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data deleted")
    
    elif choice==4:
        # id = int(input("Enter ID: "))         # to fetch only one data by entering ID
        query = "select * from data"

        mycursor.execute(query)

        # mydata = mycursor.fetchone()          # to fetch only one data by ID
        mydata = mycursor.fetchall()            # to fectch all data we have to first make an variable then an method
        print(mydata)
    
    elif choice==5:
        print("Thank you")
        break
    
    else:
        print("Invalid choice")
        break