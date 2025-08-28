# *****************************ADVANCE PYTHON***************************

# Examples
# 1) Value error

try:
    n = int(input("Enter number: "))
    print(n)

    if n>0:
        print("+ve number")
    
except ValueError as e:                     # e is used for storing errorin variable
    print(e)

else:
    print("Try block is executed")
    print("Else block is executed")

finally:
    print("Finally block is executed")


# 2) Zero division error

n1 = int(input("Enter number: "))

try:
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))

    print("Division is: ",n1/n2)

except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)



# 3) Index error

try:
    l1 = [7,18,45,93]
    n = int(input("Enter index: "))

    print("Value of index is: ",l1[n])

except ValueError as e:
    print(e)

except IndexError as e:
    print(e)


# 4) For all type of error

try:
    l1 = [8,12,78,32,21]
    n = int(input("Enter index: "))
    d = int(input("Enter division number: "))

    print("Value of index is: ",l1[n])
    print("Division result is: ",l1[n]/d)

except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

except IndexError as e:
    print(e)