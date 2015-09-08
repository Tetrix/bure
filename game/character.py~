import pygame
window_x = 270
window_y = 80
main_char = "resources/penguin.png"
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (window_x,window_y)

class Character(object):
    def __init__(self):


        self.main_char = "resources/penguin.png"
        self.character = pygame.image.load(self.main_char).convert()
        self.character.set_colorkey((0,0,0))
        self.character = pygame.transform.scale(self.character,(45,45))
        self.character_rect = self.character.get_rect()
        self.character_mask = pygame.mask.from_surface(self.character)
        self.char_x = 100
        self.char_y = 100
        self.char_speed = 170
    


        
    def char_out_of_screen(self):
        if self.char_x >= 765:
            self.char_x = 765
        if self.char_x <= 0:
            self.char_x = 0
        if self.char_y <= 0:
            self.char_y = 0
        if self.char_y >= 545:
            self.char_y = 545      
    
       
       

    

    def properties(self):
        self.char_x = 100
        self.char_y = 100
        self.char_speed = 170

        
     

