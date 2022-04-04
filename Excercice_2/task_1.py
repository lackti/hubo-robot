from cs1robots import *
# you can choose any postion you want 
create_world(avenues=10, streets=10)
hubo = Robot(orientation="E",avenue=4, street=7)

hubo.set_trace('blue')
hubo.set_pause(1)

# # first you need to move one step before starting
# # and then make a loop because the Beepers are starting in the second street

while not(hubo.facing_north()):
    hubo.turn_left()
hubo.turn_left()

face_wall = 0

while True:
    # hubo need to face the wall 2 times to back to his initial position
    if face_wall == 2:
        break
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
        face_wall += 1
        
    

