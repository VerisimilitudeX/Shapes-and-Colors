import pygame
pygame.init()

front_wheel_color = (70, 70, 70)
back_wheel_color = (50, 50, 50)
car_color = (40, 20, 120)

window = pygame.display.set_mode([400, 400])
window.fill((200, 200, 255))

# Draw the back wheels
pygame.draw.circle(window, back_wheel_color, (75, 300), 50)
pygame.draw.circle(window, back_wheel_color, (325, 300), 50)

# Draw the car
rectangle = pygame.Rect(50, 100, 300, 200)
pygame.draw.rect(window, car_color, rectangle)


# Draw the front wheels
pygame.draw.circle(window, front_wheel_color, (125, 300), 50)
pygame.draw.circle(window, front_wheel_color, (350, 300), 50)

pygame.display.flip()
pygame.time.wait(5000)
