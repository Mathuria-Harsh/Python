
# B) ***************User defined******************

# a) Function without parameters and without return type.
import math

def tannu():        #function definition
    for i in range(1,6):
        print("*"*i)
    
# or

def fac():           #function definition
    n = int(input("Enter number: "))
    print(math.factorial(n))

#  or 
def factoria():      #function definition
    n = int(input("Enter number: "))
    i=1
    fact=1
    while(i<=n):
        fact*=i
        i+=1

    print(fact)

tannu()        #function call
fac()          #function call
factoria()     #function call

# b) Function with parameters & without return type.

def prime(n):    #parameters
    prime=0
    for i in range(1,n+1):
        if n%1==0:
            prime+=1

    if prime==2:
        print("number is prime")

    else:
        print("number is not prime")

def add(a,b):
    print("addition is:",a+b)

prime(2)     #arguements
add(50,50)   #arguements

            #  or from user

n = int(input("Enter number: "))

prime(n)
add(10,12)

# c) Function without parameters & with return type

def fun3():
    n = int(input("Enter number: "))
    fac=1

    for i in range(1,n+1):
        fac*=i
    
    return fac

result=fun3()
print(result)

print(fun3())

# d) function with parameters & with return type.

def check(number):
    if number%2==0:
        return "even"
    else:
        return "odd"

# taking from user
num = int(input("Enter number: "))

# function call and store the result
result = check(num)

# print result
print("number is: ",result)