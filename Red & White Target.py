import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((0, 0, 0))

red = (150, 0, 0)
white = (255, 255, 255)

pygame.draw.circle(window, red, (200, 200), 150)
pygame.draw.circle(window, white, (200, 200), 100)
pygame.draw.circle(window, red, (200, 200), 50)

pygame.display.flip()
pygame.time.wait(5000)
