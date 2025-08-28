# by using third variable
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# a = 30 b = 20
# a = 20 b = 30

temp = a #temp = 10 a = blank
a = b #a = 20 b = blank
b = temp #b = 30 temp = blank, the value of third value did not get blank, it override

print("After swapping value of A: ",a)
print("After swapping value of B: ",b)

#by using only two variable
a = 30
b = 20

a = a+b #30+20=50=a
b = a-b #50-20=30=b
a = a-b #50-30=20=a value got override

print("After swapping value of A: ",a)
print("After swapping value of B: ",b)

#by using another method
a = 30
b = 20

a,b = b,a 
print("After swapping value of A: ",a)
print("After swapping value of B: ",b)