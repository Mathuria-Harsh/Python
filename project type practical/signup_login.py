import random
otp = random.randint(1001,9999)
d = {}

while True:
    menu = """
        press 1 for Signup
        press 2 for login
        press 3 for forgot password
        press 4 for exit
    """

    print(menu)
    choice = int(input("Enter your choice: "))

    
    if choice==1:
        print("*****Signup*****")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        mobile = int(input("Enter your Mobile number: "))
        password = int(input("Enter password: "))
        cpassword = int(input("Enter confirm password: "))

        if password==cpassword:             # by using LIST
            d['email'] = email
            d['mobile'] = mobile
            d['password'] = password

            print("Signup Successful")
        else:
            print("Password & confirm password doesn't match")
    
    
    elif choice==2:
        print("*****Login*****")
        email = input("Enter email: ")
        password = int(input("Enter password: "))

        if d['email']==email:
            if d['password']==password:
                print("Login Successful")
            else:
                print("Password or Email doesn't match")
        else:
            print("Email doesn't match")
    
    
    elif choice==3:
        print("*****Forgot password*****")
        mobile = int(input("Enter mobile number: "))

        if d['mobile'] == mobile:
            print("Your OTP is: ",otp)

            uotp = int(input("Enter OTP: "))        # user otp
            if otp == uotp:
                password = int(input("Enter "))
            
                d['password'] = password                # it will override the previous password
                print("Password changed successfully")

            else:
                print("Incorrect OTP")
        
        else:
            print("Mobile number doesn't match")


    elif choice==4:
        print("Thank you")
        break