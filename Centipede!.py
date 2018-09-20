'''
*************************************************************************
Name: Alexander Treacy
Student ID: S15106436
Date: 11/01/2016
Course Title: BSc Computer Science
Module title: Software development
Module code: CMP4104
*************************************************************************
'''

#importing modules
import sys
import pygame
import random
import time
from pygame.locals import *
 
pygame.init()
pygame.key.set_repeat(1,1)

#initialising variables (cannot change)
red = (255,0,0)
green = (0, 255, 0)
width = 800
height = 600

screen = pygame.display.set_mode((width, height))

#Creating a caption for the game which will displayed in the window border.
caption = "Centipede!"
pygame.display.set_caption(caption)

#Loading in images for later use and giving each a name.
eatingFood = pygame.mixer.Sound('eatingFood.wav')
snakeHead = pygame.image.load('snakeHead.png')
snakeFood = pygame.image.load('snakeFood.png')
bonusCheese = pygame.image.load('bonusCheese.png')
extraLife = pygame.image.load('extraLife.png')
NumOfLives = pygame.image.load('lives.png')
playButton = pygame.image.load('playButton.png')
helpButton = pygame.image.load('helpButton.png')
exitButton = pygame.image.load('exitButton.png')
minusLife = pygame.image.load('minusLife.png')
border = pygame.image.load('border.png')

#The snake function will give the snake an X and a Y value in list format.
def snake(grid, extlist):
    for XandY in extlist:   
        screen.blit(snakeHead, (XandY[0], XandY[1]))

#This function will allow creation of messages in a simple way when creating one.
#The text, colour, X position and Y position have been defined as a parameter but
#can later be changed (as a parameter) when using the function
def msg(text, colour, posX = 100, posY = 280):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render(text, True, colour)
    screen.blit(screen_text, [posX, posY])

