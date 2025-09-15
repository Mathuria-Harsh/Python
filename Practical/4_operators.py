# Practicals:-
# 1) To find the greatest number by using operators

# a) and operators

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

# n1=1300 
# n2=1500 
# n3=800

if n1>n2 and n1>n3:
    print(n1,"is the greatest number")

elif n2>n1 and n2>n3:
    print(n2,"is the greatest number")

else:
    print(n3,"is the greatest number")

# b) or operators

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

# n1=1300 
# n2=1500 
# n3=800

if n1>n2 or n1>n3:
    print(n1,"is the greatest number")

elif n2>n1 or n2>n3:
    print(n2,"is the greatest number")

else:
    print(n3,"is the greatest number")