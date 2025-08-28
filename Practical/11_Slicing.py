s = "Python Programming"

# +ve climb

print(len(s))
print(s[0:6:1])
print(s[2:10:1])
print(s[2::1])

# Examples:

# 1) for +ve climb
s = "Python is programming language"

# +ve climb
print(s[5:16:2])
print(s[:18:3])
print(s[5::4])    #ending is not given
print(s[6:14:2])
print(s[16:28:3])


# 2) for -ve climb by using -ve slicing 
s = "Python is programming language"

print(s[-29:-6:3])
print(s[-20:-3:1])
print(s[::-1])
print(s[:-6:3])
print(s[-18::4])


# 3) to find the palindrome string by using slicing

s = input("Enter name: ")
rev = s[::-1]

if s==rev:
    print("Palindrome")

else:
    print("not palindrome")


# 4) to find 3 middle character from string (it is only applicable for odd not for even)

s = input("Enter string: ")

if len(s)%2==0:
    print(s)

else:
    mid = len(s)//2   #<-| it will take mid from here
#                        | 
#                        | 
#                        |
    print(s[mid-1] + s[mid] + s[mid+1])
#    left slicing               right slicing 