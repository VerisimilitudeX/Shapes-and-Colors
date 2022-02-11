#### ---- SETUP ---- ####

# Import the random library
import random

# Import the PYGAME library
import pygame

# INITialize pygame
pygame.init()

# SET_MODE to open a window with size [600, 300] and
# assign the result to variable window
window = pygame.display.set_mode([600, 300])

# FILL the window with the color (255, 255, 255)
window.fill((255, 255, 255))

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
count = 1

# Get a random int 1 - 3, and assign to the
# variable different
different = random.randint(1, 3)

# Get a random int between 0 and 230 and assign to r
r = random.randint(0, 230)

# Get a random int between 0 and 230 and assign to g
g = random.randint(0, 230)

# Get a random int between 0 and 230 and assign to b
b = random.randint(0, 230)


#### ---- DRAW TRIANGLES ---- ####

# While count is less than or equal to 3
while count <= 3:

    # If count is equal to different
    if count == different:
        
        # Create a COLOR tuple with the values r + 15,
        # g + 15, b + 15, and assign to variable color
        color = (r + 15, g + 15, b + 15)

    # Else
    else:

        # Create a COLOR tuple with values r, g, b and
        # assign it to variable color
        color = (r, g, b)

    # DRAW a POLYGON with points (left, bottom),
    # (middle, top), and (right, bottom) in window
    # using color variable
    pygame.draw.polygon(window, color, [(left, bottom), (middle, top), (right, bottom)])

    # Increment count by 1
    count += 1

    # Increment left by 200
    left +- 200

    # Increment middle by 200
    middle += 200

    # Increment right by 200
    right += 200

# FLIP the display
pygame.display.flip()


#### ---- USER GUESS ---- ####

# Ask user to guess which shape is a different color.
# Typecast to an int and assign to variable guess.
guess = int(input("Was the different color 1, 2, or 3? "))

# If guess is equal to different
if guess == different:

    # Tell the user they guessed right
    print("You got it! ")

# Else
else:

    # Tell the user what the correct answer was
    # (variable different)
    print("Sorry, that's not right.  It was " + str(different) + " . ")
