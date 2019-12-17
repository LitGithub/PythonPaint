import pygame
import datetime
import math
import colorsys
pygame.init()#initializes Pygame
pygame.display.set_caption("Mouse events")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
draw = False
#color definitions (you have to add these to the game, and you can add more if you want)
color = (255, 0, 0)
times = 0
pygame.font.init() # init pygame font
font = pygame.font.Font(None, 20)
#rainbow####################################################
def rainbow():
    h1 = colorsys.hsv_to_rgb((((math.ceil((datetime.datetime.now().timestamp() * 1000) / 20)) / 360)), 1, 1)
    (r, g, b) = h1
    r*=255
    g*=255
    b*=255
    r = round(r)
    g = round(g)
    b = round(b)
    return (r, g, b)
#gameloop###################################################
while True:
    COLORS = [(0,0,200), (200, 0,0), (0,200, 0), (200, 200, 0), (200, 0, 200), (0,200,200), (255, 255, 255), (0,0,0), "rainbow", (80, 80, 65)]
    
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
#update/timer section---------------------------------------
    if mousePos[1] > 750:
        number = int(mousePos[0] / 50)
        if number >= len(COLORS):
            number = len(COLORS) - 1
        
        color = COLORS[number]
    if mousePos[1] < 15 and mousePos[0] < 35:
        screen.fill((0,0,0))
    #add other colors here!
#input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        draw = True

    if event.type == pygame.MOUSEBUTTONUP:
        draw = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
 
#render section---------------------------------------------
    if draw == True:
        if color == "rainbow":
            pygame.draw.circle(screen, rainbow(), (mousePos), 10)
        else:
            pygame.draw.circle(screen, color, (mousePos), 10)#player paintbrush
    text = font.render(str("Clear"),1,(0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255),(0, 0,35,15))
    screen.blit(text,(0, 0))
    
    #color changing rectangles at bottom of screen
    
    #more colors go here!
    pygame.draw.rect(screen, (255, 255, 255), (0,745,800,60))
    for i in COLORS:
        if i == "rainbow":
            i = rainbow()
        pygame.draw.rect(screen, i, (0 + (50 * times),750,50,50))
        times = times + 1;
        if times == len(COLORS):
            times = 0
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()


