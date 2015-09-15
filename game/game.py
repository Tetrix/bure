bure_f= "resources/bure.png"
game_over_f= 'resources/game-over.png'

#Level 1-5
wheel_file= "resources/level1/wheel.png"
star_file="resources/level1/star.png"
background = "resources/level1/bg_lvl1.png"
lvl1_color = (157,186,236)


#Level 6-10
background2 = "resources/level2/bg_lv2.png"
star2_small = "resources/level2/small_star.png"
star2_big = "resources/level2/big_star.png"
wheel2_file = "resources/level2/wheel.png"
lvl2_color=(95,172,93)






window_x = 270
window_y = 80

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
from numbers import *
from level import *
from check_sum import *
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (window_x,window_y)



def collision_detection(obj2,object1_rect_left , object1_rect_top , object2_rect_left , object2_rect_top , object1_mask , object2_mask,death_level ):
    offset_x, offset_y = int((object1_rect_left - object2_rect_left)), int((object1_rect_top - object2_rect_top))
    if (object2_mask.overlap(object1_mask, (offset_x, offset_y)) != None):
       
        screen.blit(game_over,go_coordinates)
        pygame.time.set_timer(USEREVENT+1,1)
     
         
        for event in pygame.event.get():
           if event.type == USEREVENT+1:
            time.sleep(1)
            death_level()
        
    

pygame.init()
bure = pygame.image.load(bure_f)
pygame.display.set_icon(bure)
pygame.display.set_caption('BURE')

game_over = pygame.image.load(game_over_f).convert_alpha()
go_coordinates=Vector2(200,150)

pygame.mouse.set_visible(0)    














