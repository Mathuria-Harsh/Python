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