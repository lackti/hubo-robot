from cs1robots import *
# you can change the avenues and streets from here
avenues=10
streets=7
create_world(avenues=avenues, streets=streets)
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    # function to turn right
    for _ in range(3):
        hubo.turn_left()

def square_move():
    # function to turn back with a square
    turn_right()
    hubo.move()
    turn_right()

if (avenues >= 1 or streets >= 1) and (avenues + streets > 2):
    hubo.turn_left()
    # couter of the avenue number
    count = 0
    for i in range(avenues):
        for _ in range(streets-1):
            hubo.move()
        count += 1
        square_move()
        for __ in range(streets-1):
            hubo.move()
        count += 1
        if count == avenues:
            break
        hubo.turn_left()
        hubo.move()
        hubo.turn_left()
else:
    print('Streets and avenues should be greater than (1,1)')
