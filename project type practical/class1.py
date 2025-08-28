class Prime:
    def prime(self):
        n = int(input("Enter number: "))
        prime1=0

        for i in range(1,n+1):
            if n%i==0:
                prime1+=1
            
        if prime1 == 2:
                print(n, "is a prime number")
        else:
                print(n, "is not a prime number")

class Pattern:
    def pattern(self):
        for i in range(1,6):
            for j in range(1,i+1):
                print("*",end="")
        
            print()

class Table:
    def table(self):
        n = int(input("Enter number: "))

        for i in range(1,11):
            print(f"{n}*{i}={n*i}")

class Reverse:
    def rev(self,s):
        if len(s)%2==0:
            print(s)
        
        else:
            mid = len(s)//2
            return mid