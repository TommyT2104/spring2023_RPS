# File created by Thomas Trombatore
# import libraries
from time import sleep

from random import randint

import pygame as pg

import os

# setup asset folders which are images and sounds
game_folder = os.path.dirname(__file__)
# prints these asset folders
print(game_folder)

# game settings the width, hight, and frames per second of the video game that is being printed
WIDTH = 360
HEIGHT = 480
FPS = 30

# Tuples are immutable and cannot change once created
# define the color white
WHITE = (255, 255, 255)
# define the color black
BLACK = (255, 255, 255)
# define the color red
RED = (255, 0, 0)
# define the color green
GREEN = (255, 255, 255)
# define the color blue
BLUE = (255, 255, 255)

# initiate pygame which means it is ready to use the pixels on the screen
pg.init()
pg.mixer.init()


# sets the constant width and constant height to the display
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors...")

# used to get the current processor time as a floating point number expressed in seconds
clock = pg.time.Clock()

# pulls the rock image from your files and creates a variable to hold the images of rock 
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
# it is storing not the pixels themself but the dimensions and allows us to access and change those things
rock_image_rect = rock_image.get_rect()

# pulls the paper image from your files and creates a variable to hold the images of paper 
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
# it is storing not the pixels themself but the dimensions and allows us to access and change those things
paper_image_rect = paper_image.get_rect()

# pulls the scissors image from your files and creates a variable to hold the images of scissors
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
# it is storing not the pixels themself but the dimensions and allows us to access and change those things
scissors_image_rect = scissors_image.get_rect()

# when the game is running it is telling the comuter to run the code
running = True

# when the code is running it prints a message according to where you click on the pygame
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # when clicking x running is false
            running = False
        # Mousebutton up means once you release the click
        if event.type == pg.MOUSEBUTTONUP:
            # displays the coordinates where we click. 0 is the x value 
            print(pg.mouse.get_pos()[0])
            # 1 is the y value
            print(pg.mouse.get_pos()[1])
            # stores the mouse coordinates
            mouse_coords = pg.mouse.get_pos()
            # These are the data types returning a true or false
            print(rock_image_rect.collidepoint(mouse_coords))
        if rock_image_rect.collidepoint(mouse_coords):
            print("you clicked on rock..")
        elif paper_image_rect.collidepoint(mouse_coords):
                pass
    # says if you don't click on rock or paper the computer says the message
        else:
            print("you didnt click on anything")
        ########## input ###########
    # HCI - human computer interaction...
    # keyboard, mouse, controller, vr headset
    ########## update ###################
    rock_image_rect.x += -1
    rock_image_rect.y += 1

     ############ draw ###################
    screen.fill(BLACK)

    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)


# allows only a portion of the screen to be updated instead of the entire area
    pg.display.flip()

# this ends the program
pg.quit()