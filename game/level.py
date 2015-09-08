background = "resources/ledena_doba.jpg"
import pygame
import os
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from wheel import *
from numbers import *
from star import * 
from character import *
import check_sum

window_x = 270
window_y = 80

#Window positioning
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (window_x,window_y)
pygame.init()
screen = pygame.display.set_mode((800,600),0,32)

#Loading fonts
myfont = pygame.font.Font("resources/fonts/gentium.ttf", 40)
goalfont = pygame.font.Font("resources/fonts/goall.otf", 30)
levelfont = pygame.font.Font("resources/fonts/goall.otf", 30)
levelnumber = pygame.font.Font("resources/fonts/goall.otf", 30)
sumfont = pygame.font.Font("resources/fonts/goall.otf", 30)
class Level(object):
    def __init__(self,background,zbir,level_num):
        
        #Background
        self.background_img = pygame.image.load(background).convert()
        self.background_img = pygame.transform.scale(self.background_img,(800,600))
       
      
    
        self.goal = goalfont.render("The number you need to get is: ",1,(0,0,0))
        self.level_text = levelfont.render("Level: ",1,(0,0,0))
        self.level_number = levelnumber.render(str(level_num), 1, (0,0,0))
        self.zbiro = goalfont.render(str(zbir), 1, (0,0,0))
        self.num_str= goalfont.render("|  1 2 3 4 5 6 7 8 9 ", 1, (239,239,239))
        

    def blit_main(self):
        screen.blit(self.background_img,(0,0))
        screen.blit(self.goal,(10,10))
        screen.blit(self.zbiro,(435,10))  
        screen.blit(self.num_str,(480,10))
        screen.blit(self.level_text,(10,40))
        screen.blit(self.level_number,(95,40))   

    def loading_objects(self,acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9):

         
        #making instance of class Wheel
        self.first_wheel = Wheel()
        self.first_wheel.wheel_properties()

        #making instance of class Star
        self.star_object = Star()
        self.star_object.star_properties()
        self.star_object.image_marking()

        #making instance of class Numbers
        self.num_obj = Numbers()
        self.num_obj.get_num_vector()
        self.num_obj.acceleration(acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9)
        self.num_obj.collision_flag()
             

        #making instance of class Character
        self.main_character = Character()
       
   

    def wheel_star_rotation(self,x1,x2):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == self.first_wheel.wheel_rotate:  
                self.first_wheel.wheel_rotation_direction=+x1
                self.star_object.star_rotation_direction=+x2
            #making the star changing color
            if event.type == self.star_object.star_event:
                self.star_object.star_file=self.star_object.star_file
            if event.type == self.star_object.star2_event:
                self.star_object.star_file=self.star_object.star2_file
            if event.type == self.star_object.star3_event:
                self.star_object.star_file=self.star_object.star3_file


    def numbers_rotated(self,list_length,acc):
        #number rotation
        self.num_obj.eden_pos.x,self.num_obj.eden_pos.y = self.num_obj.num_rotation(self.num_obj.eden,self.num_obj.eden_pos.x,self.num_obj.eden_pos.y,self.num_obj.acceleration_list[0])
        screen.blit(self.num_obj.eden,(self.num_obj.eden_pos.x,self.num_obj.eden_pos.y))
        
        self.num_obj.dva_pos.x,self.num_obj.dva_pos.y = self.num_obj.num_rotation(self.num_obj.dva,self.num_obj.dva_pos.x,self.num_obj.dva_pos.y,self.num_obj.acceleration_list[1])
        screen.blit(self.num_obj.dva,(self.num_obj.dva_pos.x,self.num_obj.dva_pos.y))
        
        self.num_obj.tri_pos.x,self.num_obj.tri_pos.y = self.num_obj.num_rotation(self.num_obj.tri,self.num_obj.tri_pos.x,self.num_obj.tri_pos.y,self.num_obj.acceleration_list[2])
        screen.blit(self.num_obj.tri,(self.num_obj.tri_pos.x,self.num_obj.tri_pos.y))
        
        self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y = self.num_obj.num_rotation(self.num_obj.cetiri,self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y,self.num_obj.acceleration_list[3])
        screen.blit(self.num_obj.cetiri,(self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y))
        
        self.num_obj.pet_pos.x,self.num_obj.pet_pos.y = self.num_obj.num_rotation(self.num_obj.pet,self.num_obj.pet_pos.x,self.num_obj.pet_pos.y,self.num_obj.acceleration_list[4])
        screen.blit(self.num_obj.pet,(self.num_obj.pet_pos.x,self.num_obj.pet_pos.y))
        
        self.num_obj.sest_pos.x,self.num_obj.sest_pos.y = self.num_obj.num_rotation(self.num_obj.sest,self.num_obj.sest_pos.x,self.num_obj.sest_pos.y,self.num_obj.acceleration_list[5])
        screen.blit(self.num_obj.sest,(self.num_obj.sest_pos.x,self.num_obj.sest_pos.y))
        
        self.num_obj.sedum_pos.x,self.num_obj.sedum_pos.y = self.num_obj.num_rotation(self.num_obj.sedum,self.num_obj.sedum_pos.x,self.num_obj.sedum_pos.y,self.num_obj.acceleration_list[6])
        screen.blit(self.num_obj.sedum,(self.num_obj.sedum_pos.x,self.num_obj.sedum_pos.y))
        
        self.num_obj.osum_pos.x,self.num_obj.osum_pos.y = self.num_obj.num_rotation(self.num_obj.osum,self.num_obj.osum_pos.x,self.num_obj.osum_pos.y,self.num_obj.acceleration_list[7])
        screen.blit(self.num_obj.osum,(self.num_obj.osum_pos.x,self.num_obj.osum_pos.y))
        
        self.num_obj.devet_pos.x,self.num_obj.devet_pos.y = self.num_obj.num_rotation(self.num_obj.devet,self.num_obj.devet_pos.x,self.num_obj.devet_pos.y,self.num_obj.acceleration_list[8])
        screen.blit(self.num_obj.devet,(self.num_obj.devet_pos.x,self.num_obj.devet_pos.y))

        for i in range(list_length):
           self.num_obj.acceleration_list[i]+=acc


    def numbers_rotated2(self,list_length,acc):
        #number rotation
        self.num_obj.eden_pos.x,self.num_obj.eden_pos.y = self.num_obj.num_rotation2(self.num_obj.eden,self.num_obj.eden_pos.x,self.num_obj.eden_pos.y,self.num_obj.acceleration_list[0])
        screen.blit(self.num_obj.eden,(self.num_obj.eden_pos.x,self.num_obj.eden_pos.y))
        
        self.num_obj.dva_pos.x,self.num_obj.dva_pos.y = self.num_obj.num_rotation2(self.num_obj.dva,self.num_obj.dva_pos.x,self.num_obj.dva_pos.y,self.num_obj.acceleration_list[1])
        screen.blit(self.num_obj.dva,(self.num_obj.dva_pos.x,self.num_obj.dva_pos.y))
        
        self.num_obj.tri_pos.x,self.num_obj.tri_pos.y = self.num_obj.num_rotation2(self.num_obj.tri,self.num_obj.tri_pos.x,self.num_obj.tri_pos.y,self.num_obj.acceleration_list[2])
        screen.blit(self.num_obj.tri,(self.num_obj.tri_pos.x,self.num_obj.tri_pos.y))
        
        self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y = self.num_obj.num_rotation2(self.num_obj.cetiri,self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y,self.num_obj.acceleration_list[3])
        screen.blit(self.num_obj.cetiri,(self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y))
        
        self.num_obj.pet_pos.x,self.num_obj.pet_pos.y = self.num_obj.num_rotation2(self.num_obj.pet,self.num_obj.pet_pos.x,self.num_obj.pet_pos.y,self.num_obj.acceleration_list[4])
        screen.blit(self.num_obj.pet,(self.num_obj.pet_pos.x,self.num_obj.pet_pos.y))
        
        self.num_obj.sest_pos.x,self.num_obj.sest_pos.y = self.num_obj.num_rotation2(self.num_obj.sest,self.num_obj.sest_pos.x,self.num_obj.sest_pos.y,self.num_obj.acceleration_list[5])
        screen.blit(self.num_obj.sest,(self.num_obj.sest_pos.x,self.num_obj.sest_pos.y))
        
        self.num_obj.sedum_pos.x,self.num_obj.sedum_pos.y = self.num_obj.num_rotation2(self.num_obj.sedum,self.num_obj.sedum_pos.x,self.num_obj.sedum_pos.y,self.num_obj.acceleration_list[6])
        screen.blit(self.num_obj.sedum,(self.num_obj.sedum_pos.x,self.num_obj.sedum_pos.y))
        
        self.num_obj.osum_pos.x,self.num_obj.osum_pos.y = self.num_obj.num_rotation2(self.num_obj.osum,self.num_obj.osum_pos.x,self.num_obj.osum_pos.y,self.num_obj.acceleration_list[7])
        screen.blit(self.num_obj.osum,(self.num_obj.osum_pos.x,self.num_obj.osum_pos.y))
        
        self.num_obj.devet_pos.x,self.num_obj.devet_pos.y = self.num_obj.num_rotation2(self.num_obj.devet,self.num_obj.devet_pos.x,self.num_obj.devet_pos.y,self.num_obj.acceleration_list[8])
        screen.blit(self.num_obj.devet,(self.num_obj.devet_pos.x,self.num_obj.devet_pos.y))


        for i in range(list_length):
           self.num_obj.acceleration_list[i]+=acc

    def print_text_sum(self):
        suma_txt=sumfont.render("The sum",1,(0,0,0))
        #suma=check_sum.check_sum(numbers_chosen,20,suma)
        screen.blit(suma_txt,(60,470))
        #screen.blit(suma,(100,400))


