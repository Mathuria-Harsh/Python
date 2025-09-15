s = "Python Programming"

print(s.capitalize())           # capitalize first letter 
print(len(s))                   # give the lenght of string
print(s.count("m"))             # give number of repeative letters but is case sensitive
print(s.casefold())             # give whole string
print(s.upper())                # convert string into uppercase 
print(s.lower())                # convert string into lowercase
print(s.center(24,"*"))         # it will centered the string by giving position number & any design 
print(s.find("p",2))            # used to locate the first occurrence of a specified substring within a given string
print(s.index("y"))             # To locate the position of an element within a sequence
print(s.isalnum())              # Return True if the string is an alpha-numeric string, otherwise False
print(s.isalpha())              # Return True if the string is an alphabetic string, otherwise false.
print(s.replace("m","y"))       # Return a copy with all occurrences of substring old replaced by 
print(s.title())                # Return a version of the string where each word is titlecased.
print(s.swapcase())             # Convert uppercase characters to lowercase and lowercase characters to uppercase