
import pygame
import random #for random position of aliens
import math
from pygame import mixer #to add sound in the game
mixer.init()
pygame.init() #imp lib for pygame
mixer.music.load('background.wav')
mixer.music.play(-1)

#creating a window for our game
screen=pygame.display.set_mode((800,600))

pygame.display.set_caption('SPACE SHOOTER GAME')
icon=pygame.image.load('icon.png') #setting logo and name of game
pygame.display.set_icon(icon)

#if you want to see igm continusly,add it to loop
background=pygame.image.load('bg.png')
sapceshipimg=pygame.image.load('arcade.png')

alienimg=[]
alienx=[]
alieny=[]
alienspeedx=[]
alienspeedy=[]

no_of_aliens=6
for i in range(no_of_aliens):


  alienimg.append(pygame.image.load('enemy.png'))
  alienx.append(random.randint(0,736))
  alieny.append(random.randint(30,150))
  alienspeedx.append(2)
  alienspeedy.append(10)


spaceshipX=370
spaceshipY=480 
changex=0
bulletimg=pygame.image.load('bullet.png')
check= False
bulletx=386
bullety=490
score=0

#creating a condition to window band na ho by using events like click
running=True
 
font=pygame.font.SysFont('Arial',32,'bold')
def score_text():
    img=font.render(f'Score:{score}',True,'white')
    screen.blit(img,(10,10)) 


font_gameover=pygame.font.SysFont('Arial',70,'bold')
 
def gameover():
    img_gameover=font_gameover.render('GAME OVER',True,'white')
    screen.blit(img_gameover,(200,250)) 



while running:
    screen.blit(background,(0,0))
    # value is in form of tuples
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    #setting the movement of sapce ship
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            changex=-3
        if event.key==pygame.K_RIGHT:
            changex=3
        if event.key==pygame.K_UP:
           if check is False:
            mixer.music.load('laser.wav')
            mixer.music.play()
            check= True 
            bulletx=spaceshipX+16
           

    if event.type==pygame.KEYUP:
        changex=0
    spaceshipX+=changex
    if spaceshipX<=0:
        spaceshipX=0
    elif spaceshipX>=736: #800-64
        spaceshipX=736
    
    #setting the movement for alien
    
    for i in range(no_of_aliens):
        #wrting gane over condition
         if alieny[i]>420:
           for j in range(no_of_aliens):
            alieny[j]=2000 
            gameover()
            break

         alienx[i] +=alienspeedx[i]
         if alienx[i]<=0:
           alienspeedx[i]=2
           alieny[i] +=alienspeedy[i]
         if alienx[i]>=736:
          alienspeedx[i]=-2
          alieny[i] +=alienspeedy[i]   
         distance=math.sqrt(math.pow(bulletx-alienx[i],2) +math.pow(bullety-alieny[i],2))
         if distance<27:
             mixer.music.load('explosion.wav')
             mixer.music.play()
             bullety=480
             check=False 
             alienx[i]=random.randint(0,736)
             alieny[i]=random.randint(30,150)
             score= score+1
         screen.blit(alienimg[i] ,(alienx[i] ,alieny[i] ))
        


    if bullety<=0:
           bullety=490 
           check=False 
    
    if check is True: 
            screen.blit(bulletimg,(bulletx,bullety)) 
            bullety -=9

   

    
    screen.blit(sapceshipimg,(spaceshipX,spaceshipY))
    
    score_text()
    pygame.display.update()
