import pygame


main_char = "resources/penguin.png"

class Character(object):
    def __init__(self):
        self.character= pygame.sprite.Sprite()
        self.character.image = pygame.image.load(main_char).convert_alpha()
        self.character.image =pygame.transform.scale(self.character.image,(35,55))
        self.character.mask = pygame.mask.from_surface(self.character.image)
        self.character.rect=self.character.image.get_rect()
    
    def properties(self):
        self.char_x = 100
        self.char_y = 300
        self.char_speed = 300
