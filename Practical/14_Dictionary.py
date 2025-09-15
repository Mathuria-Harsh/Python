d = {1:"Hello", 2:"Harsh", 3:"Good morning"}
print(type(d))

# methods

print(d.get(1))                 # print values of given keys
print(d.keys())                 # print keys
print(d.values())               # print all values of all keys
print(d.items())                # print whole items keys as well as their values
d.update({4:"Ms Dhoni"})        # it will update the dictionary by giving keys 
print(d)

d.pop(2)                        # remove specific key & their value by giving number
print(d)

d.popitem()                     # remove whole dictionary


# to convert in list from tuple

t = {1,2,3}
t1 = []

print(d.fromkeys(t1))


# Examples

# 1) Write a Python program to create a dictionary where the keys are numbers from 1 to 30 and the values are the squares of the keys

d = {}
for i in range(1,31):
    d[i]=i*i
print(d)


# 2) Write a Python program to add the values of common keys in two dictionaries and store the result in a new dictionary.

d1 = {'p':1100, 'q':300, 'r':600}
d2 = {'p':400, 'q':200}
d3 = {}

for i,j in d1.items():              # i is key & j is value, so i='p', j=1100
    for k,l in d2.items():          # k is key & l is value, so k='p', l=400
        if i==k:                    # it means (i is key of d1)p==p(k is key of d2)
            d3[i]=j+l               # it will add values of j & l, means 1100+400

print(d3)


# 3) make key values pair from list & store the result in dictionary

l = [16,62,24]          # l is keys
l1 = [32,89,62]         # l1 is values
d = {}                  # result to be store in dictionary

for i in range(len(l)): # len(l) is index, it will work by starting from 0 to 2 means, 0->16, 1->62 & 2->24, so the length of list is 3.
    d[l[i]] = l1[i]     

print(d)