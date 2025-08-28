from tkinter import *
from tkcalendar import DateEntry
from tkin_login import *
from tkinter import messagebox
import pymysql


# Insert data function
def insert_data():
    name = ename.get()
    email = eemail.get()
    mobile = emobile.get()
    passwrord = epassword.get()
    cpasswrord = ecpassword.get()
    gender = gender_var.get()
    DOB_label = dob.get_date()
    check1 = check_1.get()
    check2 = check_2.get()

    try:
        mydb = pymysql.connect(host="localhost", user="root", passwd="", database="tkin")
        mycursor = mydb.cursor()

        query = "insert into data (name, email, mobile, password, cpassword, gender, dob, check_1, check_2) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        args = (name, email, mobile, passwrord, cpasswrord, gender, dob, check1, check2)
        mycursor.execute(query, args)
        mydb.commit()
        print("Data Inserted")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Update data function
def update_data():
    name = ename.get()
    email = eemail.get()
    mobile = emobile.get()
    passwrord = epassword.get()
    cpasswrord = ecpassword.get()
    gender = gender_var.get()
    DOB_label = dob.get_date()
    check1 = check_1.get()
    check2 = check_2.get()

    if mobile == "":
        messagebox.showwarning("Enter mobile number to update")
        return

    try:
        mydb = pymysql.connect(host="localhost", user="root", passwd="", database="tkin")
        mycursor = mydb.cursor()

        query = """
            UPDATE data 
            SET name=%s, email=%s, password=%s, cpassword=%s, gender=%s, dob=%s, check_1=%s, check_2=%s
            WHERE mobile=%s
            """
        args = (name, email, passwrord, cpasswrord, gender, DOB_label, check1, check2, mobile)
        mycursor.execute(query, args)
        mydb.commit()
        
        if mycursor.rowcount==0:
            messagebox.showinfo("Sorry, no record found")
        else:
            messagebox.showinfo("Data updated")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Delete data function
def delete_data():
    mobile = emobile.get()

    if mobile=="":
        messagebox.showerror("Enter mobile number to delete: ")
        return

    try:
        mydb = pymysql.connect(host="localhost", user="root", passwd="", database="tkin")
        mycursor = mydb.cursor()

        query = "delete from data where mobile=%s"
        mycursor.execute(query, (mobile,))
        mydb.commit()

        if mycursor.rowcount>0:
            messagebox.showinfo("Data deleted")
        
        else:
            messagebox.showinfo("Sorry, no record found")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = Tk()

root.geometry("500x500")
root.title("Signup form")


name = Label(root, text="Enter name:", font=("Arial",12,"bold"))
name.place(x=50,y=50)

email = Label(root, text="Enter email:", font=("Arial",12,"bold"))
email.place(x=50,y=100)

mobile = Label(root, text="Enter mobile:", font=("Arial",12,"bold"))
mobile.place(x=50,y=150)

passwrord = Label(root, text="Enter password:", font=("Arial",12,"bold"))
passwrord.place(x=50,y=200)

cpasswrord = Label(root, text="Enter cpassword:", font=("Arial",12,"bold"))
cpasswrord.place(x=50,y=250)

gender = Label(root, text="Select Gender:", font=("Arial",12,"bold"))
gender.place(x=50,y=300)


# for making box/Entries field
ename = Entry(root, bg="yellow")
ename.place(x=240,y=60)

eemail = Entry(root, bg="yellow")
eemail.place(x=240,y=110)

emobile = Entry(root, bg="yellow")
emobile.place(x=240,y=160)

epassword = Entry(root, bg="yellow")
epassword.place(x=240,y=210)

ecpassword = Entry(root, bg="yellow")
ecpassword.place(x=240,y=260)


# Radio buttons
gender_var = StringVar(value="None")                # selected gender is store

male = Radiobutton(root, text="Male", variable=gender_var, value="Male", font=("Arial",12,"bold"), fg="blue")
male.place(x=240,y=300)

female = Radiobutton(root, text="Female", variable=gender_var, value="Female", font=("Arial",12,"bold"), fg="blue")
female.place(x=300,y=300)

other = Radiobutton(root, text="Other", variable=gender_var, value="Other", font=("Arial",12,"bold"), fg="blue")
other.place(x=380,y=300)


# Checkboxes
check_1 = IntVar()              # to store it's state
check_2 = IntVar()              # to store it's state

check1 = Checkbutton(root, text="Given Credentials are true", variable=check_1, font=("Arial",12,"bold"), fg="green")
check1.place(x=50,y=340)

check2 = Checkbutton(root, text="I accept terms & conditions", variable=check_2, font=("Arial",12,"bold"), fg="green")
check2.place(x=50,y=370)


# Date pickup
DOB_label = Label(root, text="Select DOB: ", font=("Arial",12,"bold"))
DOB_label.place(x=50,y=410)

dob = DateEntry(root, width=18, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy", font=("Arial",12,"bold"))
dob.place(x=200,y=410)


# for making buttons
insert = Button(root, text="Insert", font=("Arial",16,"italic"), fg="red", command=insert_data)
insert.place(x=50,y=460)

update = Button(root, text="Update", font=("Arial",16,"italic"), fg="red", command=update_data)
update.place(x=140,y=460)

delete = Button(root, text="Delete", font=("Arial",16,"italic"), fg="red", command=delete_data)
delete.place(x=240,y=460)

login = Button(root, text="Login", font=("Arial",16,"italic"), fg="red", command=login_screen)
login.place(x=330,y=460)


root.mainloop()