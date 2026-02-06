"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

The below code is for the game completation of the above link . This code might not work for this but thos woll work in the website.
This code just teach us how we create the function and use it.
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_cycle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for robot in range(6):
    one_cycle()


