# There are two concept for patterns:-
#      a) Row: It print row firstly
#      b) Column: After row, column is printed

# a) Right angle pattern:
for i in range(1,6):           # i = row
    for j in range(1,i+1):     # j = column
        print("*",end="")

    print()

#      or

# for i in range(1,6):
#     print("",end="")