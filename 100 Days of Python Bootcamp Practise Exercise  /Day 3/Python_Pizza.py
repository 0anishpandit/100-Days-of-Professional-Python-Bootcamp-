print("Welcome to Python Pizza Deliveries !")
size = input("What size pizza do you want ? S , M or L: ")
pepperoni = input("Do you want the pepperoni on your pizza ? Y or N: ")
extra_cheese = input("Do you want extra cheese ? Y or N: ")

bill = 0
if size == "s" :
    bill = 15
if size == "m":
    bill = 20
if size == "l":
    bill = 25
else:
    print("Sorry you choose the wrong input.")

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
if extra_cheese == "y":
    bill += 1

    print(f"Your total bill is ${bill}")
else :
    print(f"Your total bill is ${bill}")