import pygame
from gameobjects.vector2 import Vector2


class Star(object):
    
      
    def star_properties(self):
        
        self.star_speed = 300.
        self.star_rotation = 0.
        self.star_rotation_speed = -50. # Degrees per second
        self.star_rotation_direction =0.
        

        self.star_event=pygame.USEREVENT +2
        self.star_event_speed = 10
        pygame.time.set_timer(self.star_event,self.star_event_speed)

        self.star2_event=pygame.USEREVENT +3
        self.star2_event_speed = 20
        pygame.time.set_timer(self.star2_event,self.star2_event_speed)

        self.star3_event=pygame.USEREVENT +4
        self.star3_event_speed = 30
        pygame.time.set_timer(self.star3_event,self.star3_event_speed)


    def rotating_star(self,obj_star,obj_star_rotation,obj_star_x,obj_star_y):
        self.rotated_star = pygame.transform.rotate(obj_star, obj_star_rotation)
        self.w2, self.h2 = self.rotated_star.get_size()
        self.star_draw_pos = Vector2(obj_star_x-self.w2/2, obj_star_y-self.h2/2) 


    def image_marking(self,starf,w,h,x,y):
        self.star=pygame.image.load(starf).convert()
        self.star = pygame.transform.scale(self.star,(w,h))
        
        self.star.set_colorkey((255,255,255))
        
        self.star_mask = pygame.mask.from_surface(self.star)
        self.star_rect = self.star.get_rect()
        self.star_pos = Vector2(x,y)




        
