# Examples
# 1) 

file = open("Test1","w")                    # new file created
file.write("Hello write method")
file.close

file = open("Test1","a")                    # updating existing file
file.write("\nThis is an append method")
file.close

# making it readable
file = open("Test1","r")
print(file.read())                          # we can also use .readline()
file.close()


# 2) to store integer value by converting it into string (str)

n = int(input("Enter number: "))

with open("Test2","a") as file:
    for i in range(1,n+1):
        file.write(str(i)+"\n")


# 3) To store data in dictionary

d = {}

for i in range(1,11):
    d[i] = i*i

file = open("Test3","w")
file.write(str(d))
file.close()


# 4) To store data in list

l = []

for i in range(1,11):
    l.append(i)

file = open("Test4","w")
file.write(str(l))
file.close()


# 5) w+ (write + read method)/ w+ function

file = open("Test5","w+")
file.write("w+ method")

print(file.tell())              # give position of pointer
file.seek(3)                    # moves the pointer to position 3 or start read
print(file.read())              # reads from position 3 to end
file.close()


# 6) r+ (first read then write (read + write method))/ r+ function


file = open("Test5","r+")
file.write("Updated data")
file.read()                     # or print(file.read())


# 7) a+ (append + read method)/ a+ function:- 

file = open("Test5","a+")
file.write("\nThis is a+ method")
file.seek(0)
file.read()                         # or print(file.read())
file.close() 