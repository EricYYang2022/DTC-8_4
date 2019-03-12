# Write your code here :-)
import pygame
import sys
import os
from pathlib import Path
import inspect
import time

def load_music(path):
    songs = []
    for filename in os.listdir(path):
        if filename.endswith('.mp3'):
            songs.append(os.path.join(path, filename))
    return songs

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()


clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()

dir_path = os.path.dirname(os.path.realpath(__file__))
listsong = load_music(dir_path)

#colors
#---------------------
green = (0, 255, 0)
lgreen = (0, 150, 0)
red = (255, 0 , 0)
lred = (150, 0,  0)
orange = (253, 106, 2)
lorange = (249, 166, 2)


#------------------------------------------
diff = 1
def set_difficulty(diff_to):
    diff = 5*diff_to
    print(diff)
    
def button(msg,x,y,w,h,ic,ac,action=None,act_arg=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action:
            print("screw off")
            action(act_arg)         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


    
counter = 1
for file in listsong:
    print(file)
    if counter == 1:
        pygame.mixer.music.load(file)
    else:
        pygame.mixer.music.queue(file)
    counter += 1;



gameDisplay=pygame.display.set_mode((800, 600))

playvar = 0
while True:
    gameDisplay.fill((255,255,255))
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Hi Jaylen!!", largeText)
    TextRect.center = ((800/2),(600/2))
    gameDisplay.blit(TextSurf, TextRect)


    button("EzPz",200,450,100,50,green,lgreen,set_difficulty,1)
    button("Normal",400,450,100,50,orange,lorange,set_difficulty,2)
    button("Tryhard",600,450,100,50,red,lred,set_difficulty,3)
    pygame.display.update()
    clock.tick(15)

    for event in pygame.event.get():
        wasjust = 0
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playvar = 1
                wasjust = 1
            elif event.key == pygame.K_s:
                playvar = 0
                pygame.mixer.music.pause()
            elif event.key == pygame.K_a:
                pygame.mixer.music.play()
                pygame.event.wait()
        if (playvar == 1) and (wasjust == 1):
            pygame.mixer.music.unpause()
