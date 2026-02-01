import random
from doctest import script_from_examples

rock = '''
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

options = [rock, paper, scissor]
computer_choice = random.choice(options)
print("Type 'rock' for selecting Rock", rock)
print("Type 'paper' for selecting Paper", paper)
print("Type 'scissor' for selecting Scissor", scissor)
user_choice = input("Enter your choice: ")

if user_choice == "rock":
    user_choice = rock
elif user_choice == "paper":
    user_choice = paper
elif user_choice == "scissor":
    user_choice = scissor
else :
    print("Invalid Input !")

if user_choice == "invalid":
    print("Invalid Input!")
elif computer_choice == user_choice:
    print("It's a tie!")
elif (user_choice == rock and computer_choice == paper) or \
        (user_choice == paper and computer_choice == scissor) or \
        (user_choice == scissor and computer_choice == rock):
    print("User Choice",user_choice)
    print("Computer Choice :" ,computer_choice ," Computer wins!")
else:
    print("Computer Choice",computer_choice)
    print("Your Choice : ", user_choice , "You Won")