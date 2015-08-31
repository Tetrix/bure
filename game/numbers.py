zero = 'resources/digits/0.png'
one = 'resources/digits/1.png'
two = 'resources/digits/2.png'
three = 'resources/digits/3.png'
four = 'resources/digits/4.png'
five = 'resources/digits/5.png'
six = 'resources/digits/6.png'
seven = 'resources/digits/7.png'
eight = 'resources/digits/8.png'
nine = 'resources/digits/9.png'
divide = 'resources/digits/delenje.png'
multiply = 'resources/digits/mnozenje.png'
subtract = 'resources/digits/minus.png'
add = 'resources/digits/plus.png'

import pygame
from gameobjects.vector2 import Vector2

class Numbers(object):
    def __init__(self):
        
        self.nula = pygame.image.load(zero).convert()
        self.nula.set_colorkey((0,0,0))
        self.nula_rect = self.nula.get_rect()
        self.nula_mask = pygame.mask.from_surface(self.nula)
            
        self.eden = pygame.image.load(one).convert()
        self.eden.set_colorkey((0,0,0))
        self.eden_rect = self.eden.get_rect()
        self.eden_mask = pygame.mask.from_surface(self.eden)
        
        self.dva = pygame.image.load(two).convert()
        self.dva.set_colorkey((0,0,0))
        self.dva_rect = self.dva.get_rect()
        self.dva_mask = pygame.mask.from_surface(self.dva)
        
        self.tri = pygame.image.load(three).convert()
        self.tri.set_colorkey((0,0,0))
        self.tri_rect = self.tri.get_rect()
        self.tri_mask = pygame.mask.from_surface(self.tri)
        
        self.cetiri = pygame.image.load(four).convert()
        self.cetiri.set_colorkey((0,0,0))
        self.cetiri_rect = self.cetiri.get_rect()
        self.cetiri_mask = pygame.mask.from_surface(self.cetiri)
        
        self.pet = pygame.image.load(five).convert()
        self.pet.set_colorkey((0,0,0))
        self.pet_rect = self.pet.get_rect()
        self.pet_mask = pygame.mask.from_surface(self.pet)
        
        self.sest = pygame.image.load(six).convert()
        self.sest.set_colorkey((0,0,0))
        self.sest_rect = self.sest.get_rect()
        self.sest_mask = pygame.mask.from_surface(self.sest)
        
        self.sedum = pygame.image.load(seven).convert()
        self.sedum.set_colorkey((0,0,0))
        self.sedum_rect = self.sedum.get_rect()
        self.sedum_mask = pygame.mask.from_surface(self.sedum)
        
        self.osum = pygame.image.load(eight).convert()
        self.osum.set_colorkey((0,0,0))
        self.osum_rect = self.osum.get_rect()
        self.osum_mask = pygame.mask.from_surface(self.osum)
        
        self.devet = pygame.image.load(nine).convert()
        self.devet.set_colorkey((0,0,0))
        self.devet_rect = self.devet.get_rect()
        self.devet_mask = pygame.mask.from_surface(self.devet)
        
        self.delenje = pygame.image.load(divide).convert()
        self.delenje.set_colorkey((0,0,0))
        self.delenje_rect = self.delenje.get_rect()
        self.delenje_mask = pygame.mask.from_surface(self.delenje)
        
        self.mnozenje = pygame.image.load(multiply).convert()
        self.mnozenje.set_colorkey((0,0,0))
        self.mnozenje_rect = self.mnozenje.get_rect()
        self.mnozenje_mask = pygame.mask.from_surface(self.mnozenje)
        
        self.minus = pygame.image.load(subtract).convert()
        self.minus.set_colorkey((0,0,0))
        self.minus_rect = self.minus.get_rect()
        self.minus_mask = pygame.mask.from_surface(self.minus)
        
        self.plus = pygame.image.load(add).convert()
        self.plus.set_colorkey((0,0,0))
        self.plus_rect = self.plus.get_rect()
        self.plus_mask = pygame.mask.from_surface(self.plus)
        
        
        
        
        
        
    
       