# Avishek Santhaliya
# Btech Second Year CSE
# MNNIT
# Snake Game using PyGame


import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((800,600))

# To set the title of the game
pygame.display.set_caption('Snake Game')

# To set the icon of the game
#icon = pygame.image.load('icon.png')
#pygame.display.set_icon(icon)


pygame.display.update()

#img = pygame.image.load('snake.png')

clock = pygame.time.Clock()

block_size = 10
appleSize = 20
FPS_Main = 5
FPS = 30

#Always change the movement variables instead of Frames Per Second
#Increasing FPS increases the processing

smallFont = pygame.font.SysFont( None , 25 )
mediumFont = pygame.font.SysFont( None , 40 )
largeFont = pygame.font.SysFont( None , 60 )

def score( score ):
    text = smallFont.render("Score: "+str(score) , True , black )
    gameDisplay.blit( text , [0,0] )

def pause():

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

        gameDisplay.fill( white )
        message_to_screen(
            "Paused",
            red,
            -100,
            size="large"
        )

        message_to_screen(
            "Press c to continue",
            black
        )

        pygame.display.update()

        clock.tick(FPS_Main)

def startScreen():
    flag = True

    while flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    flag = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to SANVAS Snake Game",
                          green ,
                          -100,
                          "large"
                          )
        message_to_screen("Eat the Fruits and don't hit the walls or yourself",
                          black,
                          -60
                          )
        message_to_screen("Press p to play or q to quit",
                          black,
                          -10
                          )

        pygame.display.update()
        clock.tick(FPS_Main)

    gameLoop()

def apple_gen():
    randAppleX = random.randrange(0, display_width - appleSize )
    # This is so that the apple location is always a multiple of 10 so that it matches location of snake
    # randAppleX = round(randAppleX / 10.0) * 10.0

    randAppleY = random.randrange(0, display_height - appleSize)
    # This is so that the apple location is always a multiple of 10 so that it matches location of snake
    # randAppleY = round(randAppleY / 10.0) * 10.0

    return randAppleX , randAppleY

def snake( block_size , snakeList ):
    for Point in snakeList:
        pygame.draw.rect(gameDisplay, blue, [Point[0], Point[1], block_size, block_size])

def text_objects( text , color , size):
    if size == "small":
        textSurface = smallFont.render( text , True , color )
    elif size == "medium":
        textSurface = mediumFont.render(text, True, color)
    elif size == "large":
        textSurface = largeFont.render(text, True, color)

    return textSurface , textSurface.get_rect()

def message_to_screen( msg , color , y_displace=0 , size = "small" ):

    #screen_text = font.render(msg , True , color )
    #gameDisplay.blit(screen_text , [display_width/2 , display_height/2])

    textSurface , textRect = text_objects(msg,color , size)
    textRect.center = ( display_width / 2 ) , ( display_height / 2 ) + y_displace
    gameDisplay.blit( textSurface , textRect )

def gameLoop():

    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    randAppleX , randAppleY  = apple_gen()

    snakeList = []
    snakeLength = 1

    points = 0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red , -50 , "large")
            message_to_screen(" Press p to play again q to quit." , black )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0 :
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill( white )

        # Drawing the Score text
        score(points)

        # Drawing the Apple.
        pygame.draw.rect( gameDisplay , red , [randAppleX , randAppleY , appleSize ,appleSize ])


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)


        if len(snakeList) > snakeLength:
            del snakeList[0]

        for Point in snakeList[:-1]:
            if Point == snakeHead:
                gameOver = True

        # Drawing the snake
        snake( block_size , snakeList )

        pygame.display.update()

        # This is for when the apple size is same as the snake size
        """if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = apple_gen_X()
            randAppleY = apple_gen_Y()
            snakeLength += 1
        """
        # For the case when apple size can be greater than the snake size
        """if lead_x >= randAppleX and lead_x <= randAppleX + appleSize:
            if lead_y >= randAppleY and lead_y <= randAppleY + appleSize:
                randAppleX = apple_gen_X()
                randAppleY = apple_gen_Y()
                snakeLength += 1
        """

        # For the case when there is atleast some part of the snake hits apple
        # Original Collision Detection

        if lead_x > randAppleX and lead_x < randAppleX + appleSize or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleSize :
            if lead_y > randAppleY and lead_y < randAppleY + appleSize :
                randAppleX, randAppleY = apple_gen()
                snakeLength += 1
                points += 10

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleSize:
                randAppleX , randAppleY = apple_gen()
                snakeLength += 1
                points += 10

        clock.tick(FPS)

    pygame.quit()
    quit()

startScreen()