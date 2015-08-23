main_char = "resources/penguin.png"
wheel_file= "resources/wheel.png"
xx = 270
yy = 80

import pygame
from pygame.locals import *
from sys import exit
import os
pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (xx,yy)
screen = pygame.display.set_mode((800,600),0,32)
clock = pygame.time.Clock()

char_x = 100
char_y = 300
char_speed = 200




wheel_x=200
wheel_y=50


character = pygame.image.load(main_char).convert_alpha()
character = pygame.transform.scale(character,(35,55))

wheel = pygame.image.load(wheel_file).convert_alpha()
wheel = pygame.transform.scale(wheel,(480,480))

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    time_passed = clock.tick(50)
    time_passed_seconds = time_passed / 1000.0
    
    pressed_keys = pygame.key.get_pressed()
    
    
    
    # making the character move
    
    if pressed_keys[K_RIGHT]:
        char_x += char_speed * time_passed_seconds
    if pressed_keys[K_LEFT]:
        char_x -= char_speed * time_passed_seconds
    if pressed_keys[K_UP]:
        char_y -= char_speed * time_passed_seconds
    if pressed_keys[K_DOWN]:
        char_y += char_speed * time_passed_seconds          
    # end of the movement
    
    # if character goes out of the screen
            
    if char_x >= 765:
        char_x = 765
    if char_x <= 0:
        char_x = 0
    if char_y <= 0:
        char_y = 0
    if char_y >= 545:
        char_y = 545

    
    # end    
    
    screen.fill((255,255,255))            

        
    screen.fill((255,255,255))
    screen.blit(wheel,(wheel_x,wheel_y))            

    screen.blit(character,(char_x,char_y))
    
    
    
    pygame.display.update()
