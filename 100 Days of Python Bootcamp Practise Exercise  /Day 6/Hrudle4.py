# Self-Made Logic

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump_wall()
    else:
        move()



# Anglena Yu
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump_wall()

    else:
        move()
