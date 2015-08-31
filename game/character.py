import pygame


main_char = "resources/penguin.png"

class Character(object):
    def __init__(self):


        self.main_char = "resources/penguin.png"
        self.character = pygame.image.load(self.main_char).convert()
        self.character.set_colorkey((0,0,0))
        self.character = pygame.transform.scale(self.character,(45,45))
        self.character_rect = self.character.get_rect()
        self.character_mask = pygame.mask.from_surface(self.character)
    
    def properties(self):
        self.char_x = 100
        self.char_y = 100
        self.char_speed = 170

        
     
    
       
