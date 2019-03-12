# Write your code here :-)
import pygame, sys, os, inspect, time, random
from pathlib import Path
from random import shuffle
import tkinter as tk




#Some initiation procedures we need
clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()


#colors
#------------------------------------------
green = (0, 255, 0)
lgreen = (0, 150, 0)
red = (255, 0 , 0)
lred = (150, 0,  0)
orange = (253, 106, 2)
lorange = (249, 166, 2)
black = (0, 0, 0)
teal = (102, 178, 178)
lteal = (0, 128, 128)
pink = (253, 158, 178)
lpink =  (249, 80, 135)
#Function for calculating difficulty level

#I'm pretty sure using global is excessive as diff
#should already be a global variable but I did it anways
#------------------------------------------
diff = 0

#Looping mechanisms to complement difficulty

balanced_list = []
final_list = []
def reset_balance():
    global balanced_list, final_list
    balanced_list = [1] * diff + [0] * (20 - diff - 3)
    shuffle(balanced_list)
    final_list = [0] * 3 + balanced_list

def loop_function(passfail):
    global final_list
    del final_list[0]
    final_list = final_list + [passfail]
    print(final_list)
    print(sum(final_list))
    print(diff)
    print(checker)
    
def set_difficulty(diff_to):
    global diff
    diff = 5*diff_to
    reset_balance()


set_difficulty(2)
#sets initial difficulty to 2 (10 balance/20 seconds)

#Button coding
#------------------------------------------
selected_diff_X = 400
selected_diff_Y = 450

def change_highlight(xpos, ypos):
    global selected_diff_X, selected_diff_Y
    selected_diff_X = xpos
    selected_diff_Y = ypos
    
def selectbutton(msg,x,y,w,h,ic,ac,typeof, action=None,act_arg=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, black, [x, y, w, h], 2)
    if typeof == 1:
        
        if x+w >= selected_diff_X >= x and y+h >= selected_diff_Y >= y:
            pygame.draw.rect(gameDisplay, black, [x, y, w, h], 5)
        
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        

        if click[0] == 1 and action:
            timme = clock.tick()
            time_since_last = clock.get_time()
            if time_since_last > 300:
                if typeof == 1:
                    change_highlight(x, y)
                if act_arg:
                    action(act_arg)
                elif act_arg == None:
                    action()
            
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)




#not quite sure what this is but it seems to be coding for custom fonts
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

    


#-------------------------------------------------
#Making list of all mp3 files in current directory

def load_music(path):
    songs = []
    for filename in os.listdir(path):
        if filename.endswith('.mp3'):
            songs.append(os.path.join(path, filename))
    return songs
    
dir_path = os.path.dirname(os.path.realpath('PostArduino.py'))
listsong = load_music(dir_path)
current_song = ""

song_pos = 0

def load():
    global current_song
    pygame.mixer.music.load(listsong[song_pos])
    current_song = listsong[song_pos]
    current_song = current_song[(len(dir_path)+1):]
    print(current_song)
    if len(current_song) > 20:
        current_song = current_song[:(45-len(current_song))] + "..."

def shuffle_music():
    global song_pos
    pygame.mixer.music.stop()
    song_pos = 0
    shuffle(listsong)
    load()
    reset_balance()
    pygame.mixer.music.play()
    pygame.event.wait()


def load_next():
    global song_pos
    song_pos = (song_pos + 1) % len(listsong)
    # Go to the next song (or first if at last).
    load()

def skip_forward():
    pygame.mixer.music.stop()
    load_next()
    pygame.mixer.music.play()
    
def skip_backward():
    global song_pos
    pygame.mixer.music.stop()
    song_pos = (song_pos - 1) % len(listsong)
    load()
    pygame.mixer.music.play()
    



#GameLoop-------------------------------------------


global checker
checker = 0
def trigger_pos():

    pygame.mixer.music.unpause()

def trigger_neg():
    pygame.mixer.music.pause()
    
gameDisplay=pygame.display.set_mode((800, 600))
gameloop = True
if __name__ == '__main__':
    while gameloop:
    
        gameDisplay.fill((255,255,255))
        largeText = pygame.font.Font('freesansbold.ttf',80)
        smallText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Welcome to the Music Mat Companion App!", smallText)
        TextRect.center = ((800/2),(150))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Kneel on the Mat to begin.", smallText)
        TextRect.center = ((800/2),(200))
        gameDisplay.blit(TextSurf, TextRect)    

        selectbutton("Easy",230,350,100,50,green,lgreen,1,set_difficulty,1)
        selectbutton("Normal",350,350,100,50,orange,lorange,1,set_difficulty,2)
        selectbutton("Hard",480,350,100,50,red,lred,1,set_difficulty,3)

        selectbutton("Shuffle",350,480,100,50,teal,lteal,2,shuffle_music)
        selectbutton("|<<",351,531,48,49,pink,lpink,2,skip_backward)
        selectbutton(">>| ", 401,531,48,49,pink,lpink,2,skip_forward)
        selectbutton("Current song: "+ current_song, 0, 0, 800, 50, teal, teal, 2)
        pygame.display.update()
        #clock.tick(20)
    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    trigger_pos()
                    checker = 1;
                elif event.key == pygame.K_s:
                    trigger_neg()
                    checker = 0;
                elif event.key == pygame.K_a:
                    checker = 1;
                    load()
                    reset_balance()
                    pygame.mixer.music.play()
                    pygame.event.wait()
                elif event.key == pygame.K_n:
                    loop_function(1)
                elif event.key == pygame.K_m:
                    loop_function(0)
                elif event.key == pygame.K_d:
                    #print("hello?")
                    checker = 0
                    pygame.mixer.music.stop()
            elif event.type == pygame.USEREVENT:
                load_next()

        if sum(final_list) < diff and checker == 1:
            trigger_neg()
                
        elif sum(final_list) >= diff and checker == 1:
            trigger_pos()

            
