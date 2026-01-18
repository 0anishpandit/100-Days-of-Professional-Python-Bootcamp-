# Nested if / elif / else

bill = 0
user_heights = int(input("Enter Your Height : "))
if user_heights > 120 :
    print("Can Ride")
    user_age = int(input("Enter Your Age : "))
    if user_age > 18  & user_age <45:
        print("$12")
        bill = 12
    if user_age > 12  & user_age <= 18 :
        print("$7")
        bill = 7
    if user_age <= 12 :
        print("$5")
        bill = 5
    if user_age >= 45 & user_age <=55:
        print("You have a free ride.")
    wants_photo = input("Do you want photo ? Type Y or N : ")
    if wants_photo == "y" :
        bills = bill + 3
        print(f"Your total bill is ${bills}")
    elif wants_photo == "n":
        print(f"Your final bill is ${bill}")


else :
    print("You Can't Ride")