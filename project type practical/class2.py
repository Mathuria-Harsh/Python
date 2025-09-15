from class1 import *

obj1 = Prime()
obj2 = Pattern()
obj3 = Table()
obj4 = Reverse()

while True:
    menu = """
        press 1 for prime number
        press 2 for Pattern
        press 3 for Table
        press 4 for Reverse
        press 5 for Exit
"""

    print(menu)

    choice = int(input("Enter your choice: "))

    if choice==1:
        obj1.prime()
    
    elif choice==2:
        obj2.pattern()
    
    elif choice==3:
        obj3.table()
    
    elif choice==4:
        s = input("Enter name: ")
        print(obj4.rev(s))
    
    elif choice==5:
        print("Thank you")
        break
    
    else:
        print("Invalid choice")
        break