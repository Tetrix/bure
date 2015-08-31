bure_f= "resources/bure.png"
game_over_f= 'resources/game-over.png'
numbers_chosen = []
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
from numbers import Numbers
from level import *


pygame.init()
bure = pygame.image.load(bure_f)
pygame.display.set_icon(bure)

def collision_detection(obj2,object1_rect_left , object1_rect_top , object2_rect_left , object2_rect_top , object1_mask , object2_mask ):
    offset_x, offset_y = int((object1_rect_left - object2_rect_left)), int((object1_rect_top - object2_rect_top))
    if (object2_mask.overlap(object1_mask, (offset_x, offset_y)) != None):
       
        screen.blit(game_over,go_coordinates)
        pygame.time.set_timer(USEREVENT+1,1)
     
         
        for event in pygame.event.get():
           if event.type == USEREVENT+1:
            time.sleep(1)
            main()
        


def collision_detection_numbers(val,obj1,obj2,object1_rect_left , object1_rect_top , object2_rect_left , object2_rect_top , object1_mask , object2_mask,numbers_chosen ):
    offset_x, offset_y = int((object1_rect_left - object2_rect_left)), int((object1_rect_top - object2_rect_top))
    if (object2_mask.overlap(object1_mask, (offset_x, offset_y)) != None):
        print "COLLISION DETECTED"
        if val not in numbers_chosen:
            numbers_chosen.append(val)
            obj1.set_alpha(0)        
            return True
        else: 
            return False
    else: 
       return False


def check_sum(numbers_chosen,zbir):
    suma = 0
    for num in numbers_chosen:
        suma += num
    if zbir == suma:
        print "UDZU"

#function for number rotation        
def num_rotation(obj,x,y,acc):
    angle = 0.
    speed = (2*3.14)/7.2
    radius = 150
    angle += speed * acc
    x = cos(angle) * radius + 420
    y = sin(angle) * radius + 280  
    screen.blit(obj,(x,y)) 
    return x,y

window_x = 270
window_y = 80

#making instance of class level
level_one = Level()


#Window positioning
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (window_x,window_y)

pygame.display.set_caption('BURE')

#Loading fonts
myfont = pygame.font.Font("resources/fonts/gentium.ttf", 40)
goalfont = pygame.font.Font("resources/fonts/ubuntu.ttf", 30)


#screen = pygame.display.set_mode((800,600),0,32)
game_over = pygame.image.load(game_over_f).convert_alpha()
go_coordinates=Vector2(200,150)

def main():
 clock = pygame.time.Clock()
 pygame.mouse.set_visible(0)

 goal = goalfont.render("The number you need to get is: ",1,(0,0,0))
 zbiro = goalfont.render("20", 1, (0,0,0))
 num_str= goalfont.render(" 1 2 3 4 5 6 7 8 9 ", 1, (239,239,239))

#making instance of class Character
 main_character = Character()
 main_character.properties()

#making instance of class Wheel
 first_wheel = Wheel()
 first_wheel.wheel_properties()

#making instance of class Star
 star_object = Star()
 star_object.star_properties()

 #making instance of class Numbers
 zero_obj = Numbers()
 dva_pos = Vector2(80,170)
 cetiri_pos = Vector2(170,100)
 devet_pos = Vector2(275, 100)   
 sest_pos = Vector2(170, 360)
 osum_pos = Vector2(285, 360)
 pet_pos = Vector2(80, 285)
 sedum_pos = Vector2(380,160)
 eden_pos = Vector2(400, 280)
 tri_pos = Vector2(400, 100)

 

 #the sum
 zbir = 20
 zbirr = "20"

