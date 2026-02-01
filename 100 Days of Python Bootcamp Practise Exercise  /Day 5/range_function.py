"""
    #range()  :
    SYNTAX: for number in range(a,b):  // a= inclusive , b=  exclusive
    print(number)

"""

for number in range(0,10):
    print(number)

add_range_number = 0
for numbers in range(1,101):
    add_range_number += numbers
print(add_range_number)