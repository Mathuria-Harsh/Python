# To use random number
import random                                       

# chooses a random number between 1 and 50
original = random.randint(1,50)             
        
# This will run again and again until we break the loop
while True:                                         
    print("Enter number between 1 to 50 range")

 # Ask the user to guess the number
    choice = int(input("Enter choice: "))

# Check if the guess is not in the range (less than 1 or more than 50)
    if choice <1 or choice>50:
        print("Invalid choice")         # Wrong input
        break                           # exit the loop

# If the guess is correct
    elif choice==original:
        print("You win")                # Correct gues  
        break                           # Exit the loop

# If the original number is greater than your guess
    elif original>choice:
        print("Original number is greatest")

# If the original number is smaller than your guess
    else:
        print("Original number is smallest")