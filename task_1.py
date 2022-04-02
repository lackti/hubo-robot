from cs1robots import *
load_world("worlds/harvest3.wld")
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    # function to turn right
    for _ in range(3):
        hubo.turn_left()

def move_and_pick():
    # function to move and pick in the same time
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()

def turn_right_to_left():
    # function to turn from right side to the left side
    hubo.turn_left()
    move_and_pick()
    hubo.turn_left()


def turn_left_to_right():
    # function to turn from the left side to the right side
    turn_right()
    move_and_pick()
    turn_right()

# first you need to move one step before starting
# and then make a loop because the Beepers are starting in the second street
move_and_pick()
# the first turn is from right to left 
# if completed the turn it to false 
# means the turn is the inverse form left to right
right_to_left = True
for row in range(6):
    for i in range(5):
        move_and_pick()
    if row == 5:
        break
    elif right_to_left:
        turn_right_to_left()
        right_to_left = False
    else:
        turn_left_to_right()
        right_to_left = True
