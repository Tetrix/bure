background = "resources/ledena_doba.jpg"
star_file = "resources/star2/s2_1.png"
s1 = 'resources/star2/s2_1.png'
s2 = 'resources/star2/s2_2.png'
s3 = 'resources/star2/s2_3.png'

import pygame
from pygame.locals import *
from sys import exit
import os
import time
from gameobjects.vector2 import Vector2
from math import *
import random
from character import Character
from wheel import Wheel
from star import Star

pygame.init()

window_x = 270
window_y = 80




# Window positioning
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (window_x,window_y)

pygame.display.set_caption('BURE')

myfont = pygame.font.Font("resources/fonts/gentium.ttf", 40)

# Window positioning
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (window_x,window_y)
# Loading font
myfont = pygame.font.SysFont("resources/fonts/gentium.ttf", 40)

goalfont = pygame.font.Font("resources/fonts/ubuntu.ttf", 30)

screen = pygame.display.set_mode((800,600),0,32)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

#Background
ledena_doba = pygame.image.load(background).convert()
ledena_doba = pygame.transform.scale(ledena_doba,(800,600))

#making instance of class Character
main_character = Character()
main_character.properties()

#making instance of class Wheel
first_wheel = Wheel()
first_wheel.wheel_properties()

#making instance of class Star
star_object = Star()
star_object.star_properties()

star_draw_pos =Vector2(447,302)


#main loop
while True: 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == first_wheel.wheel_rotate: #rotate the wheel and the star 

            first_wheel.wheel_rotation_direction=+0.0
            star_object.star_rotation_direction=+0.0   

            first_wheel.wheel_rotation_direction=+1.0
            star_object.star_rotation_direction=+1.0   

        if event.type == star_object.star_event:
            star_file=s1
        if event.type == star_object.star2_event:
            star_file=s2
        if event.type == star_object.star3_event:
            star_file=s3
    
    main_character.character_rect.topleft = (main_character.char_x,main_character.char_y)
    star_object.star_rect.topleft=(star_draw_pos.x,star_draw_pos.y)
           
    time_passed = clock.tick(80)
    time_passed_seconds = time_passed / 1000.0
    
    pressed_keys = pygame.key.get_pressed()

    star_object.star=pygame.image.load(star_file).convert()
    star_object.star.set_colorkey((255,255,255))
    star_object.star=pygame.transform.scale(star_object.star,(475,475))

    

    # making the character move
    
    if pressed_keys[K_RIGHT]:
        main_character.char_x += main_character.char_speed * time_passed_seconds
    if pressed_keys[K_LEFT]:
        main_character.char_x -= main_character.char_speed * time_passed_seconds
    if pressed_keys[K_UP]:
        main_character.char_y -= main_character.char_speed * time_passed_seconds
    if pressed_keys[K_DOWN]:
        main_character.char_y += main_character.char_speed * time_passed_seconds          
    # end of the movement
    
    # if character goes out of the screen
            
    if main_character.char_x >= 765:
        main_character.char_x = 765
    if main_character.char_x <= 0:
        main_character.char_x = 0
    if main_character.char_y <= 0:
        main_character.char_y = 0
    if main_character.char_y >= 545:
        main_character.char_y = 545     

    # displaying numbers in the wheel
    
    goal = goalfont.render("The number you need to get is: 12",1,(0,0,0))
    

    zero = myfont.render("0", 1, (56,162,134))
    one = myfont.render("1", 1, (56,162,134))
    two = myfont.render("2", 1, (56,162,134))
    three = myfont.render("3", 1, (56,162,134))
    four = myfont.render("4", 1, (56,162,134))
    five = myfont.render("5", 1, (56,162,134))
    six = myfont.render("6", 1, (56,162,134))
    seven = myfont.render("7", 1, (56,162,134))
    eight = myfont.render("8", 1, (56,162,134))
    nine = myfont.render("9", 1, (56,162,134))
    plus = myfont.render("+", 1 ,(56,162,134))
    
    screen.fill((255,255,255))   
    screen.blit(ledena_doba,(0,0))
    screen.blit(goal,(10,10))
    

    first_wheel.wheel.blit(two, (80, 170))
    first_wheel.wheel.blit(four, (170, 100)) 
    first_wheel.wheel.blit(nine, (275, 100))
    first_wheel.wheel.blit(seven, (380,160))
    first_wheel.wheel.blit(one, (400, 280))
    first_wheel.wheel.blit(eight, (285, 360))
    first_wheel.wheel.blit(plus, (170, 360))
    first_wheel.wheel.blit(five, (80, 285))
    
    
    # Making the wheel rotate (bliting the wheel with same width height & same position)
    rotated_wheel = pygame.transform.rotate(first_wheel.wheel, first_wheel.wheel_rotation)
    w, h = rotated_wheel.get_size()
    wheel_draw_pos = Vector2(first_wheel.wheel_pos.x-w/2, first_wheel.wheel_pos.y-h/2) 
    screen.blit(rotated_wheel, wheel_draw_pos)

    # Making the star rotate (bliting the star with same width height & same position)
    rotated_star = pygame.transform.rotate(star_object.star, star_object.star_rotation)
    w2, h2 = rotated_star.get_size()
    star_draw_pos = Vector2(star_object.star_pos.x-w2/2, star_object.star_pos.y-h2/2) 
    screen.blit(rotated_star, star_draw_pos)
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    
    #wheel rotation
    first_wheel.wheel_rotation += first_wheel.wheel_rotation_direction * first_wheel.wheel_rotation_speed *time_passed_seconds
    #star rotation
    star_object.star_rotation += star_object.star_rotation_direction * star_object.star_rotation_speed *time_passed_seconds
    
    #collision detection
    
    offset_x, offset_y = ((star_object.star_rect.left) - main_character.character_rect.left), ((star_object.star_rect.top) -     main_character.character_rect.top)
    if (main_character.character_mask.overlap(star_object.star_mask, (offset_x, offset_y)) != None):
        print 'Collision Detected!',offset_x,offset_y,star_object.star_rect.left , star_object.star_rect.top
    else:
        print 'None',offset_x,offset_y, star_object.star_rect.left , star_object.star_rect.top, star_object.star_rect.bottom, star_object.star_rect.right
    
    screen.blit(main_character.character,(main_character.char_x,main_character.char_y))
    

    pygame.display.update() 
