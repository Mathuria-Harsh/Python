# 1) print any random number between given the range

import random

n = random.randint(1,51)
print(n)


# 2) print any random number from given list

import random

l = [56,24,31,12]
print(random.choice(l))


# 3) generate otp

import random

otp = random.randint(1000,9999)
print("OTP is: ",otp)
user_otp = int(input("Enter OTP: "))

if otp==user_otp:
    print("Correct otp")

else:
    print("Invalid otp")