user_weight = int(input("Enter Your Weight : "))
user_height = float(input("Enter Your Height : "))

bmi = user_weight / (user_height ** 2)
if bmi < 18.5 :
    print("UnderWeight")
elif bmi < 25 :
    print("Normal Weight")
else :
    print("Overweight")
