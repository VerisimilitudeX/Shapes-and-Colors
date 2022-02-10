#### ---- SET UP WINDOW ---- ####

# Import the PYGAME library
import pygame

# INITialize pygame
pygame.init()

# SET_MODE to open a window of size [400, 300], assign
# to the variable window
window = pygame.display.set_mode([400, 300])


#### ---- DRAW RECTANGLES ---- ####

# Create a COLOR tuple with values 175, 175, 175 and
# assign it to a variable called gray
gray = (175, 175, 175)

# Create a COLOR tuple with values 120, 120, 240 and
# assign it to a variable called purple
purple = (120, 120, 240)

# Create a RECT with left side 0, top 0, width 200 and
# height 300. Assign it to a variable called left.
left = pygame.Rect(0, 0, 200, 300)

# DRAW the left RECT using window and gray
pygame.draw.rect(window, gray, left)

# Create a RECT with left side 200, top 0, width 200
# and height 300. Assign it to a variable called right.
right = pygame.Rect(200, 0, 200, 300)

# DRAW the right RECT using window and purple
pygame.draw.rect(window, purple, right)


#### ---- DRAW CIRCLES ---- ####

# Create a COLOR tuple with values 150, 150, 200 and
# assign it to the variable mid
mid  = (150, 150, 200)

# DRAW a CIRCLE in window with color mid at position
# (100, 150) with radius 20
pygame.draw.circle(window, mid, (100, 150), 20)

# DRAW another CIRCLE in window with color mid at
# position (300, 150) with radius 20
pygame.draw.circle(window, mid, (300, 150), 20)


#### ---- FINISH ---- ####

# FLIP the display
pygame.display.flip()

# Get input to pause the program
input("Press enter to pause the program")

white = (255, 255, 255)
window.fill(white)

pygame.draw.circle(window, mid, (300, 150), 20)
pygame.draw.circle(window, mid, (100, 150), 20)

pygame.display.flip()

input()
