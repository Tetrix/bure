import pygame
from gameobjects.vector2 import Vector2

star_file="resources/star2/s2_1.png"

class Star(object):
    def __init__(self):
        self.star=pygame.image.load(star_file).convert_alpha()
        self.star=pygame.transform.scale(self.star,(550,550))    
    
    def star_properties(self):
        self.star_pos = Vector2(447, 302)
        self.star_speed = 300.
        self.star_rotation = 0.
        self.star_rotation_speed = -50. # Degrees per second
        self.star_rotation_direction =0.
        
        self.star_event=pygame.USEREVENT +2
        self.star_event_speed = 100
        pygame.time.set_timer(self.star_event,self.star_event_speed)

        self.star2_event=pygame.USEREVENT +3
        self.star2_event_speed = 50
        pygame.time.set_timer(self.star2_event,self.star2_event_speed)

        self.star3_event=pygame.USEREVENT +4
        self.star3_event_speed = 20
        pygame.time.set_timer(self.star3_event,self.star3_event_speed)
        
