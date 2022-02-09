# Add outline to existing shapes to find hidden picture

import pygame
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

window = pygame.display.set_mode([400, 400])
window.fill((50, 50, 50))

# Outline each shape
pygame.draw.circle(window, white, (200, 150), 200)
pygame.draw.circle(window, black, (200, 150), 200, 3)

pygame.draw.circle(window, white, (200, 200), 180)
pygame.draw.circle(window, black, (200, 200), 180, 3)

pygame.draw.circle(window, white, (130, 130), 40)
pygame.draw.circle(window, black, (130, 130), 40, 3)

pygame.draw.circle(window, white, (130, 130), 10)
pygame.draw.circle(window, black, (130, 130), 10, 3)

pygame.draw.circle(window, white, (270, 130), 40)
pygame.draw.circle(window, black, (270, 130), 40, 3)

pygame.draw.circle(window, white, (270, 130), 10)
pygame.draw.circle(window, black, (270, 130), 10, 3)

pygame.draw.polygon(window, white, [(200, 130), (200, 260), (250, 230)])
pygame.draw.polygon(window, white, [(200, 130), (200, 260), (250, 230)], 3)

rect = pygame.Rect(120, 290, 80, 40)
pygame.draw.ellipse(window, white, rect)
pygame.draw.ellipse(window, black, rect, 3)

pygame.display.flip()
pygame.time.wait(5000)
