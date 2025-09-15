# ladder if else:- there are multiple if else which makes a ladder
n = int(input("Enter age: "))

if n>100:
    print("invalid age")

elif n>=18: #elif = else if
    print("valid for vote")

else:
    print("not valid for vote")


# Practicals:-
# 1):- to find even or odd number

n = int(input("Enter number: "))

if n==0:
    print("neither even or odd")

elif n%2==0:
    print("the entered number is even")

else:
    print("the entered number is odd")


# 2):- to find the number is +ve or -ve

n = int(input("Enter number: "))

if n==0:
    print("neither +ve nor -ve")

elif n>0:
    print("number is +ve")

else:
    print("number is -ve")