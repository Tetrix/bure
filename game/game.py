main_char = "resources/penguin.png"
background = "resources/ledena_doba.jpg"
wheel_file= "resources/circle.png"
star_file="resources/star.png"

xx = 270
yy = 80

import pygame
from pygame.locals import *
from sys import exit
import os
import time
from gameobjects.vector2 import Vector2
from math import *
pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (xx,yy)
screen = pygame.display.set_mode((800,600),0,32)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)



char_x = 100
char_y = 300
char_speed = 200
wheel_speed=500
sprite_rotation_speed = 360
sprite_speed=300


wheel_x=200
wheel_y=50

myfont = pygame.font.SysFont("resources/Attic.ttf", 40)
goalfont = pygame.font.Font("resources/Attic.ttf", 30)



character = pygame.image.load(main_char).convert_alpha()
character=pygame.transform.scale(character,(35,55))
wheel=pygame.image.load(wheel_file).convert_alpha()
star=pygame.image.load(star_file).convert_alpha()
star=pygame.transform.scale(star,(550,550))



wheel_x=200
wheel_y=50

wheel_rotate=pygame.USEREVENT + 1
pygame.time.set_timer(wheel_rotate,wheel_speed)


sprite_pos = Vector2(450, 300)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = -20. # Degrees per second
sprite=wheel

sprite_pos2 = Vector2(447, 302)
sprite_speed2 = 300.
sprite_rotation2 = 0.
sprite_rotation_speed2 = -20. # Degrees per second
sprite2=star

rotation_direction = 0.
rotation_direction2 =0.



ledena_doba = pygame.image.load(background).convert()
ledena_doba = pygame.transform.scale(ledena_doba,(800,600))



while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == wheel_rotate:
            rotation_direction=+1.0
            rotation_direction2=+1.0    

    
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

    # displaying numbers in the wheel
    
    goal = goalfont.render("The number you need to get is: 12",1,(0,0,0))
    

    zero = myfont.render("0", 1, (56,162,130))
    one = myfont.render("1", 1, (56,162,131))
    two = myfont.render("2", 1, (56,162,132))
    three = myfont.render("3", 1, (56,162,133))
    four = myfont.render("4", 1, (56,162,134))
    five = myfont.render("5", 1, (56,162,135))
    six = myfont.render("6", 1, (56,162,136))
    seven = myfont.render("7", 1, (56,162,137))
    eight = myfont.render("8", 1, (56,162,138))
    nine = myfont.render("9", 1, (56,162,139))
    plus = myfont.render("+", 1 ,(56,162,140))
    
    screen.fill((255,255,255))   
    screen.blit(ledena_doba,(0,0))
    screen.blit(wheel,(wheel_x,wheel_y))            
    screen.blit(goal,(10,10))
    
    wheel.blit(two, (80, 170))
    wheel.blit(four, (170, 100)) 
    wheel.blit(nine, (275, 100))
    wheel.blit(seven, (360,180))
    wheel.blit(one, (370, 300))
    wheel.blit(eight, (270, 360))
    wheel.blit(plus, (170, 360))
    wheel.blit(five, (80, 285))
    
    screen.blit(character,(char_x,char_y))

    

    
    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    sprite_draw_pos = Vector2(sprite_pos.x-w/2, sprite_pos.y-h/2) 
    screen.blit(rotated_sprite, sprite_draw_pos)
    rotated_sprite2 = pygame.transform.rotate(sprite2, sprite_rotation2)
    w2, h2 = rotated_sprite2.get_size()
    sprite_draw_pos2 = Vector2(sprite_pos2.x-w2/2, sprite_pos2.y-h2/2) 
    screen.blit(rotated_sprite2, sprite_draw_pos2)
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    sprite_rotation += rotation_direction * sprite_rotation_speed *time_passed_seconds
    sprite_rotation2 += rotation_direction2 * sprite_rotation_speed2 *time_passed_seconds
    
    screen.blit(character,(char_x,char_y))
    

    pygame.display.update()
    
    
    
    
    
    
