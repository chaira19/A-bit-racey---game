import pygame
import time
import random

pygame.init()

display_width= 800
display_height= 600
blue = (0,0,200)
black = (0,0,0)
white = (255,255,255)
red=(200,0,0)
green=(0,200,0)
bright_red=(255,0,0)
pause=True
bright_green=(0,255,0)
car_width=73
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('My_first_game')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
gameIcon = pygame.image.load('carIcon.png')
Highscore1 = 0
dodged1=0
Highscore2 = 0
dodged2 = 0

pygame.display.set_icon(gameIcon)

def car(x,y) :
    gameDisplay.blit(carImg, (x,y))
def things_dodged(count,pos):
    font=pygame.font.SysFont(None,25)
    text= font.render("Dodged: "+str(count), True , black)
    gameDisplay.blit(text, (pos,0))
def things_Highscore(count,pos):
    font=pygame.font.SysFont(None,25)
    text= font.render("Highscore: "+str(count), True , black)
    gameDisplay.blit(text, (pos,25))
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
def game_loop2():
    global Highscore1
    global Highscore2
    pygame.mixer.music.load('jazz.wav')
    pygame.mixer.music.play(-1)
    x1 =  (display_width * 0.45)
    y1 = (display_height * 0.8)
    x1_change = 0
    y1_change = 0
    x2 =  (display_width * 0.45)
    y2 = (display_height * 0.8)
    x2_change = 0
    y2_change = 0
    thing_startx= random.randrange(0,display_width)
    thing_starty= -600
    thing_speed= 7
    thing_width= 100
    thing_height= 100
    dodged1=0
    dodged2=0
    gameExit= False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
                #instead of gameExit = True
                #and print(event)
            gameDisplay.fill(white)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x2_change = -20
                elif event.key == pygame.K_RIGHT:
                    x2_change = 20
                elif event.key == pygame.K_UP :
                    y2_change = -10
                elif event.key == pygame.K_DOWN :
                    y2_change = 10
                elif event.key == pygame.K_p:
                    pause = True #not working if pause isn't a global variable
                    paused()
                elif event.key == pygame.K_a:
                    x1_change = -20
                elif event.key == pygame.K_d:
                    x1_change = 20
                elif event.key == pygame.K_w :
                    y1_change = -10
                elif event.key == pygame.K_s :
                    y1_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x1_change = 0
                if event.key == pygame.K_s or event.key == pygame.K_w :
                    y1_change = 0
                if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                    x2_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                    y2_change = 0
                

        if Highscore1 < dodged1 :
            Highscore1 = dodged1
        if Highscore2 < dodged2 :
            Highscore2 = dodged2
        x2=x2+x2_change
        y2=y2+y2_change
        x1=x1+x1_change
        y1=y1+y1_change
        
        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed
        things_dodged(dodged1,0)
        things_Highscore(Highscore1,0)
        things_Highscore(Highscore2,680)
        things_dodged(dodged2,680)
        car(x1,y1)
        car(x2,y2)
        #if x1>display_width-car_width or x1<0 :
        #    crash()
        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx= random.randrange(0,display_width)
            dodged1 +=1
            thing_speed +=1
            thing_width += (dodged1*1.01)

        #if y<thing_starty+thing_height:
            
            #if x1>thing_startx and x1<thing_startx+thing_width or x1+car_width>thing_startx and x1+car_width<thing_startx+thing_width:
                
                #crash()
        pygame.display.update()
        clock.tick(60)

game_loop2()
