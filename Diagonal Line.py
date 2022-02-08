import pygame
pygame.init()
window = pygame.display.set_mode([400, 400])
window.fill = ((255, 255, 255))

pygame.draw.line(window, (0, 0, 0), (400, 0), (0, 400), 2)

pygame.display.flip()
input()
