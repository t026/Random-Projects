import pygame
from sys import exit
import random

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    return []

def collisions(player, obstacles)
#initialising pygame
pygame.init() #initializes pygame

#creating a display surface
screen = pygame.display.set_mode((800, 400)) #creates a display surface with width and height stored in a tuple

#changing name of window
pygame.display.set_caption("Video Game") #creates a title for the display window

#creating a clock
clock = pygame.time.Clock() #creates a clock variable for frame rate

game_active = True
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

#obstacles
snail_surface = pygame.image.load("Graphics/Snail/snail1.png").convert_alpha()
#snail_rectangle = snail_surface.get_rect(midbottom = (600, 300))
fly_surface = pygame.image.load("Graphics/Fly/fly1.png").convert_alpha()
# fly_rectangle = fly_surface.get_rect(midbottom = (600, 300))
obstacle_rect_list = []

player_surface = pygame.image.load("Graphics/Player/player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300)) #takes the surface and draws a rectangle around it

#variables and constants
framerate = 60 #setting a framerate constant
player_gravity = 0 #setting a gravity variable
score = 0
reset = True
doublejump = True
newtime = 0

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

while True: #loops over and over 60 times per second
    for event in pygame.event.get(): #looks for event in event.get() 
        if event.type == pygame.QUIT: #if event is quit(X), closes pygame and stops code
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if player_rectangle.bottom >= 300 or doublejump:
                    player_gravity = -20  #have to figure out how to make this scale with framerate
                    doublejump = False
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active = True
                score = 0
                newtime = pygame.time.get_ticks()/1000
        if event.type == obstacle_timer and game_active:
            if random.randint(0, 1) == 1:
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (random.randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(bottomright = (random.randint(900, 1100), 210)))
    if player_rectangle.bottom == 300: 
        doublejump = True
    if game_active:
        #background
        screen.blit(sky, (0,0)) #puts a surface on the display surface
        pygame.draw.rect(screen, '#c0e8ec', text_rectangle)  
        pygame.draw.rect(screen, '#c0e8ec', text_rectangle, 10)  #draws a rectangle around our text; 1st param = display surface; 2nd param = color; 3rd param = rectangle to be drawn; 4rd param = width; 5th param = border width
        #screen.blit(text_surface, text_rectangle)
        screen.blit(ground, (0, 300))
        
        #snail
        #screen.blit(snail_surface, snail_rectangle)
        #snail movement speed = -10 per frame = -600pixels/second 
        #speed will be the same regardless of framerate
        '''snail_rectangle.right -= 600/framerate
        if snail_rectangle.right < 0: 
            snail_rectangle.left = 800
            reset = True'''

        #player
        player_gravity += 60/framerate
        player_rectangle.y += player_gravity 
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        screen.blit(player_surface,player_rectangle)

        #if snail_rectangle.colliderect(player_rectangle): game_active = False
    
        #score
        time = round(pygame.time.get_ticks()/1000) -round(newtime)
        message = f"Score : {score}, Time : {time}"
        score_surface = test_font.render(message,  True, (64,64,64))
        score_rectangle = score_surface.get_rect(center = (400, 100))
        screen.blit(score_surface, score_rectangle)
        #if player_rectangle.center > snail_rectangle.center and reset: 
            #score += 1
            #reset = False

        '''keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("Ye")'''
        #print(player_rectangle.colliderect(snail_rectangle)) #checks if two rectangles collide
        #if player_rectangle.collidepoint(pygame.mouse.get_pos()): this checks if mouse is on rectangle
        # print(pygame.mouse.get_pressed())
        #.get_pressed()creates a tuple where 0th position is left click, 1st position is middle mouse click, 2nd position is right click
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
    else:
        message = f"Game Over. Your score was : {score}"
        end_surface = test_font.render(message, True, (64,64,64)) 
        end_rectangle = end_surface.get_rect(center = (400,100))
        screen.fill("Red")
        screen.blit(end_surface,end_rectangle)

        
            
    pygame.display.update() 
    clock.tick(framerate) #updates every second for 60 times.