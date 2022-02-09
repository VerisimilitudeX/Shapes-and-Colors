import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((200, 220, 255))

blue = (100, 130, 180)
gray = (180, 180, 180)
black = (0, 0, 0)

# Draw house
house = pygame.Rect(100, 150, 200, 200)
pygame.draw.rect(window, blue, house)
pygame.draw.rect(window, black, house, 2)

# Draw roof
pygame.draw.polygon(window, gray, [(100, 150), (200, 0), (300, 150)])
pygame.draw.polygon(window, black, [(100, 150), (200, 0), (300, 150)], 2)

# Draw door
door = pygame.Rect(200, 300, 40, 50)
pygame.draw.rect(window, gray, door)
pygame.draw.rect(window, gray, door, 3)

pygame.display.flip()
pygame.time.wait(5000)
