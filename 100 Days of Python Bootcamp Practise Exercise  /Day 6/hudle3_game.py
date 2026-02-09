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

number_of_cycle = 0
while at_goal() == False :
    one_cycle()
    number_of_cycle += 1
    print(number_of_cycle)