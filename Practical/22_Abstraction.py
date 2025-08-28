from abc import ABC, abstractclassmethod

class Employer(ABC):
    # Abstract class

    def salary(self):
        pass
        # print("Harsh 1 got 20k")
        # print("Tannu 2 got 30k")

class Harsh(Employer):
    def salary(self):
        return 8000

class Tannu(Employer):
    def salary(self):
        return 10000

obj = Harsh()
print(obj.salary())

obj1 = Tannu()
print(obj1.salary())