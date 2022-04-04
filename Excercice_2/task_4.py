import time 
from cs1robots import *
load_world('worlds/rain1.wld')
hubo = Robot(beepers=100, avenue=2, street=6, orientation="E")
#hubo.set_trace('red')

def turn_right():
    # function to turn right
    for _ in range(3):
        hubo.turn_left()

# first moves to enter inside the box
hubo.move()
hubo.turn_left()
hubo.move()

while True:
    if hubo.get_pos() == (3,6):
        hubo.turn_left()
        break
    if hubo.facing_north() and hubo.left_is_clear():
        hubo.turn_left()
    elif hubo.front_is_clear():
        if hubo.left_is_clear():
            time.sleep(1)
            hubo.drop_beeper()
            hubo.move()
        else:
            hubo.move()
    else:
        turn_right()
        if hubo.left_is_clear():
            hubo.turn_left()

 
    