#main loop
 def main_loop():
   
    acceleration_two = 10000000
    acceleration_four = 12700000
    acceleration_nine = 15400000
    acceleration_six = 18100000
    acceleration_eight = 20800000
    acceleration_five = 23500000
    acceleration_seven = 26200000
    acceleration_one = 28900000
    acceleration_three = 31600000
    one_c=False
    two_c=False
    three_c=False
    four_c=False
    five_c=False
    six_c=False
    seven_c=False
    eight_c=False
    nine_c=False    

    while True: 
   
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            
            #rotate the wheel and the star
            if event.type == first_wheel.wheel_rotate:  
                first_wheel.wheel_rotation_direction=+1.0
                star_object.star_rotation_direction=+1.0  
            
        
            
            #making the star changing color
            if event.type == star_object.star_event:
                star_object.star_file=star_object.star_file
            if event.type == star_object.star2_event:
                star_object.star_file=star_object.star2_file
            if event.type == star_object.star3_event:
                star_object.star_file=star_object.star3_file
                   
        star_object.star=pygame.image.load(star_object.star_file).convert()
        star_object.star = pygame.transform.scale(star_object.star,(470,470))
        star_object.star.set_colorkey((255,255,255))
        star_object.star_mask = pygame.mask.from_surface(star_object.star)
        star_object.star_rect = star_object.star.get_rect()

        main_character.character_rect.topleft = (main_character.char_x,main_character.char_y)
        #end of star changing color      
         

        pressed_keys = pygame.key.get_pressed()

        #setting the fps
        time_passed = clock.tick(50)
        time_passed_seconds = time_passed / 1000.0

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


           
        
        
        #rotating the wheel and the star
        first_wheel.rotating_wheel(first_wheel.wheel,first_wheel.wheel_rotation,first_wheel.wheel_pos.x,first_wheel.wheel_pos.y)
        star_object.rotating_star(star_object.star,star_object.star_rotation,star_object.star_pos.x,star_object.star_pos.y)

  
        screen.fill((0,0,0))   
        screen.blit(level_one.ledena_doba,(0,0))
        screen.blit(goal,(10,10))
        screen.blit(zbiro,(355,10))
        screen.blit(num_str,(400,10))        
        screen.blit(first_wheel.rotated_wheel, first_wheel.wheel_draw_pos)
        screen.blit(star_object.rotated_star, star_object.star_draw_pos)
        
        #number rotation
        dva_pos.x,dva_pos.y = num_rotation(zero_obj.dva,dva_pos.x,dva_pos.y,acceleration_two)
        acceleration_two += 0.0320

        cetiri_pos.x,cetiri_pos.y = num_rotation(zero_obj.cetiri,cetiri_pos.x,cetiri_pos.y,acceleration_four)
        acceleration_four += 0.0320

        devet_pos.x,devet_pos.y = num_rotation(zero_obj.devet,devet_pos.x,devet_pos.y,acceleration_nine)
        acceleration_nine += 0.0320

        sest_pos.x,sest_pos.y = num_rotation(zero_obj.sest,sest_pos.x,sest_pos.y,acceleration_six)
        acceleration_six += 0.0320

        osum_pos.x,osum_pos.y = num_rotation(zero_obj.osum,osum_pos.x,osum_pos.y,acceleration_eight)
        acceleration_eight += 0.0320

        pet_pos.x,pet_pos.y = num_rotation(zero_obj.pet,pet_pos.x,pet_pos.y,acceleration_five)
        acceleration_five += 0.0320

        sedum_pos.x,sedum_pos.y = num_rotation(zero_obj.sedum,sedum_pos.x,sedum_pos.y,acceleration_seven)
        acceleration_seven += 0.0320

        eden_pos.x,eden_pos.y = num_rotation(zero_obj.eden,eden_pos.x,eden_pos.y,acceleration_one)
        acceleration_one += 0.0320

        tri_pos.x,tri_pos.y = num_rotation(zero_obj.tri,tri_pos.x,tri_pos.y,acceleration_three)
        acceleration_three += 0.0320
        
       
        #wheel rotation
        first_wheel.wheel_rotation += first_wheel.wheel_rotation_direction * first_wheel.wheel_rotation_speed *time_passed_seconds
        #star rotation
        star_object.star_rotation += star_object.star_rotation_direction * star_object.star_rotation_speed *time_passed_seconds
        

        star_object.star_rect.topleft=(star_object.star_draw_pos.x,star_object.star_draw_pos.y)
        
        #creating a new mask
        star_object.star_mask = pygame.mask.from_surface(star_object.rotated_star)
           
        screen.blit(main_character.character,(main_character.char_x,main_character.char_y))
        
        #collision detection for the character and the star
        #collision_detection(main_character.character,star_object.star_rect.left , star_object.star_rect.top , main_character.character_rect.left , main_character.character_rect.top , star_object.star_mask , main_character.character_mask)
        
        
        #collision detection for the number one
        coli_1=collision_detection_numbers(1,zero_obj.eden,main_character.character,eden_pos.x , eden_pos.y , main_character.character_rect.left , main_character.character_rect.top , zero_obj.eden_mask , main_character.character_mask,numbers_chosen)
        if len(numbers_chosen)>0 and coli_1==True:
           one=str(numbers_chosen[-1])
           num1 = goalfont.render(one, 1, (0,0,0))
           one_c=True
        if(one_c==True):
           screen.blit(num1,(406,10))
 
        #collision detection for the number two
        coli_2=collision_detection_numbers(2,zero_obj.dva,main_character.character,dva_pos.x , dva_pos.y , main_character.character_rect.left , main_character.character_rect.top , zero_obj.dva_mask , main_character.character_mask,numbers_chosen)
        if len(numbers_chosen)>0 and coli_2==True:
           two=str(numbers_chosen[-1])
           num2 = goalfont.render(two, 1, (0,0,0))
           two_c=True
        if(two_c==True):
           screen.blit(num2,(425,10))
           
        #collision detection for the number three
        coli_3=collision_detection_numbers(3,zero_obj.tri,main_character.character,tri_pos.x , tri_pos.y , main_character.character_rect.left , main_character.character_rect.top , zero_obj.tri_mask , main_character.character_mask,numbers_chosen)   
        if len(numbers_chosen)>0 and coli_3==True:
           three=str(numbers_chosen[-1])
           num3 = goalfont.render(three, 1, (0,0,0))
           three_c=True
        if(three_c==True):
           screen.blit(num3,(444,10))

        #collision detection for the number four
        coli_4=collision_detection_numbers(4,zero_obj.cetiri,main_character.character,cetiri_pos.x , cetiri_pos.y , main_character.character_rect.left , main_character.character_rect.top , zero_obj.cetiri_mask , main_character.character_mask,numbers_chosen)
        if len(numbers_chosen)>0 and coli_4==True:
           four=str(numbers_chosen[-1])
           num4 = goalfont.render(four, 1, (0,0,0))
           four_c=True
        if(four_c==True):
           screen.blit(num4,(463,10))
         
        #collision detection for the number five
        coli_5=collision_detection_numbers(5,zero_obj.pet,main_character.character,pet_pos.x , pet_pos.y , main_character.character_rect.left , main_character.character_rect.top , zero_obj.pet_mask , main_character.character_mask,numbers_chosen)  
        if len(numbers_chosen)>0 and coli_5==True:
           five=str(numbers_chosen[-1])
           num5 = goalfont.render(five, 1, (0,0,0))
           five_c=True
        if(five_c==True):
           screen.blit(num5,(482,10)) 

        #collision detection for the number six
        coli_6=collision_detection_numbers(6,zero_obj.sest,main_character.character,sest_pos.x , sest_pos.y , main_character.character_rect.left , main_character.character_rect.top , zero_obj.sest_mask , main_character.character_mask,numbers_chosen)
        if len(numbers_chosen)>0 and coli_6==True:
           six=str(numbers_chosen[-1])
           num6 = goalfont.render(six, 1, (0,0,0))
           six_c=True
        if(six_c==True):
           screen.blit(num6,(501,10))

        #collision detection for the number seven
        coli_7=collision_detection_numbers(7,zero_obj.sedum,main_character.character,sedum_pos.x , sedum_pos.y , main_character.character_rect.left , main_character.character_rect.top , zero_obj.sedum_mask , main_character.character_mask,numbers_chosen)
        if len(numbers_chosen)>0 and coli_7==True:
           seven=str(numbers_chosen[-1])
           num7 = goalfont.render(seven, 1, (0,0,0))
           seven_c=True
        if(seven_c==True):
           screen.blit(num7,(520,10))
        #collision detection for the number eight
        coli_8=collision_detection_numbers(8,zero_obj.osum,main_character.character,osum_pos.x , osum_pos.y , main_character.character_rect.left , main_character.character_rect.top , zero_obj.osum_mask , main_character.character_mask,numbers_chosen)
        if len(numbers_chosen)>0 and coli_8==True:
           eight=str(numbers_chosen[-1])
           num8 = goalfont.render(eight, 1, (0,0,0))
           eight_c=True
        if(eight_c==True):
           screen.blit(num8,(539,10))
        #collision detection for the number nine
        coli_9=collision_detection_numbers(9,zero_obj.devet,main_character.character,devet_pos.x , devet_pos.y , main_character.character_rect.left , main_character.character_rect.top , zero_obj.devet_mask , main_character.character_mask,numbers_chosen)
        if len(numbers_chosen)>0 and coli_9==True:
           nine=str(numbers_chosen[-1])
           num9 = goalfont.render(nine, 1, (0,0,0))
           nine_c=True
        if(nine_c==True):
           screen.blit(num9,(558,10))
     
        
        check_sum(numbers_chosen,zbir)
        
        pygame.display.update() 
            
 main_loop()
            
main()    
