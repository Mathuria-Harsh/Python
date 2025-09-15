# 1) 

for i in range(1,11):
    if i==6:
        break
    print(i)

#  or 

for i in range(1,11):
    print(i)
    if i==5:
        break

# 2) 

for i in range(1,11):
    if i==6:
        continue
    print(i)