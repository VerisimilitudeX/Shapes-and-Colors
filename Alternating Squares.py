import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((128, 128, 128))

left_rect = pygame.Rect(50, 50, 200, 200)
right_rect = pygame.Rect(150, 150, 200, 200)

left_color = (0, 0, 0)
right_color = (255, 255, 255)

loops = 10

pygame.draw.rect(window, left_color, left_rect)
pygame.draw.rect(window, right_color, right_rect)

# Declare alternating loop boolean

while loops > 0:

    # Every other loop, draw the right rectangle
    # over the left one
    if loops % 2 == 0:
        pygame.draw.rect(window, left_color, left_rect)

    # Otherwise, draw the left rectangle
    # over the right one
    else:
        pygame.draw.rect(window, right_color, right_rect)

    # Switch alternating boolean

    pygame.display.flip()
    pygame.time.wait(1000)
    loops -= 1
