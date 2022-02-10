"""
LESSON: 3.2 - Shapes & Color
EXERCISE: Shade Imposter
"""

#### ---- SETUP ---- ####

# Import the random library
import random

# Import the PYGAME library
import pygame

# INITialize pygame
pygame.init()

# SET_MODE to open a window with size [600, 300] and
# assign the result to variable window
pygame.display.set_mode([600, 300])

# FILL the window with the color (255, 255, 255)
window.fill(255, 255, 255)

# Assign variable left the value 50
left = 50

# Assign variable middle the value 100
middle = 100

# Assign variable right the value 150
right = 150

# Assign variable top the value 50
top = 50

# Assign variable bottom the value 250
bottom = 250

# Assign variable count the value 1
# ---> TEST AFTER THIS LINE <--- #
count = 1

# Get a random int 1 - 3, and assign to the
# variable different
different = random.randint(1, 3)

# Get a random int between 0 and 230 and assign to r
r = random.randint(0, 230)

# Get a random int between 0 and 230 and assign to g
g = random.randint(0, 230)

# Get a random int between 0 and 230 and assign to b
# ---> TEST AFTER THIS LINE <--- #
b = random.randint(0, 230)


#### ---- DRAW TRIANGLES ---- ####

# While count is less than or equal to 3
while count <= 3:

    # If count is equal to different
    if count == different
        
        # Create a COLOR tuple with the values r + 15,
        # g + 15, b + 15, and assign to variable color
        color = (r + 15, g + 15, b + 15)

    # Else
    else:

        # Create a COLOR tuple with values r, g, b and
        # assign it to variable color


    # DRAW a POLYGON with points (left, bottom),
    # (middle, top), and (right, bottom) in window
    # using color variable


    # Increment count by 1
    # ---> TEST AFTER THIS LINE <--- #


    # Increment left by 200


    # Increment middle by 200


    # Increment right by 200
    # ---> TEST AFTER THIS LINE <--- #


# FLIP the display



#### ---- USER GUESS ---- ####

# Ask user to guess which shape is a different color.
# Typecast to an int and assign to variable guess.
# ---> TEST AFTER THIS LINE <--- #


# If guess is equal to different


    # Tell the user they guessed right
    # ---> TEST AFTER THIS LINE <--- #


# Else


    # Tell the user what the correct answer was
    # (variable different)
    # ---> TEST AFTER THIS LINE <--- #




# Turn in your Coding Exercise.
