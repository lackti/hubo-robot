import time 
from cs1robots import *
load_world('worlds/trash4.wld')
hubo = Robot()
hubo.set_trace('red')

def turn_right():
    # function to turn right
    for _ in range(3):
        hubo.turn_left()

def turn_right_to_left():
    # function to turn from right side to the left and move one step up
    hubo.turn_left()
    move_and_pick_beepeers()
    hubo.turn_left()

def turn_left_to_right():
    # function to turn from left side to the right and move one step up
    turn_right()
    move_and_pick_beepeers()


def move_and_pick_beepeers():
    if not hubo.on_beeper():
        hubo.move()
    else:
        while hubo.on_beeper():
            hubo.pick_beeper()
        hubo.move()


right_to_left = True
# this number of turn i set because before the first turn  
number_of_turn = 0
while True:
    # condition of the end if hubo face the upper wall 
    if number_of_turn:
        if not hubo.right_is_clear() and not hubo.front_is_clear():
            hubo.turn_left()
            while hubo.front_is_clear():
                move_and_pick_beepeers()
            hubo.turn_left()
            while hubo.carries_beepers():
                hubo.drop_beeper()
            break
        elif not hubo.left_is_clear() and not hubo.front_is_clear():
            hubo.turn_left()
            hubo.turn_left()
            while hubo.front_is_clear():
                move_and_pick_beepeers()
            hubo.turn_left()
            while hubo.front_is_clear():
                move_and_pick_beepeers()
            hubo.turn_left()
            while hubo.carries_beepers():
                hubo.drop_beeper()
            break
    # move and pick beepers
    if hubo.front_is_clear():
        move_and_pick_beepeers()
    else:
        if right_to_left:
            turn_right_to_left()
            right_to_left = False
            
        else:
            turn_left_to_right()
            turn_left_to_right()
            right_to_left = True
        number_of_turn += 1
    

