# FIle Created By: Thomas Trombatore

# Libraries are outside of the python code and are used for this rock paper scissors code
from time import sleep
from random import randint
import pygame as pg
import os

# Allows accesses to the game folder
game_folder = os.path.dirname(__file__)
print(game_folder)

# Sets the width, height, and frames per second for the pygame window
WIDTH = 860
HEIGHT = 680
FPS = 30

# Defines the colors. The colors are defined by Red,Green,Blue, Black, and White 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# This is a list of three strings.
objects = ["rock", "paper", "scissors"]

# def stores multiple lines of code and functions 
def start_screen():
    # screen is a pygame exclusive variable that shows images 
    screen.fill(BLACK)
    screen.blit(octagon_image, octagon_image_rect)
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    # pg.display.flip() updates the display with the screen images
    pg.display.flip()

# def stores multiple lines of code and functions 
def reset():
    # rect loads in the image, no rect defines the image
    screen.blit(rock_image, rock_image_rect)
    rock_image_rect.x = 0
    rock_image_rect.y = 10
    screen.blit(paper_image, paper_image_rect)
    paper_image_rect.x = 250
    paper_image_rect.y = 400
    screen.blit(scissors_image, scissors_image_rect)
    scissors_image_rect.x = 0
    scissors_image_rect.y = 400
    screen.blit(cpu_rock_image, cpu_rock_image_rect)
    cpu_rock_image_rect.x = -500
    cpu_rock_image_rect.y = -500
    screen.blit(cpu_scissors_image, cpu_scissors_image_rect)
    cpu_scissors_image_rect.x = -600
    cpu_scissors_image_rect.y = -600
    screen.blit(cpu_paper_image, cpu_scissors_image_rect)
    cpu_paper_image_rect.x = -700
    cpu_paper_image_rect.y = -700
    screen.blit(win_image, win_image_rect)
    win_image_rect.x = -2050
    screen.blit(lose_image, lose_image_rect)
    lose_image_rect.x = -2050
    screen.blit(tie_image, tie_image_rect)
    tie_image_rect.x = -2050
    screen.blit(restart_image, restart_image_rect)
    restart_image_rect.x = -2050

# def stores multiple lines of code and functions 
def win_screen():
    # rect loads in the image, no rect defines the image
    screen.blit(win_image, win_image_rect)
    win_image_rect.x = 325
    win_image_rect.y = 400
    # pg.display.flip() updates the display with the screen images
    pg.display.flip()

# def stores multiple lines of code and functions 
def tie_screen():
    # rect loads in the image, no rect defines the image
    screen.blit(tie_image, tie_image_rect)
    tie_image_rect.x = 400
    tie_image_rect.y = 400
    # pg.display.flip() updates the display with the screen images
    pg.display.flip()

# def stores multiple lines of code and functions 
def lose_screen():
    # rect loads in the image, no rect defines the image
    screen.blit(lose_image, lose_image_rect)
    lose_image_rect.x = 300
    lose_image_rect.y = 400
    # pg.display.flip() updates the display with the screen images
    pg.display.flip()

# def stores multiple lines of code and functions 
def restart_button():
    # rect loads in the image, no rect defines the image
    screen.blit(restart_image, restart_image_rect)
    restart_image_rect.x = 5
    restart_image_rect.y = 475
    # pg.display.flip() updates the display with the screen images
    pg.display.flip()

# def stores multiple lines of code and functions 
def cpu_randchoice():
    choice = objects[randint(0, 2)]
    print("The computer chose " + choice)
    # returns the users choice
    return choice

# def stores multiple lines of code and functions 
def cpu_rock():
    # rect loads in the image, no rect defines the image
    screen.blit(cpu_rock_image, cpu_rock_image_rect)
    cpu_rock_image_rect.x = 500
    cpu_rock_image_rect.y = 50
    # pg.display.flip() updates the display with the screen images
    pg.display.flip()

# def stores multiple lines of code and functions 
def cpu_paper():
    # rect loads in the image, no rect defines the image
    screen.blit(cpu_paper_image, cpu_paper_image_rect)
    cpu_paper_image_rect.x = 500
    cpu_paper_image_rect.y = 150
    # pg.display.flip() updates the display with the screen images
    pg.display.flip()

# def stores multiple lines of code and functions 
def cpu_scissors():
    # rect loads in the image, no rect defines the image
    screen.blit(cpu_scissors_image, cpu_scissors_image_rect)
    cpu_scissors_image_rect.x = 500
    cpu_scissors_image_rect.y = 150
    # pg.display.flip() updates the display with the screen images
    pg.display.flip()

# def stores multiple lines of code and functions 
def player_rock():
    # rect loads in the image, no rect defines the image
    screen.blit(rock_image, rock_image_rect)
    rock_image_rect.x = 150
    rock_image_rect.y = 50
    paper_image_rect.x = -500
    scissors_image_rect.x = -500
    # pg.display.flip updates the display with the screen images
    pg.display.flip

# def stores multiple lines of code and functions 
def player_scissors():
    # rect loads in the image, no rect defines the image
    screen.blit(scissors_image, scissors_image_rect)
    scissors_image_rect.x = 250
    scissors_image_rect.y = 150
    rock_image_rect.x = -500
    paper_image_rect.x = -500
    # pg.display.flip updates the display with the screen images
    pg.display.flip

# def stores multiple lines of code and functions 
def player_paper():
    # rect loads in the image, no rect defines the image
    screen.blit(paper_image, paper_image_rect)
    paper_image_rect.x = 250
    paper_image_rect.y = 150
    scissors_image_rect.x = -500
    rock_image_rect.x = -500
    # pg.display.flip updates the display with the screen images
    pg.display.flip

