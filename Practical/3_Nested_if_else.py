# Nested if/else:- It has if/else inside if/else
# practicals:-

# 1) pracrical:- to find the greatest number entered by user or already given

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

# n1=1300 
# n2=1500 
# n3=800

if n1>n2:
    if n2>n3:
        print(n1,"is the greatest number")

    else:
        print(n3,"is the greatest number")

else:
    if n2>n3:
        print(n2,"is the greatest number")
    
    else:
        print(n3,"is the greatest number")