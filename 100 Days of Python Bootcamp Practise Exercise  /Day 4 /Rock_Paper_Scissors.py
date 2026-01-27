import random

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

options = [rock , paper , scissor]
computer_choice = random.choice(options)

print("Type 'rock' for selecting Rock", rock)
print("Type 'paper' for selecting Paper", paper)
print("Type 'scissor' for selecting Scissor", scissor)
user_choice = input("Enter your choice: ")

