# 1) SINGLE INHERITANCE

class A:
    def fun1(self):                                 # Method-1
        n = int(input("Enter the number: "))
        i = 1

        while(i<=n):
            print(i)
            i+=1
    
    def fun2(self):                                 # Method-2
        n = int(input("Enter number: "))

        if n<0:
            print("Enter +ve number")

        else:
            if n==1 or n==2 or n==3:
                print("Already prime number")

            else:
                prime=0
                for i in range(1,n+1):
                    if n%i==0:
                        prime+=1
                
                if prime==2:
                    print(n,"is the prime number")
                
                else:
                    print(n,"is not the prime number")

class B(A):
    def fun3(self):                                 # Method-3
        for i in range(1,6):
            for j in range(1,i+1):
                print(" *",end="")
            
            print()

obj = B()
obj.fun1()
obj.fun2()
obj.fun3()


# 2) MULTILEVEL INHERITANCE

class A:
    def add(self):
        n1 = int(input("Enter number1: "))
        n2 = int(input("Enter number2: "))

        print("Addition of n1 & n2 is: ",n1+n2)
    
class B(A):
    def sub(self):
        n1 = int(input("Enter number1: "))
        n2 = int(input("Enter number2: "))

        print("Subtraction of n1 & n2 is: ",n1-n2)

class C(B):
    def division(self):
        n1 = int(input("Enter number1: "))
        n2 = int(input("Enter number2: "))

        print("Division of n1 & n2 is: ",n1/n2)

obj = C()
obj.add()
obj.sub()
obj.division()


# 3) MULTIPLE INHERITANCE

class Myclass1:
    def fun1(self):
        import random

        n = random.randint(1,11)
        print(n)

class Myclass2:
    def fun2(self):
        d = {}
        for i in range(1,11):
            d[i]=i*i
        print(d)

class Myclass3(Myclass1,Myclass2):
    def fun3(self):
        s = "Python Programming"

# +ve climb

        print(len(s))
        print(s[0:6:1])
        print(s[2:10:1])
        print(s[2::1])

obj = Myclass3()
obj.fun1()
obj.fun2()
obj.fun3()


# 4) HIERARCHICAL INHERITANCE

class A:
    def fun1(self):                     # if/else
        n = int(input("Enter age: "))

        if n>100:
            print("invalid age")

        else:
            print("valid for vote")

class B(A):
    def fun2(self):                     # ladder if/else
        n = int(input("Enter age: "))

        if n>100:
            print("invalid age")

        elif n>=18: #elif = else if
            print("valid for vote")

        else:
            print("not valid for vote")

class C(A):
    def fun3(self):                     # nested if/else
        n1 = int(input("Enter number1: "))
        n2 = int(input("Enter number2: "))
        n3 = int(input("Enter number3: "))

        if n1>n2:
            if n2>n3:
                print(n1,"is the greatest number")

            else:
                print(n3,"is the greatest number")

        else:
            if n2>n3:
                print(n2,"is the greatest number")
            
            else:
                print(n3,"is the greatest number")

obj1 = B()
obj2 = C()

obj1.fun1()     # From class A
obj1.fun2()     # From class B

obj2.fun1()     # From class A
obj2.fun3()     # From class C


# 5) HYBRID INHERITANCE

class A:
    def fun1(self):
        for i in range(1,11):
            print(i)
            if i==5:
                break
            
class B(A):
    def fun2(self):
        for i in range(1,11):
            if i==6:
                continue
            print(i)
    
class C():                  # because c doesn't have any parent class
    def fun3(self):
        for i in range(1,11):
            if i==6:
                break
            print(i)


class D(B,C):
    def fun4(self):
        for i in range(1,6):
            for k in range(1,6-i):
                print(" ",end="")

            for j in range(1,i+1):
                print("*",end="")

            print()

obj = D()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()