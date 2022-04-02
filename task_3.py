from cs1robots import *
load_world("worlds/hurdles2.wld")
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    # function to turn right
    for _ in range(3):
        hubo.turn_left()
    

def jump_one_hurdle():
    # function to jum one hurdle
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()

while True:
    # if beeper has been found stop
    if hubo.on_beeper():
        break
    # if a wall in front then jump
    elif not(hubo.front_is_clear()):
        jump_one_hurdle()
    # if nothing in front and there's no beeper then move forward
    else:
        hubo.move()
