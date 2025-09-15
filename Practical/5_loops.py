# *********************While loop**************************

# 1) Take an number from the user to print numbers till given
# by using while loop

n = int(input("Enter the number: "))
i = 1

while(i<=n):
    print(i)
    i+=1


# # 2) Now reverse, from where the number is entered by user,
# # output should be in reverse order

i = int(input("Enter the number: "))

while(i>=1):
    print(i)
    i-=1

# 3) Summation of numbers:- get a number from user & add them.
n = int(input("Enter the number: "))
i=1
sum=0

while(i<=n):
    i=i+1
    sum=sum+i

print(sum)

#                           OR
n = int(input("Enter the number: "))
i=1
sum=0

while(i<=n):
    sum=sum+i
    i=i+1

print(sum)


# 4) Get a number from user & find it's factorial
n = int(input("Enter the number: "))
i=1
fac=1

while(i<=n):
    fac*=i
    i=i+1

print(fac)

# *********************For Loops***********************
# 5) to print number till entered from user
for i in range(1,11):
    print(i)

# or reverse operation

for i in range(10,0,-1):
    print(i)

# or taking number from user
n = int(input("Enter number: "))
for i in range(1,n):   #we can also use n+1 to get exact range entered by user
    print(i)

# or taking number from user but in reverse
n = int(input("Enter number: "))
for i in range(10,n-1,-1):     #we can also use n-1 to get exact range entered by user
    print(i)


# 6) to print even & odd number
n = int(input("Enter number: "))
for i in range(1,n):    #we can also use n+1
    if i%2==0:
        print(i,"even")

    else:
        print(i,"odd")