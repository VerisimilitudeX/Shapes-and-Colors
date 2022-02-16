import pygame

pygame.init()

window = pygame.display.set_mode([510, 300])

top = 0

left = 0

r = 0

g = 0

b = 0

while left < 510:

    stripe = pygame.Rect(left, top, 2, 300)

    pygame.draw.rect(window, (r, g, b), stripe)

    r += 1

    b += 1

    left += 2

    pygame.display.flip()

input()
