import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])

red = 255
green = 255
blue = 255

timer = 255
while timer >= 0:

    window.fill((128, 128, 128))

    # Make a color that starts white and becomes black

    color = (red, green, blue)
    
    # Draw the rectangle of that color
    rectangle = pygame.Rect(100, 100, 200, 200)
    pygame.draw.rect(window, color, rectangle)

    red -= 1
    green -= 1
    blue -= 1

    pygame.display.flip()
    pygame.time.wait(10)
    timer -= 1
