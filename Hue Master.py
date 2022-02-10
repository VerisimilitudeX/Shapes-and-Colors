#### ---- SETUP ---- ####

# Import the random library
import random

# Import the PYGAME library
import pygame

# INITialize pygame
pygame.init()

# SET_MODE with size [200, 200], and assign the result
# to a variable called window
window = pygame.display.set_mode([200, 200])


#### ---- DRAW STARTING COLOR ---- ####

# Get a random int between 0 and 255, assign to rand_r
rand_r = random.randint(0, 255)

# Get a random int between 0 and 255, assign to rand_g
rand_g = random.randint(0, 255)

# Get a random int between 0 and 255, assign to rand_b
rand_b = random.randint(0, 255)

# Create a COLOR tuple called rand_color with the
# values rand_r, rand_g, and rand_b
rand_color = (rand_r, rand_g, rand_b)

# Create a RECT at 0, 0 with height and width 200 and
# assign it to the variable rand_rect
rand_rect = pygame.Rect(0, 0, 200, 200)

# DRAW the RECT rand_rect in window with rand_color
pygame.draw.rect(window, rand_color, rand_rect)

# FLIP the display
pygame.display.flip()


#### ---- GET USER'S GUESS ---- ####
# Have the user guess the r value. Typecast to an int
# and assign to guess_r.
guess_r = int(input("What is the r value? "))

# Have the user guess the g value. Typecast to an int
# and assign to guess_g.
guess_g = int(input("What is the g value? "))

# Have the user guess the b value. Typecast to an int
# and assign to guess_b.
guess_b = int(input("What is the b value? "))

# Create a COLOR tuple out of guess_r, guess_g, and
# guess_b and assign it to variable guess_color
guess_color = (guess_r, guess_g, guess_b)


#### ---- DRAW BOTH COLORS ---- ####

# Open a new window using SET_MODE with size [400, 200]
# and assign it to the variable window
window = pygame.display.set_mode([400, 200])

# FILL the window with guess_color
window.fill(guess_color)

# DRAW rand_rect RECT again on window with rand_color
pygame.draw.rect(window, rand_color, rand_rect)

# FLIP the display again
pygame.display.flip()


#### ---- SUMMARY ---- ####

# Print the user's guess color
print("Your guess color was " + str(guess_color) + " . ")

# Print the actual color
print("The actual color was " + str(rand_color) + " . ")

# Get input to pause the program
input("Press enter to end the program")
