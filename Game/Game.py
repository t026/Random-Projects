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
text_surface = test_font.render("Game 1", True, 'Red')  #first argument = text, second argument = antialiasing, third argument = color

#Creating an image surface
sky = pygame.image.load("Graphics/sky.png") #loads an image from the folder and sets it to the background
ground = pygame.image.load("Graphics/ground.png")

snail_surface = pygame.image.load("Graphics/Snail/snail1.png")
snail_x_pos = 600
snail_y_pos = 265 #constant, snail cannot jump 
while True: #loops over and over 60 times per second
    for event in pygame.event.get(): #looks for event in event.get() 
        if event.type == pygame.QUIT: #if event is quit(X), closes pygame and stops code
            pygame.quit()
            exit()
    
    screen.blit(sky, (0,0)) #puts a surface on the display surface
    screen.blit(text_surface, (100,100))
    screen.blit(ground, (0, 300))
    screen.blit(snail_surface, (snail_x_pos,snail_y_pos))
    if snail_x_pos > 200:
        snail_x_pos -= 1
    '''
    position (0,0) is the top left of the window
    increasing x goes to the right, increasing y goes to the bottom
    '''
    pygame.display.update() 
    clock.tick(60) #updates every second for 60 times.