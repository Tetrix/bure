import pygame, sys
from gameobjects.vector2 import Vector2 
from star import Star
 
white, black = (255, 255, 255), (0, 0, 0)
screen_width, screen_height = 640, 480
 
pygame.init()
pygame.display.set_caption('Perfect Collision Detection Example')
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
 
myImage = pygame.image.load("resources/star2/s2_1.png").convert()
myImage.set_colorkey(white)
myOtherImage = pygame.image.load("resources/penguin.png").convert()
myOtherImage = pygame.transform.scale(myOtherImage,(35,55))
myOtherImage.set_colorkey(white)
 
# creating masks for the images
myImage_mask = pygame.mask.from_surface(myImage)
myOtherImage_mask = pygame.mask.from_surface(myOtherImage)
 
# this is where the images are
myImage_rect = myImage.get_rect()
myOtherImage_rect = myOtherImage.get_rect()
 
myImage_rect.topleft = (0, 115)
myOtherImage_rect.topleft = (0, 0)
 
star_rotation=0
sttar_speed=1000
star_event=pygame.USEREVENT + 1
pygame.time.set_timer(star_event,sttar_speed) 
star_rotation_speed=-50.
pygame.mouse.set_visible(False)
rotation_direction=0.0
star_pos = Vector2(447,302)
 
pygame.mouse.set_visible(False)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == star_event:
            rotation_direction=+1.0
        
    myOtherImage_rect.topleft = pygame.mouse.get_pos()
 
    screen.fill(white)

    screen.blit(myOtherImage, myOtherImage_rect.topleft)
    
    # Making the star rotate (bliting the star with same width height & same position)
    rotated_star = pygame.transform.rotate(myImage,star_rotation)
    w2, h2 = rotated_star.get_size()
    star_draw_pos = Vector2(star_pos.x-w2/2, star_pos.y-h2/2) 
    screen.blit(rotated_star, star_draw_pos)
    
    time_passed = clock.tick(80)
    time_passed_seconds = time_passed / 1000.0
    
    #star rotation
    star_rotation += rotation_direction * star_rotation_speed *time_passed_seconds
    
    # this is where we check for pixel perfect collision
    # observe the order mask variables are used in calculating offset and in overlap method
    offset_x, offset_y = (myOtherImage_rect.left - myImage_rect.left), (myOtherImage_rect.top - myImage_rect.top)

    if (myImage_mask.overlap(myOtherImage_mask, (offset_x, offset_y)) != None):
        print 'Collision Detected!'
    else:
        print 'None'

    
     
    pygame.display.update()
    
