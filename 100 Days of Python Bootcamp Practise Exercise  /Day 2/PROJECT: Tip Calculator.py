print("Welcome to the Tip Calculator !")
total_bill = int(input("What was your total bill ? "))
tip_amount = int(input("How much percentage tip would you like to give? 10 , 12 or 15 ? "))
split_bill = int(input("How many people toi split hte bills ? "))

individual_amount = (total_bill + (tip_amount/100 * total_bill)) / split_bill
print(f"Each Person should pay: ${individual_amount}")


