import pygame
import random
pygame.init()

window = pygame.display.set_mode([400, 400])

# Loop through five colors
colors = 0
while colors < 5:

    # Fill the screen with a random color
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    window.fill(color)
    
    # Wait a second and increment the loop number
    pygame.display.flip()
    pygame.time.wait(1000)
    colors += 1
