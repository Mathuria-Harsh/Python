import random

ac_no = random.randint(10000000001,99999999999)
password = random.randint(1001,9999)

class Bank:
    def ac_register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        mobile = int(input("Enter your mobile number: "))
        balance = 5000

        self.balance = balance
        self.name = name

        print("Your account number is: ",ac_no)
        print("Your passwor is: ",password)
    
    def deposit(self):
        damount = int(input("Enter deposit amount: "))
        print("Deposit amount is: ",damount)
        self.balance+=damount
    
    def withdraw(self):
        wamount = int(input("Enter your withdrwa amount: "))
        print("Your withdraw amount is: ",wamount)

        if wamount>self.balance:
            print("Insufficient amount")
        
        else:
            self.balance-= wamount
    
    def check_balance(self):
        print(f"{self.name} your account balance is: {self.balance}")

obj = Bank()
print("Press 1 for create account")
print("Press 2 for exit")

choice = int(input("Enter your choice: "))
if choice==1:
    obj.ac_register()

    while True:
        menu = """
            press 1 for deposit amount
            press 2 for withdraw amount
            press 3 for check balance
            press 4 for for exit
"""
        print(menu)
        choice1 = int(input("Enter choice: "))

        if choice1==1:
            obj.deposit()

        elif choice1==2:
            obj.withdraw()
        
        elif choice1==3:
            obj.check_balance()
        
        elif choice1==4:
            print("Thank you")
        
        else:
            print("Invalid choice")

else:
    print("Thank you")