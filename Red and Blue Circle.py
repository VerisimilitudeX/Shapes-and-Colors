import pygame
pygame.init()

win = pygame.display.set_mode([300, 300])
win.fill((255, 255, 255))

# Draw circles here
pygame.draw.circle(win, (200, 0, 0), (150, 150), 100)
pygame.draw.circle(win, (0, 0, 200), (150, 150), 50)

pygame.display.flip()
input("Press enter to close the window")
