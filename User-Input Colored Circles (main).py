#User-input colored circles
#Lets the user choose colors and draw a random circle of each color every time it is loaded]

#Defining pygame and window
import pygame
import sys

pygame.init()
window = pygame.display.set_mode([400, 400])
window.fill((0, 0, 0))

#Intro
print()
print("In this program, 3 circles will be drawn in a target shape. It is up to the user to define what colors these 3 circles will be.")
pygame.time.wait(10000)
print()
print("Thoughout the program, the user will have the choice to either manually enter the RGB color values for the circles or enter a predefined color (red, pink, purple, blue, turquoise, green, yellow, or orange)")
pygame.time.wait(10000)
print()

#Circle 1
mode1 = input("Do you want to use a predefined color or want to manually enter the colors? [manual/predefined]\n")
if mode1 == "manual":
    print("We'll begin with the first circle.\n")
    #red
    rvaluecircle1 = int(input("How much red do you want in the circle. Please enter a number from 0 to 255.\n"))
    percentrvaluecircle1 = round(rvaluecircle1 / 255 * 100, 1)
    if rvaluecircle1 > 255:
        print("I'm sorry, you didn't enter a value from 0 to 255, please restart the program to try again")
        pygame.time.wait(5000)
        sys.exit()
    else:
        print("Got it, your circle will be " + str(percentrvaluecircle1) + "% red. ")
    #green
    gvaluecircle1 = int(input("How much green do you want in the circle. Please enter a number from 0 to 255.\n"))
    percentgvaluecircle1 = round(gvaluecircle1 / 255 * 100, 1)
    if gvaluecircle1 > 255:
        print("I'm sorry, you didn't enter a value from 0 to 255, please restart the program to try again")
        pygame.time.wait(5000)
        sys.exit()
    else:
        print("Okay, your circle will be " + str(percentgvaluecircle1) + "% green. ")
    #blue
    bvaluecircle1 = int(input("How much blue do you want in the circle. Please enter a number from 0 to 255.\n"))
    percentbvaluecircle1 = round(bvaluecircle1 / 255 * 100, 1)
    if bvaluecircle1 > 255:
        print("I'm sorry, you didn't enter a value from 0 to 255, please restart the program to try again")
        pygame.time.wait(5000)
        sys.exit()
    else:
        print("Got it, your circle will be " + str(percentbvaluecircle1) + "% blue. ")
    #circle 1 final color
    circle1color = (rvaluecircle1, gvaluecircle1, bvaluecircle1)
    pygame.draw.circle(window, circle1color, (200, 200), 150)
    pygame.display.flip()
    input("Press enter to create the second circle")
    
    #Circle 2
    print("Now we'll draw our second circle.\n")
    #red
    rvaluecircle2 = int(input("How much red do you want in the circle. Please enter a number from 0 to 255.\n"))
    percentrvaluecircle2 = round(rvaluecircle2 / 255 * 100, 1)
    if rvaluecircle1 > 255:
        print("I'm sorry, you didn't enter a value from 0 to 255, please restart the program to try again")
        pygame.time.wait(5000)
        sys.exit()
    else:
        print("Got it, your circle will be " + str(percentrvaluecircle2) + "% red. ")
        pygame.time.wait(500)
    #green
    gvaluecircle2 = int(input("How much green do you want in the circle. Please enter a number from 0 to 255.\n"))
    percentgvaluecircle2 = round(gvaluecircle2 / 255 * 100, 1)
    if gvaluecircle1 > 255:
        print("I'm sorry, you didn't enter a value from 0 to 255, please restart the program to try again")
        pygame.time.wait(5000)
        sys.exit()
    else:
        print("Okay, your circle will be " + str(percentgvaluecircle2) + "% green. ")
    #blue
    bvaluecircle2 = int(input("How much blue do you want in the circle. Please enter a number from 0 to 255.\n"))
    percentbvaluecircle2 = round(bvaluecircle2 / 255 * 100, 1)
    if bvaluecircle1 > 255:
        print("I'm sorry, you didn't enter a value from 0 to 255, please restart the program to try again")
        pygame.time.wait(5000)
        sys.exit()
    else:
        print("Got it, your circle will be " + str(percentbvaluecircle2) + "% blue. ")
    #circle 2 final
    circle2color = (rvaluecircle2, gvaluecircle2, bvaluecircle2)
    pygame.draw.circle(window, circle2color, (200, 200), 100)
    pygame.display.flip()
    input("Press enter to create the third circle")

    #Circle 3
    print("Lastly, we'll draw the third circle.\n")
    #red
    rvaluecircle3 = int(input("How much red do you want in the circle. Please enter a number from 0 to 255.\n"))
    percentrvaluecircle3 = round(rvaluecircle3 / 255 * 100, 1)
    if rvaluecircle1 > 255:
        print("I'm sorry, you didn't enter a value from 0 to 255, please restart the program to try again")
        pygame.time.wait(5000)
        sys.exit()
    else:
        print("Got it, your circle will be " + str(percentrvaluecircle3) + "% red. ")
    #green
    gvaluecircle3 = int(input("How much green do you want in the circle. Please enter a number from 0 to 255.\n"))
    percentgvaluecircle3 = round(gvaluecircle3 / 255 * 100, 1)
    if rvaluecircle1 > 255:
        print("I'm sorry, you didn't enter a value from 0 to 255, please restart the program to try again")
        pygame.time.wait(5000)
        sys.exit()
    else:
        print("Okay, your circle will be " + str(percentgvaluecircle3) + "% green. ")
    #blue
    bvaluecircle3 = int(input("How much blue do you want in the circle. Please enter a number from 0 to 255.\n"))
    percentbvaluecircle3 = round(bvaluecircle3 / 255 * 100, 1)
    if rvaluecircle1 > 255:
        print("I'm sorry, you didn't enter a value from 0 to 255, please restart the program to try again")
        pygame.time.wait(5000)
        sys.exit()
    else:
        print("Got it, your circle will be " + str(percentbvaluecircle3) + "% blue. ")
    #circle 2 final
    circle3color = (rvaluecircle3, gvaluecircle3, bvaluecircle3)
    pygame.draw.circle(window, circle3color, (200, 200), 50)
    pygame.display.flip()
    print("We will now spend 10 seconds looking at this artistic masterpiece")
    pygame.time.wait(10000)
