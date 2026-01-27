import random

friends = ["Alice" , "Bob" , "Charlie" , "David" , "Emma"]
#option 1
bill_payer = random.choice(friends)
print(bill_payer)

#option 2
random_index = random.randint(0,4)
print(friends[random_index])