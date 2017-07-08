import pygame
from pygame.locals import *
from sys import exit
pygame.init()
size=FULLSCREEN
img=pygame.transform.scale(pygame.image.load('images/newbattle.jpg'),(1366,768))
screen=pygame.display.set_mode((1366,768),size,32)
largefont=pygame.font.SysFont('Algerian',64)
font=pygame.font.SysFont('Algerian',32)
key='';
ext=False;
while True:
    screen.fill((0,0,0))
    screen.blit(img,(0,0))
    screen.blit(largefont.render('Enter your name',True,(0,0,0)),(400,380))
    screen.blit(font.render(key,True,(0,0,0)),(550,450))
    for event in pygame.event.get():
        if event.type==quit:
            exit();
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit();
                exit();
            if event.key==K_TAB:
                if size==0:
                    size=FULLSCREEN
                else:
                    size=0
                pygame.display.set_mode((1366,768),size,32)
            else:
                if((event.key>=97 and event.key<=122) or event.key==8 or event.key==32 or event.key==13):
                    if(event.key==8):
                        length=len(key)
                        key=key[0:length-1]
                    elif(event.key==32):
                        key+='  ';
                    elif event.key==13:
                        ext=True
                    else:
                        if len(key)<16:
                            key+=pygame.key.name(event.key)
    if ext:
        break
    pygame.display.update()
import target.py
