import pygame
from sys import exit

pygame.init() #initializes pygame
screen = pygame.display.set_mode((800, 400)) #creates a display surface with width and height stored in a tuple
pygame.display.set_caption("Video Game") #creates a title for the display window
clock = pygame.time.Clock() #creates a clock variable for frame rate

testsurface = pygame.Surface((800, 190))
testsurface.fill('Brown')
grass = pygame.Surface((800, 10))
grass.fill("Green")
while True: #loops over and over 60 times per second
    for event in pygame.event.get(): #looks for event in event.get() 
        if event.type == pygame.QUIT: #if event is quit(X), closes pygame and stops code
            pygame.quit()
            exit()
    screen.blit(testsurface, (0, 210)) #puts a surface on a position in the display surface
    screen.blit(grass, (0, 200))
    '''
    position (0,0) is the top left of the window
    increasing x goes to the right, increasing y goes to the bottom
    '''
    pygame.display.update() 
    clock.tick(90) #updates every second for 60 times.