
from math import *

zero = 'resources/digits/0.png'
one = 'resources/digits/1.png'
two = 'resources/digits/2.png'
three = 'resources/digits/3.png'
four = 'resources/digits/4.png'
five = 'resources/digits/5.png'
six = 'resources/digits/6.png'
seven = 'resources/digits/7.png'
eight = 'resources/digits/8.png'
nine = 'resources/digits/9.png'
divide = 'resources/digits/delenje.png'
multiply = 'resources/digits/mnozenje.png'
subtract = 'resources/digits/minus.png'
add = 'resources/digits/plus.png'

import pygame
from gameobjects.vector2 import Vector2


screen = pygame.display.set_mode((800,600),0,32)


class Numbers(object):
    def __init__(self):
        
        self.nula = pygame.image.load(zero).convert()
        self.nula.set_colorkey((0,0,0))
        self.nula_rect = self.nula.get_rect()
        self.nula_mask = pygame.mask.from_surface(self.nula)
            
        self.eden = pygame.image.load(one).convert()
        self.eden.set_colorkey((0,0,0))
        self.eden_rect = self.eden.get_rect()
        self.eden_mask = pygame.mask.from_surface(self.eden)
        
        self.dva = pygame.image.load(two).convert()
        self.dva.set_colorkey((0,0,0))
        self.dva_rect = self.dva.get_rect()
        self.dva_mask = pygame.mask.from_surface(self.dva)
        
        self.tri = pygame.image.load(three).convert()
        self.tri.set_colorkey((0,0,0))
        self.tri_rect = self.tri.get_rect()
        self.tri_mask = pygame.mask.from_surface(self.tri)
        
        self.cetiri = pygame.image.load(four).convert()
        self.cetiri.set_colorkey((0,0,0))
        self.cetiri_rect = self.cetiri.get_rect()
        self.cetiri_mask = pygame.mask.from_surface(self.cetiri)
        
        self.pet = pygame.image.load(five).convert()
        self.pet.set_colorkey((0,0,0))
        self.pet_rect = self.pet.get_rect()
        self.pet_mask = pygame.mask.from_surface(self.pet)
        
        self.sest = pygame.image.load(six).convert()
        self.sest.set_colorkey((0,0,0))
        self.sest_rect = self.sest.get_rect()
        self.sest_mask = pygame.mask.from_surface(self.sest)
        
        self.sedum = pygame.image.load(seven).convert()
        self.sedum.set_colorkey((0,0,0))
        self.sedum_rect = self.sedum.get_rect()
        self.sedum_mask = pygame.mask.from_surface(self.sedum)
        
        self.osum = pygame.image.load(eight).convert()
        self.osum.set_colorkey((0,0,0))
        self.osum_rect = self.osum.get_rect()
        self.osum_mask = pygame.mask.from_surface(self.osum)
        
        self.devet = pygame.image.load(nine).convert()
        self.devet.set_colorkey((0,0,0))
        self.devet_rect = self.devet.get_rect()
        self.devet_mask = pygame.mask.from_surface(self.devet)
        

        
        
            
           
    def num_rotation(self,obj,x,y,acc):
        self.angle = 0.
        self.speed = (2*3.14)/7.2
        self.radius = 150
        self.angle += self.speed * acc
        self.x = cos(self.angle) * self.radius + 420
        self.y = sin(self.angle) * self.radius + 280   
        return self.x,self.y
    def num_rotation2(self,obj,x,y,acc):
        self.angle = 0.
        self.speed = (2*3.14)/7.2
        self.radius = 150
        self.angle -= self.speed * acc
        self.x = cos(self.angle) * self.radius + 420
        self.y = sin(self.angle) * self.radius + 280   
        return self.x,self.y
        
        
    def collision_detection_numbers(self,val,obj1,obj2,object1_rect_left , object1_rect_top , object2_rect_left , object2_rect_top , object1_mask , object2_mask,numbers_chosen ):
        self.offset_x, self.offset_y = int((object1_rect_left - object2_rect_left)), int((object1_rect_top - object2_rect_top))
        if (object2_mask.overlap(object1_mask, (self.offset_x, self.offset_y)) != None):
            print "COLLISION DETECTED"
            if val not in numbers_chosen:
                numbers_chosen.append(val)
                obj1.set_alpha(0)        
                return True
            else: 
                return False
        else: 
            return False
        
    def get_num_vector(self):
        self.eden_pos = Vector2()
        self.dva_pos = Vector2()
        self.tri_pos = Vector2()
        self.cetiri_pos = Vector2()
        self.pet_pos = Vector2()
        self.sest_pos = Vector2()
        self.sedum_pos = Vector2()
        self.osum_pos = Vector2()
        self.devet_pos = Vector2()

    def acceleration(self,acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9):
        self.acceleration_one = 28900000
        self.acceleration_two = 10000000
        self.acceleration_three = 31600000
        self.acceleration_four = 12700000
        self.acceleration_five = 23500000
        self.acceleration_six = 18100000
        self.acceleration_eight = 20800000
        self.acceleration_seven = 26200000
        self.acceleration_nine = 15400000
        
        self.acceleration_list = [self.acceleration_one , self.acceleration_two , self.acceleration_three , self.acceleration_four , self.acceleration_five , self.acceleration_six , self.acceleration_seven , self.acceleration_eight , self.acceleration_nine]


    def collision_flag(self):
        self.one_c=False
        self.two_c=False
        self.three_c=False
        self.four_c=False
        self.five_c=False
        self.six_c=False
        self.seven_c=False
        self.eight_c=False
        self.nine_c=False    

    

        
        
        
        

       
