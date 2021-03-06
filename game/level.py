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
    def __init__(self,background,zbir,level_num,font_color1,font_color2):
        
        #Background
        self.background_img = pygame.image.load(background).convert()
        self.background_img = pygame.transform.scale(self.background_img,(800,600))
       
      
    
        self.goal = goalfont.render("The number you need to get is: ",1,font_color1)
        self.level_text = levelfont.render("Level: ",1,font_color1)
        self.level_number = levelnumber.render(str(level_num), 1, font_color1)
        self.zbiro = goalfont.render(str(zbir), 1, font_color1)
        self.num_str= goalfont.render("|  1 2 3 4 5 6 7 8 9 11 12 13 14 15 16 17 18 19 |", 1, font_color2)
        self.num_str2=goalfont.render("|  1 2 3 4 5 6 7 8 9 ", 1, font_color2)

    def blit_main(self,arg):
        screen.blit(self.background_img,(0,0))
        screen.blit(self.goal,(10,10))
        screen.blit(self.zbiro,(435,10))
        if arg==True:  
           screen.blit(self.num_str,(50,60))
	if arg==False:
           screen.blit(self.num_str2,(50,60))
        screen.blit(self.level_text,(650,10))
        screen.blit(self.level_number,(735,10))   

    def loading_objects(self,acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9,accc1,accc2,accc3,accc4,accc5,accc6,accc7,accc8,accc9):

        #making instance of class Numbers
        self.num_obj = Numbers()
        self.num_obj.get_num_vector()
        self.num_obj.acceleration(acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9)
        self.num_obj.collision_flag()
        self.num_obj.acceleration2(accc1,accc2,accc3,accc4,accc5,accc6,accc7,accc8,accc9)     
    def load_char(self):
        #making instance of class Character
        self.main_character = Character()
    
    def wheel_load(self,wheel_f,size_w,size_h,x,y):
   	#making instance of class Wheel
        self.first_wheel = Wheel(wheel_f,size_w,size_h)
        self.first_wheel.wheel_properties(x,y)
    def wheel_load2(self,wheel_f,size_w,size_h,x,y):
   	#making instance of class Wheel
        self.second_wheel = Wheel(wheel_f,size_w,size_h)
        self.second_wheel.wheel_properties(x,y)
    def star_load(self,star_f,w,h,x,y):
   	#making instance of class Star
        self.star_object = Star()
        self.star_object.star_properties()
        self.star_object.image_marking(star_f,w,h,x,y)
    def star_load2(self,star_f,w,h,x,y):
   	#making instance of class Star
        self.star_object2 = Star()
        self.star_object2.star_properties()
        self.star_object2.image_marking(star_f,w,h,x,y)
   
   
    def wheel_star_rotation(self,x1,x2):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == self.first_wheel.wheel_rotate:  
                self.first_wheel.wheel_rotation_direction=+x1
                self.star_object.star_rotation_direction=+x2

            


    def wheel_star_rotation2(self,x1,x2,star,star2,wheel,wheel2,y1,y2):
     

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == wheel.wheel_rotate:  
                wheel.wheel_rotation_direction=+x1
                star.star_rotation_direction=+x2
                if star2!=None:
                        star2.star_rotation_direction=+y1
                if wheel2!=None:
                        wheel2.wheel_rotation_direction=+y2

          



    def numbers_rotated(self):
        #number rotation
        self.num_obj.eden_pos.x,self.num_obj.eden_pos.y = self.num_obj.num_rotation(self.num_obj.eden,self.num_obj.eden_pos.x,self.num_obj.eden_pos.y,self.num_obj.acceleration_list[0],150,420,280)
        screen.blit(self.num_obj.eden,(self.num_obj.eden_pos.x,self.num_obj.eden_pos.y))
        
        self.num_obj.dva_pos.x,self.num_obj.dva_pos.y = self.num_obj.num_rotation(self.num_obj.dva,self.num_obj.dva_pos.x,self.num_obj.dva_pos.y,self.num_obj.acceleration_list[1],150,420,280)
        screen.blit(self.num_obj.dva,(self.num_obj.dva_pos.x,self.num_obj.dva_pos.y))
        
        self.num_obj.tri_pos.x,self.num_obj.tri_pos.y = self.num_obj.num_rotation(self.num_obj.tri,self.num_obj.tri_pos.x,self.num_obj.tri_pos.y,self.num_obj.acceleration_list[2],150,420,280)
        screen.blit(self.num_obj.tri,(self.num_obj.tri_pos.x,self.num_obj.tri_pos.y))
        
        self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y = self.num_obj.num_rotation(self.num_obj.cetiri,self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y,self.num_obj.acceleration_list[3],150,420,280)
        screen.blit(self.num_obj.cetiri,(self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y))
        
        self.num_obj.pet_pos.x,self.num_obj.pet_pos.y = self.num_obj.num_rotation(self.num_obj.pet,self.num_obj.pet_pos.x,self.num_obj.pet_pos.y,self.num_obj.acceleration_list[4],150,420,280)
        screen.blit(self.num_obj.pet,(self.num_obj.pet_pos.x,self.num_obj.pet_pos.y))
        
        self.num_obj.sest_pos.x,self.num_obj.sest_pos.y = self.num_obj.num_rotation(self.num_obj.sest,self.num_obj.sest_pos.x,self.num_obj.sest_pos.y,self.num_obj.acceleration_list[5],150,420,280)
        screen.blit(self.num_obj.sest,(self.num_obj.sest_pos.x,self.num_obj.sest_pos.y))
        
        self.num_obj.sedum_pos.x,self.num_obj.sedum_pos.y = self.num_obj.num_rotation(self.num_obj.sedum,self.num_obj.sedum_pos.x,self.num_obj.sedum_pos.y,self.num_obj.acceleration_list[6],150,420,280)
        screen.blit(self.num_obj.sedum,(self.num_obj.sedum_pos.x,self.num_obj.sedum_pos.y))
        
        self.num_obj.osum_pos.x,self.num_obj.osum_pos.y = self.num_obj.num_rotation(self.num_obj.osum,self.num_obj.osum_pos.x,self.num_obj.osum_pos.y,self.num_obj.acceleration_list[7],150,420,280)
        screen.blit(self.num_obj.osum,(self.num_obj.osum_pos.x,self.num_obj.osum_pos.y))
        
        self.num_obj.devet_pos.x,self.num_obj.devet_pos.y = self.num_obj.num_rotation(self.num_obj.devet,self.num_obj.devet_pos.x,self.num_obj.devet_pos.y,self.num_obj.acceleration_list[8],150,420,280)
        screen.blit(self.num_obj.devet,(self.num_obj.devet_pos.x,self.num_obj.devet_pos.y))

        
        
	
    def numbers1_rotated(self,num_obj,obj,pos,obj2,pos2,obj3,pos3):\

        self.num_obj.dva_pos.x,self.num_obj.dva_pos.y = self.num_obj.num_rotation(self.num_obj.dva,self.num_obj.dva_pos.x,self.num_obj.dva_pos.y,self.num_obj.acceleration_list[1],110,235,340)
        screen.blit(self.num_obj.dva,(self.num_obj.dva_pos.x,self.num_obj.dva_pos.y))
        
        pos.x,pos.y = num_obj.num_rotation(obj,pos.x,pos.y,num_obj.acceleration_list[2],110,235,340)
        screen.blit(obj,(pos.x,pos.y))

        self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y = self.num_obj.num_rotation(self.num_obj.cetiri,self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y,self.num_obj.acceleration_list[3],110,235,340)
        screen.blit(self.num_obj.cetiri,(self.num_obj.cetiri_pos.x,self.num_obj.cetiri_pos.y))
        
        self.num_obj.pet_pos.x,self.num_obj.pet_pos.y = self.num_obj.num_rotation(self.num_obj.pet,self.num_obj.pet_pos.x,self.num_obj.pet_pos.y,self.num_obj.acceleration_list[4],110,235,340)
        screen.blit(self.num_obj.pet,(self.num_obj.pet_pos.x,self.num_obj.pet_pos.y))
        
	pos2.x,pos2.y = num_obj.num_rotation(obj2,pos2.x,pos2.y,num_obj.acceleration_list[6],110,235,340)
        screen.blit(obj2,(pos2.x,pos2.y))
        
        self.num_obj.osum_pos.x,self.num_obj.osum_pos.y = self.num_obj.num_rotation(self.num_obj.osum,self.num_obj.osum_pos.x,self.num_obj.osum_pos.y,self.num_obj.acceleration_list[7],110,235,340)
        screen.blit(self.num_obj.osum,(self.num_obj.osum_pos.x,self.num_obj.osum_pos.y))
        
	pos3.x,pos3.y = num_obj.num_rotation(obj3,pos3.x,pos3.y,num_obj.acceleration_list[8],110,235,340)
        screen.blit(obj3,(pos3.x,pos3.y))

     

    def numbers2_rotated(self,num_obj,obj,pos,obj2,pos2,obj3,pos3):
        #number rotation
        pos.x,pos.y = num_obj.num_rotation(obj,pos.x,pos.y,num_obj.acceleration_list2[0],70,600,232)
        screen.blit(obj,(pos.x,pos.y))
        
        self.num_obj.dva2_pos.x,self.num_obj.dva2_pos.y = self.num_obj.num_rotation(self.num_obj.dva2,self.num_obj.dva2_pos.x,self.num_obj.dva2_pos.y,self.num_obj.acceleration_list2[1],70,600,232)
        screen.blit(self.num_obj.dva2,(self.num_obj.dva2_pos.x,self.num_obj.dva2_pos.y))
        
        pos2.x,pos2.y = num_obj.num_rotation(obj2,pos2.x,pos2.y,num_obj.acceleration_list2[3],70,600,232)
        screen.blit(obj2,(pos2.x,pos2.y))
        
        pos3.x,pos3.y = num_obj.num_rotation(obj3,pos3.x,pos3.y,num_obj.acceleration_list2[5],70,600,232)
        screen.blit(obj3,(pos3.x,pos3.y))
        
        self.num_obj.devet2_pos.x,self.num_obj.devet2_pos.y = self.num_obj.num_rotation(self.num_obj.devet2,self.num_obj.devet2_pos.x,self.num_obj.devet2_pos.y,self.num_obj.acceleration_list2[8],70,600,232)
        screen.blit(self.num_obj.devet2,(self.num_obj.devet2_pos.x,self.num_obj.devet2_pos.y))


        

    def print_text_sum(self,color):
        suma_txt=sumfont.render("The sum",1,color)
        #suma=check_sum.check_sum(numbers_chosen,20,suma)
        screen.blit(suma_txt,(650,470))
        #screen.blit(suma,(100,400))


