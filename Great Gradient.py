#### ---- SETUP ---- ####

# Import PYGAME
import pygame

# INITialize pygame
pygame.init()

# Open a window with SET_MODE of size [510, 300] and
# assign the result to a variable called window
window = pygame.display.set_mode([510, 300])

# Assign 0 to the variable top
top = 0

# Assign 0 to the variable left
left = 0

# Assign 0 to the variable r
r = 0

# Assign 0 to the variable g
g = 0

# Assign 0 to the variable b
b = 0


#### ---- DRAW GRADIENT ---- ####

# While left is less than 510
while left < 510:

    # Create a RECT at left, top, with width 2 and
    # height 300, and assign it to the variable stripe
    stripe = pygame.Rect(left, top, 2, 300)

    # DRAW the stripe RECT from the previous line in
    # window using the color (r, g, b)
    pygame.draw.rect(window, (r, g, b), stripe)

    # Increment r by 1
    r += 1

    # Increment b by 1
    b += 1

    # Increment left by 2
    left += 2


#### ---- FINISH DRAWING ---- ####

# FLIP the display
    pygame.display.flip()

# Get input to pause the program
input()
