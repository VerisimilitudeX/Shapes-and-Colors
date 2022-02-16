import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((200, 200, 255))
color = (0, 30, 80)

top_left = (0, 150)
bottom_left = (0, 250)
top_top = (300, 100)
top_bottom = (300, 150)
bottom_top = (300, 250)
bottom_bottom = (300, 300)
middle_center = (400, 200)

pygame.draw.polygon(window, color, [top_left, bottom_left, bottom_top, bottom_bottom, middle_center, top_top, top_bottom])

pygame.display.flip()
input("Press enter to end the program")
