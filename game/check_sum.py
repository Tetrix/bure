import time
import pygame
from pygame.locals import USEREVENT
from gameobjects.vector2 import Vector2

pygame.init()

lvl_finish_f = 'resources/bugara.png'
game_over_f= 'resources/game-over.png'
go_coordinates=Vector2(200,150)
sumfont = pygame.font.Font("resources/fonts/goall.otf", 60)
screen = pygame.display.set_mode((800,600),0,32)

lvl_finish = pygame.image.load(lvl_finish_f).convert_alpha()
lvl_finish = pygame.transform.scale(lvl_finish,(600,300))
game_over = pygame.image.load(game_over_f).convert_alpha()


def check_sum(numbers_chosen,zbir,suma,level,same_level):
    
    #import game
    for num in numbers_chosen:
        suma += num
    if zbir == suma:
        print "UDZU"
        screen.blit(lvl_finish,(142,100))
        pygame.time.set_timer(USEREVENT+6,20)
        for event in pygame.event.get():
            if event.type == USEREVENT+6:
               time.sleep(1)
               level()
 
    if zbir < suma:
       screen.blit(game_over,go_coordinates)
       pygame.time.set_timer(USEREVENT+7,20)
       for event in pygame.event.get():
          if event.type == USEREVENT+7:
            time.sleep(1)
            same_level()   
    
    

def check_the_sum(numbers_chosen,zbir,suma):
    for num in numbers_chosen:
        suma += num
    summ = sumfont.render(str(suma),1,(0,0,0))
    return summ
