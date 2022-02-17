import pygame
import random
pygame.init()

window = pygame.display.set_mode([400, 400])

colors = 0
while colors < 5:

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    window.fill(color)

    pygame.display.flip()
    pygame.time.wait(1000)
    colors += 1
