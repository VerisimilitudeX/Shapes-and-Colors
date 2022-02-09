import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((0, 0, 0))

# Get colors from user input
red = int(input("How much red do you want in the circle? "))
green = int(input("How much red do you want in the circle? "))
blue = int(input("How much red do you want in the circle? "))
color = (red, green, blue)

# Draw circle
pygame.draw.circle(window, color, (200, 200), 100)

pygame.display.flip()
pygame.time.wait(5000)