def main():


        def level_one():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum=random.randint(20,30)
            level_one = Level(background,the_sum,1,lvl1_color,lvl1_color)
            level_one.loading_objects(26200000,10000000,31600000,15400000,28900000,12700000,23500000,18100000,20800000,None,None,None,None,None,None,None,None,None)
            level_one.star_load(star_file,300,300,300,300)
            level_one.wheel_load(wheel_file,470,470,450, 300)
            level_one.load_char()

            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
            

                level_one.wheel_star_rotation(1.0,0.55) 
                
                level_one.star_object.image_marking(star_file,470,470,447, 302)

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                                  
                #rotating the wheel and the star
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(False)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                level_one.numbers_rotated()
                for i in range(9):
                    level_one.num_obj.acceleration_list[i]-=0.023
                
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,main)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(234,60))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(260,60))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))
                     
                summ=check_the_sum(numbers_chosen,the_sum,suma,lvl1_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl1_color)
                check_sum(numbers_chosen,the_sum,suma,level_two,main)
                pygame.display.update() 

        


















        def level_two():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum2=random.randint(20,30)
            level_one = Level(background,the_sum2,2,lvl1_color,lvl1_color)
            level_one.loading_objects(26200000,10000000,31600000,15400000,28900000,12700000,23500000,18100000,20800000,None,None,None,None,None,None,None,None,None)
            level_one.star_load(star_file,300,300,300,300)
            level_one.wheel_load(wheel_file,470,470,450, 300)
            level_one.load_char()
            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
            

                level_one.wheel_star_rotation(1.0,1.0) 
                
                level_one.star_object.image_marking(star_file,470,470,447, 302)

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                                  
                #rotating the wheel and the star
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(False)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                level_one.numbers_rotated()
                for i in range(9):
                    level_one.num_obj.acceleration_list[i]-=0.033
                
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_two)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(234,60))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(260,60))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))
                     
                summ=check_the_sum(numbers_chosen,the_sum2,suma,lvl1_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl1_color)
                check_sum(numbers_chosen,the_sum2,suma,level_three,level_two)

                pygame.display.update() 

























        def level_three():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum3=random.randint(30,40)
            level_one = Level(background,the_sum3,3,lvl1_color,lvl1_color)
            level_one.loading_objects(26200000,10000000,31600000,15400000,28900000,12700000,23500000,18100000,20800000,None,None,None,None,None,None,None,None,None)
            level_one.star_load(star_file,300,300,300,300)
            level_one.wheel_load(wheel_file,470,470,450, 300)
            level_one.load_char()
            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
            

                level_one.wheel_star_rotation(1.0,0.7) 
                
                level_one.star_object.image_marking(star_file,470,470,447, 302)

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                                  
                #rotating the wheel and the star
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(False)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                
                level_one.numbers_rotated()
		for i in range(9):
                    level_one.num_obj.acceleration_list[i]-=0.023
                
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_three)
                
               #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(234,60))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(260,60))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))
                     
                summ=check_the_sum(numbers_chosen,the_sum3,suma,lvl1_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl1_color)
                check_sum(numbers_chosen,the_sum3,suma,level_four,level_three)
                pygame.display.update() 













        def level_four():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum4=random.randint(30,40)
            level_one = Level(background,the_sum4,4,lvl1_color,lvl1_color)
            level_one.loading_objects(26200000,10000000,31600000,15400000,28900000,12700000,23500000,18100000,20800000,None,None,None,None,None,None,None,None,None)
            level_one.star_load(star_file,300,300,300,300)
            level_one.wheel_load(wheel_file,470,470,450, 300)
            level_one.load_char()
            clock = pygame.time.Clock()
         
            suma = 0
         
            while True:
                
            

                level_one.wheel_star_rotation(1.0,1.25) 
                
                level_one.star_object.image_marking(star_file,470,470,447, 302)

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                                  
                #rotating the wheel and the star
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(False)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                rotate=level_one.numbers_rotated()
		for i in range(9):
                    level_one.num_obj.acceleration_list[i]-=0.033
               
                
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_four)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(234,60))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(260,60))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))
                     
                summ=check_the_sum(numbers_chosen,the_sum4,suma,lvl1_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl1_color)
                check_sum(numbers_chosen,the_sum4,suma,level_five,level_four)
                
                
                pygame.display.update()






        def level_five():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum5=random.randint(40,45)
            level_one = Level(background,the_sum5,5,lvl1_color,lvl1_color)
            level_one.loading_objects(26200000,10000000,31600000,15400000,28900000,12700000,23500000,18100000,20800000,None,None,None,None,None,None,None,None,None)
            level_one.star_load(star_file,300,300,300,300)
            level_one.wheel_load(wheel_file,650,650,450, 300)
            level_one.load_char()
            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
            

                level_one.wheel_star_rotation(1.0,1.1) 
                
                level_one.star_object.image_marking(star_file,470,470,447, 302)

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                                  
                #rotating the wheel and the star
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(False)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                level_one.numbers_rotated()
		for i in range(9):
                    level_one.num_obj.acceleration_list[i]-=0.033
               
                
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_five)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(234,60))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(260,60))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))
                     
                summ=check_the_sum(numbers_chosen,the_sum5,suma,lvl1_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl1_color)
                check_sum(numbers_chosen,the_sum5,suma,level_six,level_five)
                pygame.display.update() 










        
        def level_six():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum6=random.randint(50,60)
            level_one = Level(background2,the_sum6,6,lvl2_color,lvl2_color)
            #level_one.loading_objects(0,11,3,15.7,17,19.3,23,21.5,20.5)
	    level_one.loading_objects(0,1,2,3,4,6,5,6,0,   0.9,11.1,3.5,16.7,17.5,19.8,23.7,22,21.2)
	    
            level_one.star_load(star2_small,355,355,250,347)
            level_one.star_load2(star2_big,205,250,620,250)
            level_one.wheel_load(wheel2_file,365,365,257,360)
            level_one.wheel_load2(wheel2_file,250,250,620,250)
            
            level_one.load_char()
            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
          

                level_one.wheel_star_rotation2(1.0,1.3,level_one.star_object,level_one.star_object2,level_one.first_wheel,level_one.second_wheel,1.0,1.5) 
              
		level_one.star_object2.image_marking(star2_small,220,250,620,250)
                level_one.star_object.image_marking(star2_big,350,350,257,360)
                

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                



                  
                #rotating the wheel and the star
                
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.second_wheel.rotating_wheel(level_one.second_wheel.wheel,level_one.second_wheel.wheel_rotation,level_one.second_wheel.wheel_pos.x,level_one.second_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                level_one.star_object2.rotating_star(level_one.star_object2.star,level_one.star_object2.star_rotation,level_one.star_object2.star_pos.x,level_one.star_object2.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(True)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.second_wheel.rotated_wheel, level_one.second_wheel.wheel_draw_pos)

                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                screen.blit(level_one.star_object2.rotated_star, level_one.star_object2.star_draw_pos)
                           
                level_one.numbers2_rotated(level_one.num_obj,level_one.num_obj.eden,level_one.num_obj.eden_pos, level_one.num_obj.cetiri2,level_one.num_obj.cetiri2_pos,level_one.num_obj.sest,level_one.num_obj.sest_pos)
                level_one.numbers1_rotated(level_one.num_obj,level_one.num_obj.tri,level_one.num_obj.tri_pos, level_one.num_obj.sedum,level_one.num_obj.sedum_pos,level_one.num_obj.devet,level_one.num_obj.devet_pos)
                for i in range(9):
                    level_one.num_obj.acceleration_list2[i]+=0.033
		for i in range(9):
                    level_one.num_obj.acceleration_list[i]+=0.02
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                level_one.second_wheel.wheel_rotation += level_one.second_wheel.wheel_rotation_direction * level_one.second_wheel.wheel_rotation_speed *time_passed_seconds
		

                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds

                level_one.star_object2.star_rotation += level_one.star_object2.star_rotation_direction * level_one.star_object2.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)

                level_one.star_object2.star_rect.topleft=(level_one.star_object2.star_draw_pos.x,level_one.star_object2.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                level_one.star_object2.star_mask = pygame.mask.from_surface(level_one.star_object2.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_six)

                collision_detection(level_one.main_character.character,level_one.star_object2.star_rect.left , level_one.star_object2.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object2.star_mask , level_one.main_character.character_mask,level_six)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128
           
                #collision detection for the number two2
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
		#collision detection for the number two2
		coli2_2=level_one.num_obj.collision_detection_numbers(12,level_one.num_obj.dva2,level_one.main_character.character,level_one.num_obj.dva2_pos.x , level_one.num_obj.dva2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva2_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli2_2==True:
                   num22 = goalfont.render("12", 1, (0,0,0))
                   level_one.num_obj.two2_c=True
                if(level_one.num_obj.two2_c==True):
                   screen.blit(num22,(377,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
		#collision detection for the number four2
                coli2_4=level_one.num_obj.collision_detection_numbers(14,level_one.num_obj.cetiri2,level_one.main_character.character,level_one.num_obj.cetiri2_pos.x , level_one.num_obj.cetiri2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_4==True:
                   num42 = goalfont.render("14", 1, (0,0,0))
                   level_one.num_obj.four2_c=True
                if(level_one.num_obj.four2_c==True):
                   screen.blit(num42,(455,60))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(234,60))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(260,60))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render("9", 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))

		#collision detection for the number nine2
                coli2_9=level_one.num_obj.collision_detection_numbers(19,level_one.num_obj.devet2,level_one.main_character.character,level_one.num_obj.devet2_pos.x , level_one.num_obj.devet2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_9==True:
                   num92 = goalfont.render("19", 1, (0,0,0))
                   level_one.num_obj.nine2_c=True
                if(level_one.num_obj.nine2_c==True):
                   screen.blit(num92,(652,60))
                     
                summ=check_the_sum(numbers_chosen,the_sum6,suma,lvl2_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl2_color)
                check_sum(numbers_chosen,the_sum6,suma,level_seven,level_six)
                pygame.display.update() 

	def level_seven():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum6=random.randint(50,60)
            level_one = Level(background2,the_sum6,7,lvl2_color,lvl2_color)
            #level_one.loading_objects(0,11,3,15.7,17,19.3,23,21.5,20.5)
	    level_one.loading_objects(0,1,2,3,4,6,5,6,0,   0.9,11.1,3.5,16.7,17.5,19.8,23.7,22,21.2)
	    
            level_one.star_load(star2_small,355,355,250,347)
            level_one.star_load2(star2_big,205,250,620,250)
            level_one.wheel_load(wheel2_file,365,365,257,360)
            level_one.wheel_load2(wheel2_file,250,250,620,250)
            
            level_one.load_char()
            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
          

                level_one.wheel_star_rotation2(1.0,1.5,level_one.star_object,level_one.star_object2,level_one.first_wheel,level_one.second_wheel,1.4,1.5) 
              
		level_one.star_object2.image_marking(star2_small,220,250,620,250)
                level_one.star_object.image_marking(star2_big,350,350,257,360)
                

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                



                  
                #rotating the wheel and the star
                
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.second_wheel.rotating_wheel(level_one.second_wheel.wheel,level_one.second_wheel.wheel_rotation,level_one.second_wheel.wheel_pos.x,level_one.second_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                level_one.star_object2.rotating_star(level_one.star_object2.star,level_one.star_object2.star_rotation,level_one.star_object2.star_pos.x,level_one.star_object2.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(True)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.second_wheel.rotated_wheel, level_one.second_wheel.wheel_draw_pos)

                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                screen.blit(level_one.star_object2.rotated_star, level_one.star_object2.star_draw_pos)
                           
                level_one.numbers2_rotated(level_one.num_obj,level_one.num_obj.eden,level_one.num_obj.eden_pos, level_one.num_obj.cetiri2,level_one.num_obj.cetiri2_pos,level_one.num_obj.sest,level_one.num_obj.sest_pos)
                level_one.numbers1_rotated(level_one.num_obj,level_one.num_obj.tri2,level_one.num_obj.tri2_pos, level_one.num_obj.sedum2,level_one.num_obj.sedum2_pos,level_one.num_obj.eden2,level_one.num_obj.eden2_pos)
                for i in range(9):
                    level_one.num_obj.acceleration_list2[i]+=0.033
		for i in range(9):
                    level_one.num_obj.acceleration_list[i]+=0.02
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                level_one.second_wheel.wheel_rotation += level_one.second_wheel.wheel_rotation_direction * level_one.second_wheel.wheel_rotation_speed *time_passed_seconds
		

                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds

                level_one.star_object2.star_rotation += level_one.star_object2.star_rotation_direction * level_one.star_object2.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)

                level_one.star_object2.star_rect.topleft=(level_one.star_object2.star_draw_pos.x,level_one.star_object2.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                level_one.star_object2.star_mask = pygame.mask.from_surface(level_one.star_object2.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_seven)

                collision_detection(level_one.main_character.character,level_one.star_object2.star_rect.left , level_one.star_object2.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object2.star_mask , level_one.main_character.character_mask,level_seven)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128

                #collision detection for the number one2
		coli2_1=level_one.num_obj.collision_detection_numbers(11,level_one.num_obj.eden2,level_one.main_character.character,level_one.num_obj.eden2_pos.x , level_one.num_obj.eden2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden2_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli2_1==True:
                   num12 = goalfont.render("11", 1, (0,0,0))
                   level_one.num_obj.one2_c=True
                if(level_one.num_obj.one2_c==True):
                   screen.blit(num12,(338,60))
           
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
		#collision detection for the number two2
		coli2_2=level_one.num_obj.collision_detection_numbers(12,level_one.num_obj.dva2,level_one.main_character.character,level_one.num_obj.dva2_pos.x , level_one.num_obj.dva2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva2_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli2_2==True:
                   num22 = goalfont.render("12", 1, (0,0,0))
                   level_one.num_obj.two2_c=True
                if(level_one.num_obj.two2_c==True):
                   screen.blit(num22,(377,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number three2
                coli2_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri2,level_one.main_character.character,level_one.num_obj.tri2_pos.x , level_one.num_obj.tri2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri2_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli2_3==True:
                   num32 = goalfont.render("13", 1, (0,0,0))
                   level_one.num_obj.three2_c=True
                if(level_one.num_obj.three2_c==True):
                   screen.blit(num32,(417,60))


                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
		#collision detection for the number four2
                coli2_4=level_one.num_obj.collision_detection_numbers(14,level_one.num_obj.cetiri2,level_one.main_character.character,level_one.num_obj.cetiri2_pos.x , level_one.num_obj.cetiri2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_4==True:
                   num42 = goalfont.render("14", 1, (0,0,0))
                   level_one.num_obj.four2_c=True
                if(level_one.num_obj.four2_c==True):
                   screen.blit(num42,(455,60))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(234,60))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(260,60))

                #collision detection for the number seven2
                coli2_7=level_one.num_obj.collision_detection_numbers(19,level_one.num_obj.sedum2,level_one.main_character.character,level_one.num_obj.sedum2_pos.x , level_one.num_obj.sedum2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_7==True:
                   num72 = goalfont.render("17", 1, (0,0,0))
                   level_one.num_obj.seven2_c=True
                if(level_one.num_obj.seven2_c==True):
                   screen.blit(num72,(575,60))

                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render("9", 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))

		#collision detection for the number nine2
                coli2_9=level_one.num_obj.collision_detection_numbers(19,level_one.num_obj.devet2,level_one.main_character.character,level_one.num_obj.devet2_pos.x , level_one.num_obj.devet2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_9==True:
                   num92 = goalfont.render("19", 1, (0,0,0))
                   level_one.num_obj.nine2_c=True
                if(level_one.num_obj.nine2_c==True):
                   screen.blit(num92,(652,60))

                
                     
                summ=check_the_sum(numbers_chosen,the_sum6,suma,lvl2_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl2_color)
                check_sum(numbers_chosen,the_sum6,suma,level_eight,level_seven)
                pygame.display.update()

	def level_eight():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum6=random.randint(50,60)
            level_one = Level(background2,the_sum6,8,lvl2_color,lvl2_color)
            #level_one.loading_objects(0,11,3,15.7,17,19.3,23,21.5,20.5)
	    level_one.loading_objects(0,1,2,3,4,6,5,6,0,   0.9,11.1,3.5,16.7,17.5,19.8,23.7,22,21.2)
	    
            level_one.star_load(star2_small,355,355,250,347)
            level_one.star_load2(star2_big,205,250,620,250)
            level_one.wheel_load(wheel2_file,365,365,257,360)
            level_one.wheel_load2(wheel2_file,250,250,620,250)
            
            level_one.load_char()
            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
          

                level_one.wheel_star_rotation2(1.0,1.1,level_one.star_object,level_one.star_object2,level_one.first_wheel,level_one.second_wheel,1.0,1.5) 
              
		level_one.star_object2.image_marking(star2_small,220,250,620,250)
                level_one.star_object.image_marking(star2_big,350,350,257,360)
                

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                



                  
                #rotating the wheel and the star
                
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.second_wheel.rotating_wheel(level_one.second_wheel.wheel,level_one.second_wheel.wheel_rotation,level_one.second_wheel.wheel_pos.x,level_one.second_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                level_one.star_object2.rotating_star(level_one.star_object2.star,level_one.star_object2.star_rotation,level_one.star_object2.star_pos.x,level_one.star_object2.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(True)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.second_wheel.rotated_wheel, level_one.second_wheel.wheel_draw_pos)

                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                screen.blit(level_one.star_object2.rotated_star, level_one.star_object2.star_draw_pos)
                           
                level_one.numbers2_rotated(level_one.num_obj,level_one.num_obj.sedum2,level_one.num_obj.sedum2_pos, level_one.num_obj.eden2,level_one.num_obj.eden2_pos,level_one.num_obj.eden,level_one.num_obj.eden_pos)
                level_one.numbers1_rotated(level_one.num_obj,level_one.num_obj.tri,level_one.num_obj.tri_pos, level_one.num_obj.pet2,level_one.num_obj.pet2_pos,level_one.num_obj.devet,level_one.num_obj.devet_pos)
                for i in range(9):
                    level_one.num_obj.acceleration_list2[i]-=0.033
		for i in range(9):
                    level_one.num_obj.acceleration_list[i]+=0.043
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                level_one.second_wheel.wheel_rotation += level_one.second_wheel.wheel_rotation_direction * level_one.second_wheel.wheel_rotation_speed *time_passed_seconds
		

                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds

                level_one.star_object2.star_rotation += level_one.star_object2.star_rotation_direction * level_one.star_object2.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)

                level_one.star_object2.star_rect.topleft=(level_one.star_object2.star_draw_pos.x,level_one.star_object2.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                level_one.star_object2.star_mask = pygame.mask.from_surface(level_one.star_object2.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_eight)

                collision_detection(level_one.main_character.character,level_one.star_object2.star_rect.left , level_one.star_object2.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object2.star_mask , level_one.main_character.character_mask,level_eight)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128

		#collision detection for the number eleven
                coli2_1=level_one.num_obj.collision_detection_numbers(11,level_one.num_obj.eden2,level_one.main_character.character,level_one.num_obj.eden2_pos.x , level_one.num_obj.eden2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden2_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli2_1==True:
                   num11 = goalfont.render("11", 1, (0,0,0))
                   level_one.num_obj.one2_c=True
                if(level_one.num_obj.one2_c==True):
                   screen.blit(num11,(338,60))#406+128

		#collision detection for the number seventheen
		coli2_7=level_one.num_obj.collision_detection_numbers(17,level_one.num_obj.sedum2,level_one.main_character.character,level_one.num_obj.sedum2_pos.x , level_one.num_obj.sedum2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum2_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli2_7==True:
                   num27 = goalfont.render("17", 1, (0,0,0))
                   level_one.num_obj.seven2_c=True
                if(level_one.num_obj.seven2_c==True):
                   screen.blit(num27,(575,60))#406+128
           
                #collision detection for the number two2
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
		#collision detection for the number two2
		coli2_2=level_one.num_obj.collision_detection_numbers(12,level_one.num_obj.dva2,level_one.main_character.character,level_one.num_obj.dva2_pos.x , level_one.num_obj.dva2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva2_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli2_2==True:
                   num22 = goalfont.render("12", 1, (0,0,0))
                   level_one.num_obj.two2_c=True
                if(level_one.num_obj.two2_c==True):
                   screen.blit(num22,(377,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
		
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

		#collision detection for the number fifteen
                coli2_5=level_one.num_obj.collision_detection_numbers(15,level_one.num_obj.pet2,level_one.main_character.character,level_one.num_obj.pet2_pos.x , level_one.num_obj.pet2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet2_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli2_5==True:
                   num52 = goalfont.render("15", 1, (0,0,0))
                   level_one.num_obj.five2_c=True
                if(level_one.num_obj.five2_c==True):
                   screen.blit(num52,(497,60))

                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render("9", 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))

		#collision detection for the number nine2
                coli2_9=level_one.num_obj.collision_detection_numbers(19,level_one.num_obj.devet2,level_one.main_character.character,level_one.num_obj.devet2_pos.x , level_one.num_obj.devet2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_9==True:
                   num92 = goalfont.render("19", 1, (0,0,0))
                   level_one.num_obj.nine2_c=True
                if(level_one.num_obj.nine2_c==True):
                   screen.blit(num92,(652,60))
                     
                summ=check_the_sum(numbers_chosen,the_sum6,suma,lvl2_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl2_color)
                check_sum(numbers_chosen,the_sum6,suma,level_nine,level_eight)
                pygame.display.update()

	def level_nine():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum6=random.randint(50,60)
            level_one = Level(background2,the_sum6,9,lvl2_color,lvl2_color)
            #level_one.loading_objects(0,11,3,15.7,17,19.3,23,21.5,20.5)
	    level_one.loading_objects(0,1,2,3,4,6,5,6,0,   0.9,11.1,3.5,16.7,17.5,19.8,23.7,22,21.2)
	    
            level_one.star_load(star2_small,355,355,250,347)
            level_one.star_load2(star2_big,205,250,620,250)
            level_one.wheel_load(wheel2_file,365,365,257,360)
            level_one.wheel_load2(wheel2_file,250,250,620,250)
            
            level_one.load_char()
            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
          

                level_one.wheel_star_rotation2(1.0,1.3,level_one.star_object,level_one.star_object2,level_one.first_wheel,level_one.second_wheel,1.5,1.5) 
              
		level_one.star_object2.image_marking(star2_small,220,250,620,250)
                level_one.star_object.image_marking(star2_big,350,350,257,360)
                

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                



                  
                #rotating the wheel and the star
                
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.second_wheel.rotating_wheel(level_one.second_wheel.wheel,level_one.second_wheel.wheel_rotation,level_one.second_wheel.wheel_pos.x,level_one.second_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                level_one.star_object2.rotating_star(level_one.star_object2.star,level_one.star_object2.star_rotation,level_one.star_object2.star_pos.x,level_one.star_object2.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(True)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.second_wheel.rotated_wheel, level_one.second_wheel.wheel_draw_pos)

                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                screen.blit(level_one.star_object2.rotated_star, level_one.star_object2.star_draw_pos)
                           
                level_one.numbers2_rotated(level_one.num_obj,level_one.num_obj.cetiri2,level_one.num_obj.cetiri2_pos, level_one.num_obj.tri,level_one.num_obj.tri_pos,level_one.num_obj.sest,level_one.num_obj.sest_pos)
                level_one.numbers1_rotated(level_one.num_obj,level_one.num_obj.eden,level_one.num_obj.eden_pos, level_one.num_obj.sedum,level_one.num_obj.sedum_pos,level_one.num_obj.eden2,level_one.num_obj.eden2_pos)
                for i in range(9):
                    level_one.num_obj.acceleration_list2[i]+=0.036
		for i in range(9):
                    level_one.num_obj.acceleration_list[i]-=0.02
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                level_one.second_wheel.wheel_rotation += level_one.second_wheel.wheel_rotation_direction * level_one.second_wheel.wheel_rotation_speed *time_passed_seconds
		

                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds

                level_one.star_object2.star_rotation += level_one.star_object2.star_rotation_direction * level_one.star_object2.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)

                level_one.star_object2.star_rect.topleft=(level_one.star_object2.star_draw_pos.x,level_one.star_object2.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                level_one.star_object2.star_mask = pygame.mask.from_surface(level_one.star_object2.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_nine)

                collision_detection(level_one.main_character.character,level_one.star_object2.star_rect.left , level_one.star_object2.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object2.star_mask , level_one.main_character.character_mask,level_nine)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128

                #collision detection for the number one2
		coli2_1=level_one.num_obj.collision_detection_numbers(11,level_one.num_obj.eden2,level_one.main_character.character,level_one.num_obj.eden2_pos.x , level_one.num_obj.eden2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden2_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli2_1==True:
                   num12 = goalfont.render("11", 1, (0,0,0))
                   level_one.num_obj.one2_c=True
                if(level_one.num_obj.one2_c==True):
                   screen.blit(num12,(338,60))
           
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
		#collision detection for the number two2
		coli2_2=level_one.num_obj.collision_detection_numbers(12,level_one.num_obj.dva2,level_one.main_character.character,level_one.num_obj.dva2_pos.x , level_one.num_obj.dva2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva2_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli2_2==True:
                   num22 = goalfont.render("12", 1, (0,0,0))
                   level_one.num_obj.two2_c=True
                if(level_one.num_obj.two2_c==True):
                   screen.blit(num22,(377,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number three2
                coli2_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri2,level_one.main_character.character,level_one.num_obj.tri2_pos.x , level_one.num_obj.tri2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri2_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli2_3==True:
                   num32 = goalfont.render("13", 1, (0,0,0))
                   level_one.num_obj.three2_c=True
                if(level_one.num_obj.three2_c==True):
                   screen.blit(num32,(417,60))


                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
		#collision detection for the number four2
                coli2_4=level_one.num_obj.collision_detection_numbers(14,level_one.num_obj.cetiri2,level_one.main_character.character,level_one.num_obj.cetiri2_pos.x , level_one.num_obj.cetiri2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_4==True:
                   num42 = goalfont.render("14", 1, (0,0,0))
                   level_one.num_obj.four2_c=True
                if(level_one.num_obj.four2_c==True):
                   screen.blit(num42,(455,60))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(234,60))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(260,60))

                #collision detection for the number seven2
                coli2_7=level_one.num_obj.collision_detection_numbers(19,level_one.num_obj.sedum2,level_one.main_character.character,level_one.num_obj.sedum2_pos.x , level_one.num_obj.sedum2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_7==True:
                   num72 = goalfont.render("17", 1, (0,0,0))
                   level_one.num_obj.seven2_c=True
                if(level_one.num_obj.seven2_c==True):
                   screen.blit(num72,(575,60))

                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render("9", 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))

		#collision detection for the number nine2
                coli2_9=level_one.num_obj.collision_detection_numbers(19,level_one.num_obj.devet2,level_one.main_character.character,level_one.num_obj.devet2_pos.x , level_one.num_obj.devet2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_9==True:
                   num92 = goalfont.render("19", 1, (0,0,0))
                   level_one.num_obj.nine2_c=True
                if(level_one.num_obj.nine2_c==True):
                   screen.blit(num92,(652,60))

                
                     
                summ=check_the_sum(numbers_chosen,the_sum6,suma,lvl2_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl2_color)
                check_sum(numbers_chosen,the_sum6,suma,level_nine,level_nine)
                pygame.display.update()

	
	def level_ten():
            lvl2_color=(95,172,93)
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum6=random.randint(50,60)
            level_one = Level(background2,the_sum6,10,lvl2_color,lvl2_color)
            #level_one.loading_objects(0,11,3,15.7,17,19.3,23,21.5,20.5)
	    level_one.loading_objects(0,1,2,3,4,6,5,6,0,   0.9,11.1,3.5,16.7,17.5,19.8,23.7,22,21.2)
	    
            level_one.star_load(star2_small,355,355,250,347)
            level_one.star_load2(star2_big,205,250,620,250)
            level_one.wheel_load(wheel2_file,385,385,257,360)
            level_one.wheel_load2(wheel2_file,270,270,620,250)
            
            level_one.load_char()
            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
          

                level_one.wheel_star_rotation2(1.0,1.1,level_one.star_object,level_one.star_object2,level_one.first_wheel,level_one.second_wheel,1.0,1.5) 
              
		level_one.star_object2.image_marking(star2_small,220,250,620,250)
                level_one.star_object.image_marking(star2_big,350,350,257,360)
                

                level_one.main_character.character_rect.topleft = (level_one.main_character.char_x,level_one.main_character.char_y)
                #end of star changing color      
                 
                pressed_keys = pygame.key.get_pressed()

                #setting the fps
                time_passed = clock.tick(50)
                time_passed_seconds = time_passed / 1000.0

                # making the character move
                
                if pressed_keys[K_RIGHT]:
                    level_one.main_character .char_x += level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_LEFT]:
                    level_one.main_character.char_x -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_UP]:
                    level_one.main_character.char_y -= level_one.main_character.char_speed * time_passed_seconds
                if pressed_keys[K_DOWN]:
                    level_one.main_character.char_y += level_one.main_character.char_speed * time_passed_seconds          
                # end of the movement
                
               
                # if character goes out of the screen
                
                level_one.main_character.char_out_of_screen()
                



                  
                #rotating the wheel and the star
                
                level_one.first_wheel.rotating_wheel(level_one.first_wheel.wheel,level_one.first_wheel.wheel_rotation,level_one.first_wheel.wheel_pos.x,level_one.first_wheel.wheel_pos.y)
                level_one.second_wheel.rotating_wheel(level_one.second_wheel.wheel,level_one.second_wheel.wheel_rotation,level_one.second_wheel.wheel_pos.x,level_one.second_wheel.wheel_pos.y)
                level_one.star_object.rotating_star(level_one.star_object.star,level_one.star_object.star_rotation,level_one.star_object.star_pos.x,level_one.star_object.star_pos.y)
                level_one.star_object2.rotating_star(level_one.star_object2.star,level_one.star_object2.star_rotation,level_one.star_object2.star_pos.x,level_one.star_object2.star_pos.y)
                

                screen.fill((0,0,0))   
                level_one.blit_main(True)     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.second_wheel.rotated_wheel, level_one.second_wheel.wheel_draw_pos)

                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                screen.blit(level_one.star_object2.rotated_star, level_one.star_object2.star_draw_pos)
                           
                level_one.numbers2_rotated(level_one.num_obj,level_one.num_obj.sedum2,level_one.num_obj.sedum2_pos, level_one.num_obj.eden2,level_one.num_obj.eden2_pos,level_one.num_obj.osum2,level_one.num_obj.osum2_pos)
                level_one.numbers1_rotated(level_one.num_obj,level_one.num_obj.sest2,level_one.num_obj.sest2_pos, level_one.num_obj.pet2,level_one.num_obj.pet2_pos,level_one.num_obj.eden,level_one.num_obj.eden_pos)
                for i in range(9):
                    level_one.num_obj.acceleration_list2[i]-=0.033
		for i in range(9):
                    level_one.num_obj.acceleration_list[i]-=0.043
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                level_one.second_wheel.wheel_rotation += level_one.second_wheel.wheel_rotation_direction * level_one.second_wheel.wheel_rotation_speed *time_passed_seconds
		

                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds

                level_one.star_object2.star_rotation += level_one.star_object2.star_rotation_direction * level_one.star_object2.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)

                level_one.star_object2.star_rect.topleft=(level_one.star_object2.star_draw_pos.x,level_one.star_object2.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                level_one.star_object2.star_mask = pygame.mask.from_surface(level_one.star_object2.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_ten)

                collision_detection(level_one.main_character.character,level_one.star_object2.star_rect.left , level_one.star_object2.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object2.star_mask , level_one.main_character.character_mask,level_ten)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(104,60))#406+128

		#collision detection for the number eleven
                coli2_1=level_one.num_obj.collision_detection_numbers(11,level_one.num_obj.eden2,level_one.main_character.character,level_one.num_obj.eden2_pos.x , level_one.num_obj.eden2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden2_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli2_1==True:
                   num11 = goalfont.render("11", 1, (0,0,0))
                   level_one.num_obj.one2_c=True
                if(level_one.num_obj.one2_c==True):
                   screen.blit(num11,(338,60))#406+128

		#collision detection for the number seventheen
		coli2_7=level_one.num_obj.collision_detection_numbers(17,level_one.num_obj.sedum2,level_one.main_character.character,level_one.num_obj.sedum2_pos.x , level_one.num_obj.sedum2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum2_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli2_7==True:
                   num27 = goalfont.render("17", 1, (0,0,0))
                   level_one.num_obj.seven2_c=True
                if(level_one.num_obj.seven2_c==True):
                   screen.blit(num27,(575,60))#406+128
           
                #collision detection for the number two2
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(128,60))
		#collision detection for the number two2
		coli2_2=level_one.num_obj.collision_detection_numbers(12,level_one.num_obj.dva2,level_one.main_character.character,level_one.num_obj.dva2_pos.x , level_one.num_obj.dva2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva2_mask , level_one.main_character.character_mask,numbers_chosen)
                
                if coli2_2==True:
                   num22 = goalfont.render("12", 1, (0,0,0))
                   level_one.num_obj.two2_c=True
                if(level_one.num_obj.two2_c==True):
                   screen.blit(num22,(377,60))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(153,60))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(178,60))
		
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(207,60)) 

		#collision detection for the number fifteen
                coli2_5=level_one.num_obj.collision_detection_numbers(15,level_one.num_obj.pet2,level_one.main_character.character,level_one.num_obj.pet2_pos.x , level_one.num_obj.pet2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet2_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli2_5==True:
                   num52 = goalfont.render("15", 1, (0,0,0))
                   level_one.num_obj.five2_c=True
                if(level_one.num_obj.five2_c==True):
                   screen.blit(num52,(497,60))
		#collision detection for the number six
                coli2_6=level_one.num_obj.collision_detection_numbers(16,level_one.num_obj.sest2,level_one.main_character.character,level_one.num_obj.sest2_pos.x , level_one.num_obj.sest2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_6==True:
                   num62 = goalfont.render("16", 1, (0,0,0))
                   level_one.num_obj.six2_c=True
                if(level_one.num_obj.six2_c==True):
                   screen.blit(num62,(536,60))

                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(287,60))

		coli2_8=level_one.num_obj.collision_detection_numbers(18,level_one.num_obj.osum2,level_one.main_character.character,level_one.num_obj.osum2_pos.x , level_one.num_obj.osum2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_8==True:
                   num82 = goalfont.render("18", 1, (0,0,0))
                   level_one.num_obj.eight2_c=True
                if(level_one.num_obj.eight2_c==True):
                   screen.blit(num82,(614,60))

                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render("9", 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(312,60))

		#collision detection for the number nine2
                coli2_9=level_one.num_obj.collision_detection_numbers(19,level_one.num_obj.devet2,level_one.main_character.character,level_one.num_obj.devet2_pos.x , level_one.num_obj.devet2_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet2_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli2_9==True:
                   num92 = goalfont.render("19", 1, (0,0,0))
                   level_one.num_obj.nine2_c=True
                if(level_one.num_obj.nine2_c==True):
                   screen.blit(num92,(652,60))
                     
                summ=check_the_sum(numbers_chosen,the_sum6,suma,lvl2_color)
                screen.blit(summ,(680,500))
                level_one.print_text_sum(lvl2_color)
                check_sum(numbers_chosen,the_sum6,suma,level_ten,level_ten)
                pygame.display.update()


 





        level_five()

main()   
