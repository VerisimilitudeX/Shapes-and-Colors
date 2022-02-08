import pygame
pygame.init()

win = pygame.display.set_mode([300, 300])
win.fill((255, 255, 255))

pygame.draw.line(win, (0, 0, 0), (300, 0), (0, 300))
r = pygame.Rect(50, 50, 200, 100)
pygame.draw.rect(win, (255, 255, 255), r)
pygame.draw.ellipse(win, (255, 0, 255), r)
pygame.draw.circle(win, (200, 200, 200), (150, 150), 50)
pygame.draw.polygon(win, (100, 100, 100), [(150, 0), (150, 300), (0, 300)])

pygame.display.flip()
pygame.time.wait(4000)
