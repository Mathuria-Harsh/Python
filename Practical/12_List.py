l = [7,"Harsh",True,2,1,"IR"]  # for string use ""

# methods

l.append(18)                    # it will add single value at the end of the list
print(l)

print(l.count(1))               # used to count the vlaues in list

l.extend([100,45,93])           # it will add multiple values at the end of the list
print(l)

print(l.index(100))             # to count the position of given value

l.insert(5,"Ms")                # it is used to add value at particular position in list
print(l)

l.pop(3)                        # it will remove value from list by      
print(l)                        # giving position number & by default last one

l.remove(1)                     # it will remove value by giving
print(l)                        # particular value


# **********Example*************

# 1) To add values is list & to sort from given list, find largest, second largest, & smallest number

l = [93,7,18,45]
l.sort()
print(l)

# to find largest,second largest & smallest number





# 2) to take list from user & sort it

n = int(input("Enter length of list: "))
l = []






# 3) Remove duplicate values from given list

l = [1,2,3,1,2]
l1=[]

for i in l:
    if i not in l1:
        l1.append(i)
    
print(l1)


# 4) to print only duplicate values

l = [1,2,3,1,2]
l1 = []
l2 = []

for i in l:
    if i not in l1:
        l1.append(i)
    
    else:
        l2.append(i)
    
print(l1)
print(l2)