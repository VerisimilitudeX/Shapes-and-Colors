"""
LESSON: 3.2 - Shapes & Color
TECHNIQUE 1: Defining a Shape
PRACTICE 2
"""

import pygame
pygame.init()

window = pygame.display.set_mode([300, 300])
window.fill((0, 0, 0))
color = (140, 198, 62)

# Declare the points
top_left = (100, 0)
top_right = (250, 0)
top_bottom_left = (100, 50)
top_bottom_right = (250, 50)
top_bottom_middle_left = (150, 50)
top_bottom_middle_right = (200, 50)
bottom_left = (150, 350)
bottom_right = (200, 350)

# Draw the T
pygame.draw.polygon(window, color, [top_left, top_right, top_bottom_right, top_bottom_middle_right, bottom_right, bottom_left, top_bottom_middle_left, top_bottom_left, top_left])

pygame.display.flip()
pygame.time.wait(100000)


# Turn in your Coding Exercise.