elif mode1 == "predefined":
    #Circle 1
    circle1colorinput = input("What color do you want circle 1 to be? Your options are: red, pink, purple, blue, turquoise, green, yellow, or orange")
    if circle1colorinput == "red":
        pygame.draw.circle(window, (255, 0, 0), (200, 200), 150)
    elif circle1colorinput == "pink":
        pygame.draw.circle(window, (255, 0, 228), (200, 200), 150)
    elif circle1colorinput == "purple":
        pygame.draw.circle(window, (171, 0, 255), (200, 200), 150)
    elif circle1colorinput == "blue":
        pygame.draw.circle(window, (0, 0, 255), (200, 200), 150)
    elif circle1colorinput == "turquoise":
        pygame.draw.circle(window, (0, 230, 255), (200, 200), 150)
    elif circle1colorinput == "green":
        pygame.draw.circle(window, (0, 255, 0), (200, 200), 150)
    elif circle1colorinput == "yellow":
        pygame.draw.circle(window, (252, 255, 0), (200, 200), 150)
    elif circle1colorinput == "orange":
        pygame.draw.circle(window, (255, 159, 0), (200, 200), 150)
    pygame.display.flip()
    input("Press enter to create the second circle")

    #Circle 2
    circle2colorinput = input("What color do you want circle 2 to be? Your options are: red, pink, purple, blue, turquoise, green, yellow, or orange")
    if circle2colorinput == "red":
        pygame.draw.circle(window, (255, 0, 0), (200, 200), 100)
    elif circle2colorinput == "pink":
        pygame.draw.circle(window, (255, 0, 228), (200, 200), 100)
    elif circle2colorinput == "purple":
        pygame.draw.circle(window, (171, 0, 255), (200, 200), 100)
    elif circle2colorinput == "blue":
        pygame.draw.circle(window, (0, 0, 255), (200, 200), 100)
    elif circle2colorinput == "turquoise":
        pygame.draw.circle(window, (0, 230, 255), (200, 200), 100)
    elif circle2colorinput == "green":
        pygame.draw.circle(window, (0, 255, 0), (200, 200), 100)
    elif circle2colorinput == "yellow":
        pygame.draw.circle(window, (252, 255, 0), (200, 200), 100)
    elif circle2colorinput == "orange":
        pygame.draw.circle(window, (255, 159, 0), (200, 200), 100)
    pygame.display.flip()
    input("Press enter to create the last circle")

    #Circle 3
    circle3colorinput = input("What color do you want circle 3 to be? Your options are: red, pink, purple, blue, turquoise, green, yellow, or orange")
    if circle3colorinput == "red":
        pygame.draw.circle(window, (255, 0, 0), (200, 200), 50)
    elif circle3colorinput == "pink":
        pygame.draw.circle(window, (255, 0, 228), (200, 200), 50)
    elif circle3colorinput == "purple":
        pygame.draw.circle(window, (171, 0, 255), (200, 200), 50)
    elif circle3colorinput == "blue":
        pygame.draw.circle(window, (0, 0, 255), (200, 200), 50)
    elif circle3colorinput == "turquoise":
        pygame.draw.circle(window, (0, 230, 255), (200, 200), 50)
    elif circle3colorinput == "green":
        pygame.draw.circle(window, (0, 255, 0), (200, 200), 50)
    elif circle3colorinput == "yellow":
        pygame.draw.circle(window, (252, 255, 0), (200, 200), 50)
    elif circle3colorinput == "orange":
        pygame.draw.circle(window, (255, 159, 0), (200, 200), 50)
    pygame.display.flip() 

#Display flip and end matter
pygame.display.flip()
input("Press enter to end the program")
