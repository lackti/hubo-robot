from cs1media import *

# This code converts an image into 3 colors yellow green and blue.

# thresholds
th_bright = 200
th_dark = 100

# colors
yellow = (255, 255, 0)

green = (0, 255, 0)

blue = (0, 0, 255)



#image = load_picture('./images/sherlock.jpg')
image = load_picture('./images/01.png')

width, height = image.size()


for y in range(height):
    for x in range(width):

        r, g, b = image.get(x, y)

        average_brightness = (r + g + b) // 3

        if average_brightness <= th_dark:

            image.set(x, y, blue)

        elif average_brightness >= th_bright:
            image.set(x, y, yellow)
        else:
            image.set(x, y, green)

image.show()