# init means to initializes pygame modules to get everything going
pg.init()
# screen is defined by Width and Height
screen = pg.display.set_mode((WIDTH, HEIGHT))
# set_caption displays text in the window tab
pg.display.set_caption("Rock, Paper, Scissors")
# time.clock keeps track of amount of time
clock = pg.time.Clock()

# loads in the image
win_image = pg.image.load(os.path.join(
    game_folder, 'youwin.png')).convert()
#  defines the x or y-value
# image_rect defines the image in pygame
win_image_rect = win_image.get_rect()
win_image_rect.x = -2050

# loads in the image
lose_image = pg.image.load(os.path.join(
    game_folder, 'youlose.png')).convert()
# image_rect defines the image in pygame
lose_image_rect = lose_image.get_rect()
lose_image_rect.x = -2050

# loads in the image
tie_image = pg.image.load(os.path.join(
    game_folder, 'youtie.png')).convert()
# image_rect defines the image in pygame
tie_image_rect = tie_image.get_rect()
tie_image_rect.x = -2050

# loads in the image
restart_image = pg.image.load(os.path.join(
    game_folder, 'spacerestart.png')).convert()
# image_rect defines the image in pygame
restart_image_rect = restart_image.get_rect()
restart_image_rect.x = -2050

# octagon_image_rect.x uses the modulus operator, but the octagon_image_rect.y uses the exponentiation operator
octagon_image = pg.image.load(os.path.join(
    game_folder, 'octagon.jpg')).convert()
# image_rect defines the image in pygame
octagon_image_rect = octagon_image.get_rect()
octagon_image_rect.x = (100 % 10)
octagon_image_rect.y = (500 ** 0)

# rock_image_rect.x uses the subtraction operator, but the rock_image_rect.y uses the addition operator
rock_image = pg.image.load(os.path.join(game_folder, 'therock.jpg')).convert()
# image_rect defines the image in pygame
rock_image_rect = rock_image.get_rect()
rock_image_rect.x = (5 - 5)
rock_image_rect.y = (0 + 10)

# scissors_image_rect.x"uses the subtraction operator, but the "scissors_image_rect.y" uses the addition operator
scissors_image = pg.image.load(os.path.join(
    game_folder, 'scissors.jpg')).convert()
# image_rect defines the image in pygame
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = (5000000000000000 - 5000000000000000)
scissors_image_rect.y = (200 + 200)


# paper_image_rect.x uses the division operator, but the paper_image_rect.y uses the multiplication operator
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
# image_rect defines the image in pygame
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = (500 / 2)
paper_image_rect.y = (200 * 2)

# loads in the image
cpu_rock_image = pg.image.load(os.path.join(
    game_folder, 'therock.jpg')).convert()
# image_rect defines the image in pygame
cpu_rock_image_rect = cpu_rock_image.get_rect()
cpu_rock_image_rect.x = -500
cpu_rock_image_rect.y = -500

# loads in the image
cpu_scissors_image = pg.image.load(os.path.join(
    game_folder, 'scissors.jpg')).convert()
# image_rect defines the image in pygame
cpu_scissors_image_rect = cpu_scissors_image.get_rect()
cpu_scissors_image_rect.x = -600
cpu_scissors_image_rect.y = -600

#  loads in the image
cpu_paper_image = pg.image.load(
    os.path.join(game_folder, 'paper.jpg')).convert()
# image_rect defines the image in pygame
cpu_paper_image_rect = cpu_paper_image.get_rect()
cpu_paper_image_rect.x = -700
cpu_paper_image_rect.y = -700

# running is the function in the pygame engine that is displaying it's function
running = True
# player_choice are the options that the user may choose from
player_choice = ""
#  cpu_choice is the choice the computer chooses
cpu_choice = ""

# while the loop is active the program runs forever
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        # if statements define a variable's function and what happens when that variable is used
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                reset()
        if event.type == pg.MOUSEBUTTONUP:
            mouse_coords = pg.mouse.get_pos()
            if rock_image_rect.collidepoint(mouse_coords):
                print("You chose rock")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
                # elif statements are more specific else statement
            elif paper_image_rect.collidepoint(mouse_coords):
                print("You chose paper")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("You chose scissors")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()
                # else statements are anything else that may happen besides the variable's function
            else:
                print("You chose nothing")

# Defined function in which I made the start screen
    start_screen()

# "if" statement; defines a variable's function and what will occur if variable is used
# Multiple defined functions occur if certain "if" combinations occur
    if player_choice == "rock":
        if cpu_choice == "rock":
            cpu_rock()
            player_rock()
            tie_screen()
            restart_button()
        if cpu_choice == "paper":
            cpu_paper()
            player_rock()
            lose_screen()
            restart_button()
        if cpu_choice == "scissors":
            cpu_scissors()
            player_rock()
            win_screen()
            restart_button()
    if player_choice == "paper":
        if cpu_choice == "rock":
            cpu_rock()
            player_paper()
            win_screen()
            restart_button()
        if cpu_choice == "paper":
            cpu_paper()
            player_paper()
            tie_screen()
            restart_button()
        if cpu_choice == "scissors":
            cpu_scissors()
            player_paper()
            lose_screen()
            restart_button()
    if player_choice == "scissors":
        if cpu_choice == "rock":
            cpu_rock()
            player_scissors()
            lose_screen()
            restart_button()
        if cpu_choice == "paper":
            cpu_paper()
            player_scissors()
            win_screen()
            restart_button()
        if cpu_choice == "scissors":
            cpu_scissors()
            player_scissors()
            tie_screen()
            restart_button()

# pygame stops running and exits
pg.quit
