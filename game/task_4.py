from cs1robots import *
load_world("worlds/harvest4.wld")
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    # function to turn right
    for _ in range(3):
        hubo.turn_left()

def move_and_pick_2_beepers():
    # function to move and pick 2 beepers
    # if one or 2 beepers found it pick them
    # else it move forward 
    for _ in range(2):
        if hubo.on_beeper():
            hubo.pick_beeper()
    hubo.move()

def turn_right_to_left():
    # function to turn from right side to the left side and pick 2 beepers if found
    hubo.turn_left()
    move_and_pick_2_beepers()
    hubo.turn_left()

def turn_left_to_right():
    # function to turn from the left side to the right side and pick 2 beepers if found
    turn_right()
    move_and_pick_2_beepers()
    turn_right()

move_and_pick_2_beepers()

right_to_left = True
row = 0
while True:
    for i in range(5):
        move_and_pick_2_beepers()
    row += 1
    # if the row is number 6 then stop
    if row == 6:
        break
    if right_to_left:
        turn_right_to_left()
        right_to_left = False
    else:
        turn_left_to_right()
        right_to_left = True
