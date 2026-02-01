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

options = [rock, paper, scissor]
computer_choice = random.choice(options)