import pygame
from gameobjects.vector2 import Vector2



class Wheel(object):
    def __init__(self,wheel_f,size_w,size_h):
        self.wheel = pygame.sprite.Sprite()
        self.wheel=pygame.image.load(wheel_f).convert_alpha()
        self.wheel = pygame.transform.scale(self.wheel,(size_w,size_h))


    def wheel_properties(self,x,y):
        
        self.wheel_pos = Vector2(x,y)
        self.wheel_speed = 300.
        self.wheel_ue_speed=65
        self.wheel_rotation = 0.
        self.wheel_rotation_speed = -50. # Degrees per second
        self.wheel_rotate=pygame.USEREVENT + 1
        self.wheel_rotation_direction = 0.
        pygame.time.set_timer(self.wheel_rotate,self.wheel_ue_speed)

    def rotating_wheel(self,obj_wheel,obj_wheel_rotation,obj_wheel_x,obj_wheel_y):
        self.rotated_wheel = pygame.transform.rotate(obj_wheel, obj_wheel_rotation)
        self.w, self.h = self.rotated_wheel.get_size()
        self.wheel_draw_pos = Vector2(obj_wheel_x-self.w/2, obj_wheel_y-self.h/2)
