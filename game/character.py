import pygame

main_char = "resources/penguin.png"

class Character(object):
    def __init__(self):
        self.character = pygame.image.load(main_char).convert_alpha()
        self.character=pygame.transform.scale(self.character,(35,55))
        self.rect = self.character.get_rect()
    
    def properties(self):
        self.char_x = 100
        self.char_y = 300
        self.char_speed = 200
