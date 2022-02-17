import random

import pygame

pygame.init()

window = pygame.display.set_mode([200, 200])

rand_r = random.randint(0, 255)

rand_g = random.randint(0, 255)

rand_b = random.randint(0, 255)

rand_color = (rand_r, rand_g, rand_b)

rand_rect = pygame.Rect(0, 0, 200, 200)

pygame.draw.rect(window, rand_color, rand_rect)

pygame.display.flip()

guess_r = int(input("What is the r value? "))

guess_g = int(input("What is the g value? "))

guess_b = int(input("What is the b value? "))

guess_color = (guess_r, guess_g, guess_b)

window = pygame.display.set_mode([400, 200])

window.fill(guess_color)

pygame.draw.rect(window, rand_color, rand_rect)

pygame.display.flip()

print("Your guess color was " + str(guess_color) + " . ")

print("The actual color was " + str(rand_color) + " . ")

input("Press enter to end the program")
