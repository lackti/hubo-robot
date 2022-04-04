import time 
from cs1robots import *
load_world('worlds/trash2.wld')
hubo = Robot()
hubo.set_trace('red')

def turn_right():
    # function to turn right
    for _ in range(3):
        hubo.turn_left()

def turn_right_to_left():
    # function to turn from right side to the left side
    hubo.turn_left()
    hubo.turn_left()

def put_trash_and_back():
    # function to put the trush and back to the initial position
    turn_right()
    hubo.move()
    hubo.turn_left()
    while hubo.carries_beepers():
        hubo.drop_beeper()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def pick_beepeers():
    bepeers_picked = 0
    while True:
        if hubo.on_beeper():
            hubo.pick_beeper()
            bepeers_picked += 1
        else:
            return bepeers_picked

right_to_left = True
total_beepers_collected = 0
faced_wall = 0
while True:
    if hubo.front_is_clear():
        beepers_collected = pick_beepeers()
        total_beepers_collected += beepers_collected
        hubo.move()
    else:
        if faced_wall == 0:
            # if faced the first wall then turn left to right and continue
            turn_right_to_left()
            faced_wall += 1
        else:
            # if faced the second wall then put all the trush and back to init position
            put_trash_and_back()
            break
    

