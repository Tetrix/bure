import pygame
from gameobjects.vector2 import Vector2

wheel_file= "resources/circle.png"

class Wheel(object):
    def __init__(self):
        self.wheel = pygame.sprite.Sprite()


        self.wheel=pygame.image.load(wheel_file).convert_alpha()


        
        
    def wheel_properties(self):
        
        self.wheel_pos = Vector2(450, 300)
        self.wheel_speed = 300.
        self.wheel_ue_speed=500
        self.wheel_rotation = 0.
        self.wheel_rotation_speed = -50. # Degrees per second
        self.wheel_rotate=pygame.USEREVENT + 1
        self.wheel_rotation_direction = 0.
        pygame.time.set_timer(self.wheel_rotate,self.wheel_ue_speed)
