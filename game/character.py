import pygame


main_char = "resources/penguin.png"

class Character(object):
    def __init__(self):

        
        self.character = pygame.image.load(main_char).convert()
        self.character.set_colorkey((255,255,255))
        self.character = pygame.transform.scale(self.character,(35,55))
        self.character_rect = self.character.get_rect()
        self.character_mask = pygame.mask.from_surface(self.character)
    
    def properties(self):
        self.char_x = 337
        self.char_y = 482
        self.char_speed = 200

        
        self.character = pygame.image.load(main_char).convert()
        self.character.set_colorkey((0,0,0))
        self.character =pygame.transform.scale(self.character,(35,55))
        self.character_rect = self.character.get_rect()
        self.character_mask = pygame.mask.from_surface(self.character)
    
 
