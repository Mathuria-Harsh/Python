# a) Right angle pattern:
for i in range(1,6):
    for j in range(1,i+1):
        print(" *",end="")
    
    print()

#   or

for i in range(1,6):
    print("*",end="")

# b) left right angle pattern:
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")

    for j in range(1,i+1):
        print("*",end="")

    print()

#  or

for i in range(1,6):
    print(" "*(6-i),"*"*i)


# 3) Pyramid pattern:

for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(" *",end="")

    print()

#    or

for i in range(1,6):
    print(" "*(6-i)," *"*i)


# 4) right angle pattern (but in reverse)

for i in range(6,0,-1):
    for j in range(1,i+1):
        print(" *",end="")
    print()

#       or

for i in range(6,0,-1):
    print(" "*(6-i),"*"*i)


# 5) Left angle pattern (in reverse)

for i in range(5, 0, -1):
    # Print leading spaces
    for k in range(5 - i):     #k=use for space
        print(" ", end=" ")

    for j in range(i):       #j=use to print star
        print("*", end=" ")

    print()


# 6) reverse pyramid:

for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(" *",end="")

    print()


# 7) Diamond pyramid:

for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(" *",end="")

    print()

for i in range(5,0,-1):
    for k in range(5-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(" *",end="")

    print()

