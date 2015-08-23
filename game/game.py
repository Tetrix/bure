main_char = "resources/penguin.png"

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,600),0,32)
clock = pygame.time.Clock()

char_x = 100
char_y = 300
char_speed = 200

character = pygame.image.load(main_char).convert()

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
    
    # if character goues out of the screen
            
    if char_x >= 750:
        char_x = 750
    if char_x <= 0:
        char_x = 0
    if char_y <= 0:
        char_y = 0
    if char_y >= 531:
        char_y = 531
        
    screen.fill((255,255,255))            
    screen.blit(character,(char_x,char_y))
    
    
    
    pygame.display.update()
