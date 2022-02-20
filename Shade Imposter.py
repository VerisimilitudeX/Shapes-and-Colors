import random
import pygame

pygame.init()
window = pygame.display.set_mode([600, 300])
window.fill((255, 255, 255))

left = 50
middle = 100
right = 150
top = 50
bottom = 250
count = 1

different = random.randint(1, 3)

r = random.randint(0, 230)
g = random.randint(0, 230)
b = random.randint(0, 230)

while count <= 3:
    if count == different:
        color = (r + 15, g + 15, b + 15)

    else:
        color = (r, g, b)

    pygame.draw.polygon(window, color, [(left, bottom), (middle, top), (right, bottom)])

    count += 1
    left +- 200
    middle += 200
    right += 200

pygame.display.flip(
guess = int(input("Was the different color 1, 2, or 3? "))

if guess == different:
    print("You got it! ")


else:
    print("Sorry, that's not right.  It was " + str(different) + " . ")
