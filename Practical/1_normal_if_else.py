# normal if/else:- it executes the top most priority defined
n = int(input("Enter age: "))

if n>100:
    print("invalid age")

else:
    print("valid for vote")


# Practicals:-
# 1) To print 5 numbers from users, to print even & odd number,
# to find number of outcomes of even & odd numbers, add even & 
# odd total and add even & odd


ev=0
od=0
evsum=0
odsum=0
sum=0

# to find wether the number is even or odd
for j in range(1,6):
    n = int(input(f"Enter number{j}: "))
    if n%2==0:
        print(n,"is even")
        ev+=1
        evsum+=n

    else:
        print(n,"is odd")
        od+=1
        odsum+=n
    sum+=n

print("Total even: ",ev)
print("Total odd: ",od)
print("sum of even numbers: ",evsum)
print("sum of odd numbers: ",odsum)
print("Sum of even & odd is: ",sum)

#     or

ev=0
od=0
evsum=0
odsum=0

# taking 5 numbers from user
for i in range(1, 6):
    n = int(input(f"Enter number{i}: "))
    if n % 2 == 0:
        print(n, "is even")
        ev+= 1
        evsum+= n
    else:
        print(n, "is odd")
        od+= 1
        odsum+= n
# total outcomes of even & odd
print("Total even: ",evsum)
print("Total odd: ",odsum)
print("Count of odd: ",od)
print("Count of even:",ev)
print("Total even + odd: ",evsum+odsum)