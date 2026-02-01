import  random

letters = ['a','b','c','d','e','f','g','h','i','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols =['!','#','$','%','^','&','*','(',')','+']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n"))
number_numbers = int(input("How many numbers would you like?\n"))
number_symbols = int(input("How many symbol would you like?\n"))

# #Simple Random Password Generator
# password = ""
#
# for char in range(0,number_letters):
#     password += random.choice(letters)
#
# for char in range(0,number_numbers):
#     password += random.choice(numbers)
#
# for char in range(0,number_symbols):
#     password += random.choice(symbols)
#
# print("Your Random Password is: " , password)

#Hard one
password_list = []

for char in range(0,number_letters):
    password_list.append(random.choice(letters))

for char in range(0,number_numbers):
    password_list.append(random.choice(numbers))

for char in range(0,number_symbols):
    password_list.append(random.choice(symbols))


random.shuffle(password_list)

final_password = ""
for char in password_list:
    final_password += char
print("Your Random Password is: " , final_password)
