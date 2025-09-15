# **************************METHOD OVERRIDING***************************
# EXAMPLE:-
# 1) For single inheritance:

class Myname:
    def myname(self):
        print("Hello1")

class Myname2(Myname):
    def myname(self):
        super().myname()            # method 
        print("Hello2")

obj = Myname2()
obj.myname()


# 2) For multiple inheritance:

class A:
    def fun1(self):
        super().fun1()
        print("Hello1")

class B:
    def fun1(self):
        print("Hello2")

class C(A,B):                   # also used as (B,A)
    def fun1(self):
        super().fun1()
        print("Hello3")

obj = C()
obj.fun1()