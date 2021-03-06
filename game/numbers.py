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

one2 = 'resources/digits/11.png'
two2 = 'resources/digits/12.png'
three2 = 'resources/digits/13.png'
four2 = 'resources/digits/14.png'
five2 = 'resources/digits/15.png'
six2 = 'resources/digits/16.png'
seven2 = 'resources/digits/17.png'
eight2 = 'resources/digits/18.png'
nine2 = 'resources/digits/19.png'

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
        
        #from 10

        self.eden2 = pygame.image.load(one2).convert()
        self.eden2.set_colorkey((0,0,0))
        self.eden2_rect = self.eden2.get_rect()
        self.eden2_mask = pygame.mask.from_surface(self.eden2)
        
        self.dva2 = pygame.image.load(two2).convert()
        self.dva2.set_colorkey((0,0,0))
        self.dva2_rect = self.dva2.get_rect()
        self.dva2_mask = pygame.mask.from_surface(self.dva2)
        
        self.tri2 = pygame.image.load(three2).convert()
        self.tri2.set_colorkey((0,0,0))
        self.tri2_rect = self.tri2.get_rect()
        self.tri2_mask = pygame.mask.from_surface(self.tri2)
        
        self.cetiri2 = pygame.image.load(four2).convert()
        self.cetiri2.set_colorkey((0,0,0))
        self.cetiri2_rect = self.cetiri2.get_rect()
        self.cetiri2_mask = pygame.mask.from_surface(self.cetiri2)
        
        self.pet2 = pygame.image.load(five2).convert()
        self.pet2.set_colorkey((0,0,0))
        self.pet2_rect = self.pet2.get_rect()
        self.pet2_mask = pygame.mask.from_surface(self.pet2)
        
        self.sest2 = pygame.image.load(six2).convert()
        self.sest2.set_colorkey((0,0,0))
        self.sest2_rect = self.sest2.get_rect()
        self.sest2_mask = pygame.mask.from_surface(self.sest2)
        
        self.sedum2 = pygame.image.load(seven2).convert()
        self.sedum2.set_colorkey((0,0,0))
        self.sedum2_rect = self.sedum2.get_rect()
        self.sedum2_mask = pygame.mask.from_surface(self.sedum2)
        
        self.osum2 = pygame.image.load(eight2).convert()
        self.osum2.set_colorkey((0,0,0))
        self.osum2_rect = self.osum2.get_rect()
        self.osum2_mask = pygame.mask.from_surface(self.osum2)
        
        self.devet2 = pygame.image.load(nine2).convert()
        self.devet2.set_colorkey((0,0,0))
        self.devet2_rect = self.devet2.get_rect()
        self.devet2_mask = pygame.mask.from_surface(self.devet2)
            
           
    def num_rotation(self,obj,x,y,acc,r,rx,ry):
        self.angle = 0.
        self.speed = (2*3.14)/7.2
        self.radius = r
        self.angle += self.speed * acc
        self.x = cos(self.angle) * self.radius + rx
        self.y = sin(self.angle) * self.radius + ry   
        return self.x,self.y

        
    def collision_detection_numbers(self,val,obj1,obj2,object1_rect_left , object1_rect_top , object2_rect_left , object2_rect_top , object1_mask , object2_mask,numbers_chosen):
        self.offset_x, self.offset_y = int((object1_rect_left - object2_rect_left)), int((object1_rect_top - object2_rect_top))
        if (object2_mask.overlap(object1_mask, (self.offset_x, self.offset_y)) != None):
            print "COLLISION DETECTED"
            
            if val not in numbers_chosen:
                numbers_chosen.append(val)
                obj1.set_alpha(0)
                return True     
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
	
	self.eden2_pos = Vector2()
        self.dva2_pos = Vector2()
        self.tri2_pos = Vector2()
        self.cetiri2_pos = Vector2()
        self.pet2_pos = Vector2()
        self.sest2_pos = Vector2()
        self.sedum2_pos = Vector2()
        self.osum2_pos = Vector2()
        self.devet2_pos = Vector2()

    def acceleration(self,acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9):
        self.acceleration_one = acc1
        self.acceleration_two = acc2
        self.acceleration_three = acc3
        self.acceleration_four = acc4
        self.acceleration_five = acc5
        self.acceleration_six = acc6
        self.acceleration_eight = acc7
        self.acceleration_seven = acc8
        self.acceleration_nine = acc9
        
        self.acceleration_list = [self.acceleration_one , self.acceleration_two , self.acceleration_three , self.acceleration_four , self.acceleration_five , self.acceleration_six , self.acceleration_seven , self.acceleration_eight , self.acceleration_nine]
    def acceleration2(self,accc1,accc2,accc3,accc4,accc5,accc6,accc7,accc8,accc9):
        self.acceleration_one2 = accc1
        self.acceleration_two2 = accc2
        self.acceleration_three2 = accc3
        self.acceleration_four2 = accc4
        self.acceleration_five2 = accc5
        self.acceleration_six2 = accc6
        self.acceleration_eight2 = accc7
        self.acceleration_seven2 = accc8
        self.acceleration_nine2 = accc9
        
        self.acceleration_list2 = [self.acceleration_one2 , self.acceleration_two2 , self.acceleration_three2 , self.acceleration_four2 , self.acceleration_five2 , self.acceleration_six2 , self.acceleration_seven2 , self.acceleration_eight2 , self.acceleration_nine2]

    
 

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
	
	self.one2_c=False
        self.two2_c=False
        self.three2_c=False
        self.four2_c=False
        self.five2_c=False
        self.six2_c=False
        self.seven2_c=False
        self.eight2_c=False
        self.nine2_c=False     

    
    
       
