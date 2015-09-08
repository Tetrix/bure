bure_f= "resources/bure.png"
game_over_f= 'resources/game-over.png'
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
            the_sum=random.randint(10,45)
            level_one = Level(background,the_sum,1)
            level_one.loading_objects(26200000,10000000,31600000,15400000,28900000,12700000,23500000,18100000,20800000)

            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
            

                level_one.wheel_star_rotation(1.0,0.7) 
                
                level_one.star_object.image_marking()

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
                level_one.blit_main()     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                level_one.numbers_rotated(9,0.032)
               
                
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
                   screen.blit(num1,(534,10))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(558,10))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(583,10))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(608,10))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(637,10)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(664,10))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(690,10))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(717,10))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(742,10))
                     
                summ=check_the_sum(numbers_chosen,the_sum,suma)
                screen.blit(summ,(80,500))
                level_one.print_text_sum()
                check_sum(numbers_chosen,the_sum,suma,level_two,main)
                pygame.display.update() 

        


















        def level_two():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum2=random.randint(10,45)
            level_one = Level(background,the_sum2,2)
            level_one.loading_objects(26200000,10000000,28900000,12700000,31600000,18100000,23500000,15400000,20800000)

            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
            

                level_one.wheel_star_rotation(1.0,1.2) 
                
                level_one.star_object.image_marking()

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
                level_one.blit_main()     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                level_one.numbers_rotated(9,0.043)
               
                
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
                   screen.blit(num1,(534,10))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(558,10))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(583,10))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(608,10))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(637,10)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(664,10))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(690,10))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(717,10))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(742,10))
                     
                summ=check_the_sum(numbers_chosen,the_sum2,suma)
                screen.blit(summ,(80,500))
                level_one.print_text_sum()
                check_sum(numbers_chosen,the_sum2,suma,level_three,level_two)
                pygame.display.update() 

























        def level_three():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum3=random.randint(10,45)
            level_one = Level(background,the_sum3,3)
            level_one.loading_objects(12700000,10000000,23500000,18100000,28900000,20800000,26200000,15400000,31600000)

            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
            

                level_one.wheel_star_rotation(1.0,0.7) 
                
                level_one.star_object.image_marking()

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
                level_one.blit_main()     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                level_one.numbers_rotated2(9,0.023)
               
                
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
                   screen.blit(num1,(534,10))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(558,10))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(583,10))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(608,10))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(637,10)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(664,10))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(690,10))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(717,10))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(742,10))
                     
                summ=check_the_sum(numbers_chosen,the_sum3,suma)
                screen.blit(summ,(80,500))
                level_one.print_text_sum()
                check_sum(numbers_chosen,the_sum3,suma,level_four,level_three)
                pygame.display.update() 













        def level_four():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum4=random.randint(20,30)
            level_one = Level(background,the_sum4,4)
            level_one.loading_objects(15400000,23500000,31600000,12700000,10000000,28900000,20800000,26200000,18100000)

            clock = pygame.time.Clock()
         
            suma = 0
         
            while True:
                
            

                level_one.wheel_star_rotation(1.0,1.5) 
                
                level_one.star_object.image_marking()

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
                level_one.blit_main()     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                rotate=level_one.numbers_rotated(9,0.020)
               
                
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
                   screen.blit(num1,(534,10))
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(558,10))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(583,10))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(608,10))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(637,10)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(664,10))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(690,10))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(717,10))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(742,10))
                     
                summ=check_the_sum(numbers_chosen,the_sum4,suma)
                screen.blit(summ,(80,500))
                level_one.print_text_sum()
                check_sum(numbers_chosen,the_sum4,suma,level_five,level_four)
                
                
                pygame.display.update()






        def level_five():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum5=random.randint(35,40)
            level_one = Level(background,the_sum5,5)
            level_one.loading_objects(10000000,23500000,12700000,15400000,31600000,18100000,20800000,26200000,28900000)

            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
            

                level_one.wheel_star_rotation(1.0,1.1) 
                
                level_one.star_object.image_marking()

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
                level_one.blit_main()     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                level_one.numbers_rotated2(9,0.033)
               
                
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
                   screen.blit(num1,(534,10))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(558,10))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(583,10))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(608,10))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(637,10)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(664,10))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(690,10))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(717,10))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(742,10))
                     
                summ=check_the_sum(numbers_chosen,the_sum5,suma)
                screen.blit(summ,(80,500))
                level_one.print_text_sum()
                check_sum(numbers_chosen,the_sum5,suma,level_six,level_five)
                pygame.display.update() 








        def level_six():
            
            numbers_chosen = [] 
            #OBJECT OF CLASS Level
            the_sum6=random.randint(35,40)
            level_one = Level(background,the_sum6,5)
            level_one.loading_objects(10000000,23500000,12700000,15400000,31600000,18100000,20800000,26200000,28900000)

            clock = pygame.time.Clock()
         
            suma = 0
            
            while True:
                
            

                level_one.wheel_star_rotation(1.0,1.1) 
                
                level_one.star_object.image_marking()

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
                level_one.blit_main()     
                screen.blit(level_one.first_wheel.rotated_wheel, level_one.first_wheel.wheel_draw_pos)
                screen.blit(level_one.star_object.rotated_star, level_one.star_object.star_draw_pos)
                           
                level_one.numbers_rotated2(9,0.033)
               
                
                #wheel rotation
                level_one.first_wheel.wheel_rotation += level_one.first_wheel.wheel_rotation_direction * level_one.first_wheel.wheel_rotation_speed *time_passed_seconds
                #star rotation
                level_one.star_object.star_rotation += level_one.star_object.star_rotation_direction * level_one.star_object.star_rotation_speed *time_passed_seconds
                
                level_one.star_object.star_rect.topleft=(level_one.star_object.star_draw_pos.x,level_one.star_object.star_draw_pos.y)
                
                #creating a new mask
                level_one.star_object.star_mask = pygame.mask.from_surface(level_one.star_object.rotated_star)
                   
                screen.blit(level_one.main_character.character,(level_one.main_character.char_x,level_one.main_character.char_y))
                
                #collision detection for the character and the star
                collision_detection(level_one.main_character.character,level_one.star_object.star_rect.left , level_one.star_object.star_rect.top , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.star_object.star_mask , level_one.main_character.character_mask,level_six)
                
                #collision detection for the number one
                coli_1=level_one.num_obj.collision_detection_numbers(1,level_one.num_obj.eden,level_one.main_character.character,level_one.num_obj.eden_pos.x , level_one.num_obj.eden_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.eden_mask , level_one.main_character.character_mask,numbers_chosen)
                        
                if coli_1==True:
                   num1 = goalfont.render("1", 1, (0,0,0))
                   level_one.num_obj.one_c=True
                if(level_one.num_obj.one_c==True):
                   screen.blit(num1,(534,10))#406+128
         
                #collision detection for the number two
                coli_2=level_one.num_obj.collision_detection_numbers(2,level_one.num_obj.dva,level_one.main_character.character,level_one.num_obj.dva_pos.x , level_one.num_obj.dva_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.dva_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_2==True:
                   num2 = goalfont.render("2", 1, (0,0,0))
                   level_one.num_obj.two_c=True
                if(level_one.num_obj.two_c==True):
                   screen.blit(num2,(558,10))
                   
                #collision detection for the number three
                coli_3=level_one.num_obj.collision_detection_numbers(3,level_one.num_obj.tri,level_one.main_character.character,level_one.num_obj.tri_pos.x , level_one.num_obj.tri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.tri_mask , level_one.main_character.character_mask,numbers_chosen)   
                if coli_3==True:
                   num3 = goalfont.render("3", 1, (0,0,0))
                   level_one.num_obj.three_c=True
                if(level_one.num_obj.three_c==True):
                   screen.blit(num3,(583,10))

                #collision detection for the number four
                coli_4=level_one.num_obj.collision_detection_numbers(4,level_one.num_obj.cetiri,level_one.main_character.character,level_one.num_obj.cetiri_pos.x , level_one.num_obj.cetiri_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.cetiri_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_4==True:
                   num4 = goalfont.render("4", 1, (0,0,0))
                   level_one.num_obj.four_c=True
                if(level_one.num_obj.four_c==True):
                   screen.blit(num4,(608,10))
                 
                #collision detection for the number five
                coli_5=level_one.num_obj.collision_detection_numbers(5,level_one.num_obj.pet,level_one.main_character.character,level_one.num_obj.pet_pos.x , level_one.num_obj.pet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.pet_mask , level_one.main_character.character_mask,numbers_chosen)  
                if coli_5==True:
                   num5 = goalfont.render("5", 1, (0,0,0))
                   level_one.num_obj.five_c=True
                if(level_one.num_obj.five_c==True):
                   screen.blit(num5,(637,10)) 

                #collision detection for the number six
                coli_6=level_one.num_obj.collision_detection_numbers(6,level_one.num_obj.sest,level_one.main_character.character,level_one.num_obj.sest_pos.x , level_one.num_obj.sest_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sest_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_6==True:
                   num6 = goalfont.render("6", 1, (0,0,0))
                   level_one.num_obj.six_c=True
                if(level_one.num_obj.six_c==True):
                   screen.blit(num6,(664,10))

                #collision detection for the number seven
                coli_7=level_one.num_obj.collision_detection_numbers(7,level_one.num_obj.sedum,level_one.main_character.character,level_one.num_obj.sedum_pos.x , level_one.num_obj.sedum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.sedum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_7==True:
                   num7 = goalfont.render("7", 1, (0,0,0))
                   level_one.num_obj.seven_c=True
                if(level_one.num_obj.seven_c==True):
                   screen.blit(num7,(690,10))
                #collision detection for the number eight
                coli_8=level_one.num_obj.collision_detection_numbers(8,level_one.num_obj.osum,level_one.main_character.character,level_one.num_obj.osum_pos.x , level_one.num_obj.osum_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.osum_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_8==True:
                   num8 = goalfont.render("8", 1, (0,0,0))
                   level_one.num_obj.eight_c=True
                if(level_one.num_obj.eight_c==True):
                   screen.blit(num8,(717,10))
                #collision detection for the number nine
                coli_9=level_one.num_obj.collision_detection_numbers(9,level_one.num_obj.devet,level_one.main_character.character,level_one.num_obj.devet_pos.x , level_one.num_obj.devet_pos.y , level_one.main_character.character_rect.left , level_one.main_character.character_rect.top , level_one.num_obj.devet_mask , level_one.main_character.character_mask,numbers_chosen)
                if coli_9==True:
                   num9 = goalfont.render(str(9), 1, (0,0,0))
                   level_one.num_obj.nine_c=True
                if(level_one.num_obj.nine_c==True):
                   screen.blit(num9,(742,10))
                     
                summ=check_the_sum(numbers_chosen,the_sum6,suma)
                screen.blit(summ,(80,500))
                level_one.print_text_sum()
                check_sum(numbers_chosen,the_sum6,suma,level_six,level_six)
                pygame.display.update() 









        level_six()

main()   
