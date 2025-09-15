# To press a number from menu entered by user to print particular result.
# 1) Prime number
# 2) Pyramid
# 3) Factorial
# 4) exit

while True:
    menu = """
    Press 1 for prime number
    Press 2 for pyramid
    Press 3 for factorial
    Press 4 for exit
"""

    print(menu)
    choice = int(input("Enter your choice: "))

# prime number
    if choice==1:
        n = int(input("Enter number: "))

        if n<0:
            print("Enter +ve number")

        else:
            if n==1 or n==2 or n==3:
                print("Already prime number")

            else:
                prime=0
                for i in range(1,n+1):
                    if n%i==0:
                        prime+=1
                
                if prime==2:
                    print(n,"is the prime number")
                
                else:
                    print(n,"is not the prime number")

# pyramid
    elif choice==2:
        k = int(input("Enter number of length pyramid: "))
        for i in range(1,k+1):
            for j in range(1,i+1):
                print(" *",end="")
            
            print()

# factorial
    elif choice==3:
        n = int(input("Enter number: "))
        i=1
        fac=1

        while(i<=n):
            fac*=i
            i+=1
        
        print(fac)

# exit
    elif choice==4:
        print("Thank you")
        break

    else:
        print("Invalid choice")
        break