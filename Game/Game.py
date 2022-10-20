import pygame
from sys import exit

#initialising pygame
pygame.init() #initializes pygame

#creating a display surface
screen = pygame.display.set_mode((800, 400)) #creates a display surface with width and height stored in a tuple

#changing name of window
pygame.display.set_caption("Video Game") #creates a title for the display window

#creating a clock
clock = pygame.time.Clock() #creates a clock variable for frame rate

'''
Creating a coloured surface
testsurface = pygame.Surface((791, 190))  #first argument = width, second arugment = height
testsurface.fill('Brown')
'''

#Creating a text surface
test_font = pygame.font.Font("Caviar-Dreams/CaviarDreams.ttf", 50)  #first argument = font type, second arguemnt = font size'
text_surface = test_font.render("Game 1", True, (64,64,64))  #first argument = text, second argument = antialiasing, third argument = color
text_rectangle = text_surface.get_rect(center =(400, 50))

#Creating an image surface
sky = pygame.image.load("Graphics/sky.png").convert() #loads an image from the folder and sets it to the background
ground = pygame.image.load("Graphics/ground.png").convert()

#.convert() converts png image

snail_surface = pygame.image.load("Graphics/Snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (600, 300))
 

player_surface = pygame.image.load("Graphics/Player/player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300)) #takes the surface and draws a rectangle around it
framerate = 60 #setting a framerate constant
defaultstart = (0, 0)
defaultend = (800, 400)
while True: #loops over and over 60 times per second
    for event in pygame.event.get(): #looks for event in event.get() 
        if event.type == pygame.QUIT: #if event is quit(X), closes pygame and stops code
            pygame.quit()
            exit()

    screen.blit(sky, (0,0)) #puts a surface on the display surface
    pygame.draw.rect(screen, '#c0e8ec', text_rectangle)  
    pygame.draw.rect(screen, '#c0e8ec', text_rectangle, 10)  #draws a rectangle around our text; 1st param = display surface; 2nd param = color; 3rd param = rectangle to be drawn; 4rd param = width; 5th param = border width
    screen.blit(text_surface, text_rectangle)
    screen.blit(ground, (0, 300))
    
    screen.blit(snail_surface, snail_rectangle)
    #snail movement speed = -10 per frame = -600pixels/second 
    #speed will be the same regardless of framerate
    snail_rectangle.right -= 600/framerate
    if snail_rectangle.right < 0: snail_rectangle.left = 800
    '''
    position (0,0) is the top left of the window
    increasing x goes to the right, increasing y goes to the bottom
    '''
    screen.blit(player_surface,player_rectangle)
    #print(player_rectangle.colliderect(snail_rectangle)) #checks if two rectangles collide
    #if player_rectangle.collidepoint(pygame.mouse.get_pos()): print(pygame.mouse.get_pressed())
    #.get_pressed()creates a tuple where 0th position is left click, 1st position is middle mouse click, 2nd position is right click
    
    pygame.display.update() 
    clock.tick(framerate) #updates every second for 60 times.