def main_loop():

    #Some variables are being defined for later use.
    background_color = (30,30,150)
    grid = 4.0
    snakeHeadX = 300
    snakeHeadY = 400
    snakeHeadXMove = 0
    snakeHeadYMove = 0
    lives = 3
    score = 0
    extraLifeX = 200
    extraLifeY = 500
    bonusCheeseX = 800
    bonusCheeseY = 600
    gameMenu = True
    gameRun = False
    helpMenuOpen = False
    gameOver = False
    lifeLost = False
    lifeGained = False
    gamePaused = False

    playSelected = False
    exitSelected = False
    helpSelected = False

    framerate = 30
    clock = pygame.time.Clock()

    extlist = []
    amountOfExt = 1
    
    #These variables are random values ranging between 40 and 760 int the X axis
    #and 40 and 550 in the Y axis and will always be a multiple of 10.
    snakeFoodX = (random.randrange(40, 760, 10))
    snakeFoodY = (random.randrange(40, 550, 10))
    
    #This will start the menu screen.
    while gameMenu == True:
        pygame.draw.rect(screen, (127, 127, 127), (0, 0, 800, 600))
        screen.blit(playButton, (50, 150))
        screen.blit(exitButton, (450, 150))
        screen.blit(helpButton, (250, 350))
        msg("Use the arrow keys to highlight and space bar to select", (34, 177, 76), 120, 50)
        
        #This will check for a keypress and if one of the 4 arrow keys are pressed
        #will change what this does. For example if the left key is pressed
        #the play menu will be selected and others will be deselected if they
        #were once selected.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playSelected = True
                    exitSelected = False
                    helpSelected = False
                elif event.key == pygame.K_RIGHT:
                    exitSelected = True
                    playSelected = False
                    helpSelected = False
                elif event.key == pygame.K_DOWN:
                    helpSelected = True
                    playSelected = False
                    exitSelected = False
                elif event.key == pygame.K_UP:
                    playSelected = True
                    exitSelected = False
                    helpSelected = False
                elif event.key == pygame.K_SPACE:
                    
                    #Here is the selection of each button on the main menu. It checks which
                    #option is selected and will activate one of the buttons depending on
                    #which was selected.
                    if playSelected == True:
                        gameRun = True
                        gameMenu = False
                        helpMenuOpen = False
                    if exitSelected == True:
                        helpMenuOpen = False
                        pygame.quit()
                        sys.exit()
                    if helpSelected == True:
                        helpMenuOpen = True
                        if event.key == pygame.K_RETURN:
                            main_loop()
                            
        #These statements will check if a specific menu is selected using the above
        #if statements. If one is true then a border will appear around the button.
        if helpSelected == True:
            screen.blit(border, (248, 348))
            screen.blit(helpButton, (250, 350))
        elif playSelected == True:
            screen.blit(border, (48, 148))
            screen.blit(playButton, (50, 150))
        elif exitSelected == True:
            screen.blit(border, (448, 148))
            screen.blit(exitButton, (450, 150))
            
        #This message will appear on the screen when the player accesses the help menu.
        if helpMenuOpen == True:
            pygame.draw.rect(screen, (127, 127, 127), (0, 0, 800, 600))
            msg("Collect the apples (red squares) to collect points. You can", green, 50, 50)
            msg("collect bonus points which will be given if you collect", green, 50, 100)
            msg("cheese. You only have 3 lives but more can be gained by ", green, 50, 150)
            msg("collecting the heart. Points earned and amount of", green, 50, 200)
            msg("lives you have are shown at the bottom of the screen. Use the", green, 50, 250)
            msg("arrow keys to move the centipede around and eat what", green, 50, 300)
            msg("you can find. If you crash into yourself or if you move back", green, 50, 350)
            msg("on yourself then you lose a life. If you lose all of your lives", green, 50, 400)
            msg("it will be over and you will have to start again. You can also", green, 50, 450)
            msg("pause the game if you need to using the ""P"" key. GOOD LUCK!", green, 50, 500)
            msg("Press ""space"" to return to the menu", green, 50, 550)
            
            #If the user presses space in the help menu then it will return
            #them to the main menu. The time.sleep will case the program to
            #wait 0.5 seconds to stop them from holding down the button and
            #reopening the help menu.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        time.sleep(0.2)
                        helpMenuOpen = False
                        main_loop()       
        pygame.display.update()
        
    #This will start the actual game and will start the "clock".
    while gameRun == True:
        gametime = clock.get_time()
        clock.tick(framerate)
        
        #This is a simple pause menu. The centipede will stop when the "p"
        #key is pressed and when it is pressed again the centipede will
        #continue moving. Also a message is printed to the screen.
        while gamePaused == True:
            snakeHeadX = snakeHeadX
            snakeHeadY = snakeHeadY
            msg("game paused, press ""p"" to unpause", green, 150, 200)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        time.sleep(0.2)
                        gamePaused = False
                        pygame.display.update()
                        
        #This while loop will start if the "gameOver" variable is true and will
        #print a a message onto the screen informing the player of their loss.
        #the screen will then update.
        while gameOver == True:
            background_color = (30,30,150)
            msg("Game Over! You scored: %d" % score, red, 250, 200)
            msg("Press space to return to the menu or Q to quit.", red, 170, 320)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameRun = False
                        gameOver = False
                    elif event.key == pygame.K_SPACE:
                        main_loop()
                        
        #These if statements will check if the centipede has crashed into one of
        #the walls. If it has then the centipede will appear to move through the
        #wall to the oposite side of the screen.
        if snakeHeadX < 0:
            snakeHeadX = snakeHeadX + 800
                
        elif snakeHeadX > 800 - grid:
            snakeHeadX = snakeHeadX - 800

        elif snakeHeadY < 0:
            snakeHeadY = snakeHeadY + 570
                
        elif snakeHeadY > 570 - grid:
            snakeHeadY = snakeHeadY - 570

        #Checking if the "X" in the corner of the game is pressed and if it is the
        #game will end and the window will close.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            #This is what will make the centipede move. It will check to see which key
            #has been pressed and will move corresponding to the button pressed. This
            #is done by the head of the centipede moving in a possitive or negaive
            #direction in either the X or the Y direction.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snakeHeadXMove = - grid
                    snakeHeadYMove = 0
                elif event.key == pygame.K_RIGHT:
                    snakeHeadXMove = + grid
                    snakeHeadYMove = 0
                elif event.key == pygame.K_UP:
                    snakeHeadYMove = - grid
                    snakeHeadXMove = 0
                elif event.key == pygame.K_DOWN:
                    snakeHeadYMove = + grid
                    snakeHeadXMove = 0
                elif event.key == pygame.K_p:
                    gamePaused = True
                    time.sleep(0.2)
                    
        #This code will keep the centipede moving once a direction arrow
        #has been pressed.
        snakeHeadX += snakeHeadXMove
        snakeHeadY += snakeHeadYMove
        
        #This will check that the snake has crashed into a piece of
        #food and then will play a sound, make the food disappear
        #change the location of the food, add another extension onto
        #the centipede, increase the score and speed up the centipede.
        if (snakeHeadX + 10 >= snakeFoodX) and (snakeHeadX <= snakeFoodX + 10):
            if (snakeHeadY + 10 >= snakeFoodY) and (snakeHeadY <= snakeFoodY + 10):
                eatingFood.play()
                snakeFoodX = (random.randrange(40, 760, 10))
                snakeFoodY = (random.randrange(40, 530, 10))
                screen.blit(snakeFood, (snakeFoodX, snakeFoodY))
                amountOfExt = amountOfExt + 1
                score = score + 10
                grid = grid + 0.1
                
        #Making the background and the "snake food# appear.
        screen.fill(background_color)
        screen.blit(snakeFood, (snakeFoodX, snakeFoodY))
        
        #When the player has grown enough this if statement will make
        #the cheese appear.
        if amountOfExt >= 30 and amountOfExt <= 35:
            bonusCheeseX = 370
            bonusCheeseY = 270
            screen.blit(bonusCheese, (bonusCheeseX, bonusCheeseY))
            
        #This will be worth morethan apples and will increase speed
        #more and make the centipede longer than usual.
        if snakeHeadX + 10 >= bonusCheeseX and snakeHeadX <= bonusCheeseX + 10:
            if snakeHeadY + 10 >= bonusCheeseY and snakeHeadY <= bonusCheeseY + 10:
                score = score + 50
                bonusCheeseX = 800
                bonusCheeseY = 600
                amountOfExt = amountOfExt + 3
                grid = grid + 0.3
                
        #When the player has achieved a long enough length they will be
        #able to receive another life. It will appear on the screen and
        #once it has been collected it will move off the screen.
        if amountOfExt >= 40 and amountOfExt <= 45:
            screen.blit(extraLife, (extraLifeX, extraLifeY))
            if snakeHeadX + 10 >= extraLifeX and snakeHeadX <= extraLifeX + 10:
                if snakeHeadY + 10 >= extraLifeY and snakeHeadY <= extraLifeY + 10:
                    lifeGained = True

        if lifeGained == True:
            extraLifeX = 800
            extraLifeY = 600
            lives = lives + 1
            lifeGained = False
            pygame.display.flip()
                    
        #This if statement will activate the game over while loop.
        if lives <= 0:
            gameOver = True
            
        #Appending variables of the centipedes head to the list and
        #appending the extension list to the head.
        snakeHead = []
        snakeHead.append(snakeHeadX)
        snakeHead.append(snakeHeadY)
        extlist.append(snakeHead)

        #The if statement will delete item number 0 in the list
        #giving the appearence that the centipede is moving forward.
        if  amountOfExt < len(extlist):
            del extlist[0]
            
        #If the centipede crashes into itself or moves back on itself then the
        #amount of lives will decrease by one, will moce the snake to a safe
        #position, take away points, stop the snake from growing for a short time
        #and display a message for 3 seconds before resuming the game.
        for snakeCrash in extlist[:-1]:
            if snakeCrash == snakeHead:
                lifeLost = True
        if lifeLost == True:        
            lives = lives - 1
            screen.blit(minusLife, (350, 250))
            msg("%d lives remaining" % lives, red, 320, 350)
            score = score - 20
            amountOfExt = amountOfExt - 5
            snakeHeadX = snakeHeadX - 500
            snakeHeadY = snakeHeadY - 500
            pygame.display.flip()
            time.sleep(3)
            lifeLost = False
            
                
        #Calling the snake function with the variables grid and extlist in the parameters.
        snake(grid, extlist)
        #Drawing the bar at the bottom of the screen to act as a HUD.
        pygame.draw.rect(screen, (0, 0, 0), (0, 570, width, 30))
        #Blit the image for amount of lives in the HUD.
        screen.blit(NumOfLives, (730, 570))
        #Calling the msg function to display messages in the HUD
        #And showing the score and the amount of lives.
        msg("x %d" % lives, red, 765, 575)
        msg("Score: %d" % score, green, 600, 575)
        msg("Press ""p"" to pause the game.", green, 20, 575)
        pygame.display.flip()
    pygame.quit()
    sys.exit()
main_loop()
