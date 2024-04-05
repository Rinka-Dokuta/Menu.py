import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200,800)) #screen is a rectangle, not square!
pygame.display.set_caption("game states with mouse menu")
WHITE = (255, 255, 255)
BlACK = (0, 0, 0)
font = pygame.font.Font(None, 100)
title_text = font.render("THERE IS NO GAME", True, WHITE)
#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False




#game state variable
state = 1 #1 is menu, 2 is playing, 3 is credits
button1 = False
button2 = False
button3 = False
#add more buttons here!
quitGame = False




while 1: #game loop###########################################################
    
    #input section=========================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #keeps track of mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
        #keyboard input (more needed for actual game)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                quitGame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                quitGame = False
                
                
    #physics/update section=========================================
    print(mousePos)#uncomment for testing
    
    #state 1: menu state!------------------------------
    if state == 1 and mousePos[0]>100 and mousePos[0]<300 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
    else:
        button1 = False
            
    if state == 1 and button1 == True and mouseDown == True:
        state = 2
    #state 2: playing state!---------------------------When button1 pressed
    if state == 2 and quitGame == True: #pressing quit takes you back to menu
        state = 1
    #Button2---------------------------------------------------------------------   
    if state == 1 and mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>400 and mousePos[1]<550:
        button2 = True
    else:
        button2 = False
        
    if state == 1 and button2 == True and mouseDown == True:
        state = 3
    
    if state == 3 and quitGame == True: #pressing quit takes you back to menu
        state = 1
        
    #button3----------------------------------------------------------------------
    if state == 1 and mousePos[0]>700 and mousePos[0]<900 and mousePos[1]>400 and mousePos[1]<550:
        button3 = True
    else:
        button3 = False
        
    if state == 1 and button3 == True and mouseDown == True:
        state = 4
    
    if state == 4 and quitGame == True: #pressing quit takes you back to menu
        state = 1
   
    #regular game physics would go here
    
    
    #render section=========================================
    
    #menu state-------------------------------
    if state == 1:
        screen.fill((230,100,100))# Clear the screen pink
        screen.blit(title_text, (250, 131))
      
        
        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (100, 400, 200, 150))
        else: #when button1 == True or pressed down
            pygame.draw.rect(screen, (200, 250, 200), (100, 400, 200, 150))# 1st box (Color), (position)
        if button2 == False:
            pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))#2nd box
        else:
            pygame.draw.rect(screen, (200, 250, 200), (400, 400, 200, 150))
        if button3 == False:
            pygame.draw.rect(screen, (100, 230, 100), (700, 400, 200, 150))#3rd box
        else:
            pygame.draw.rect(screen, (200, 250, 200), (700, 400, 200, 150))

    
    #game state-------------------------------
    if state == 2:
        screen.fill((80,150,100))# Clear the screen green
     
    if state == 3:
        screen.fill((255,51,51))# Clear the screen red
    
    if state == 4:
        screen.fill((0,0,255))# Clear the screen blue
        #more game stuff would be drawn here
       
    pygame.display.flip()# Update the display

#end of game loop###################################################################
pygame.quit()
