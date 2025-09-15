t = (1,2,"Hello","Harsh",1,True)
print(type(t))
print(t.count(1))
print(t.index(2))

# to convert in list from tuple
l1 = list(t)
print(l1)

# to update list
l1.append(100)
print(l1)

# to convert in tuple from list after updating
t1 = tuple(l1)
print(t1)