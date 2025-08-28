# *********************CLASS & OBJECTS************************

# Examples:-
# 1) Write a Python program using a class that contains 3 different methods & Create an object of the class and call all three methods.
class Myclass:                  # creation of class
    def fun1(self):             # method, "self" is key word used when object is created when there brackets is there, otherwise not
        l = [1,2,3,1,2]
        l1 = []

        for i in l:
            l1.append(i)
        
        print(l1)
    
    def fun2(self):
        d = {}

        for i in range(1,11):
            d[i] = i*i
        
        print(d)
    
    def fun3(self,a,b):
        print("Addition is: ",a+b)
    
obj = Myclass()             # creation of object
obj.fun1()
obj.fun2()
obj.fun3(10,20)             # using parameters & arguements