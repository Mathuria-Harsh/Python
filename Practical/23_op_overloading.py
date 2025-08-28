# ***************************OPERATOR OVERLOADING***********

# class User:
#     def __init__(self,a,b):
#         print("Constructor called")
#         self.a=a
#         self.b=b
    
#     def __str__(self):
#         # return "str called"
#         return f"{self.a},{self.b}"
    
#     def __add__(self,obj):
#         # print("Add called")

#         x = self.a+obj.a 
#         y = self.b+obj.b 

#         return x,y

# obj = User(10,20)
# print(obj)

# obj1 = User(30,40)
# print(obj1)

# print("Addition is: ",obj+obj1)


# Examples

# 1) Subtraction:-
# class Sub:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
    
#     def __str__(self):
#         return f"{self.a},{self.b}"
        
#     def __sub__(self,obj):
#         x = self.a-obj.a
#         y = self.b-obj.b

#         return x,y
    
# obj = Sub(30,20)
# print(obj)

# obj1 = Sub(10,10)
# print(obj1)

# print("Subtraction is: ",obj-obj1)


# 2) Multiplication:-

class Multi:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __str__(self):
        return f"{self.a},{self.b}"
        
    def __mul__(self,obj):
        x = self.a*obj.a
        y = self.b*obj.b

        return x,y
    
obj = Multi(2,4)
print(obj)

obj1 = Multi(5,2)
print(obj1)

print("Multiplication is: ",obj*obj1)