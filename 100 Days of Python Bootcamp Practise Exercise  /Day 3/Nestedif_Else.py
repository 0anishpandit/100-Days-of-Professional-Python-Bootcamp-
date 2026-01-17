# Nested if / else

"""
SYNTAX :
If condition:
    if another condition :
        do this
    else :
        do this
else :
    do this

"""
#Nested If / else
user_height = int(input("Enter Your Height : "))
if user_height > 120 :
    print("Can Ride")
    user_age = int(input("Enter Your Age : "))
    if user_age > 18 :
        print("$12")
    if user_age <= 18 :
        print("$7")
else :
    print("You Can't Ride")

# Nested if / elif / else
user_heights = int(input("Enter Your Height : "))
if user_heights > 120 :
    print("Can Ride")
    user_age = int(input("Enter Your Age : "))
    if user_age > 18 :
        print("$12")
    elif user_age > 12  & user_age <= 18 :
        print("$7")
    elif user_age <= 12 :
        print("$5")
else :
    print("You Can't Ride")