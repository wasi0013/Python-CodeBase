import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAY = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("ANIME")

#colour setup
BLACK = (0,0,0)
WHITE = (255,255,255)
RED =(255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
catImg=pygame.image.load('cat.png')
catx=10
caty=10
direction ='right'

FPS=30
c=10
fpsClock=pygame.time.Clock()
while True:
    
    if direction =='right':
        catx+=5
        if catx ==280:
            direction = 'down'
            DISPLAY.fill(GREEN)
    elif direction =='down':
        caty+=5
        if caty==220:
            direction ='left'
            DISPLAY.fill(BLUE)
    elif direction =='left':
        catx-=5
        if catx==10:
            direction = 'up'
            DISPLAY.fill(RED)
    elif direction =='up':
        caty-=5
        if caty==10:
            direction ='right'
            DISPLAY.fill(WHITE)
            
    DISPLAY.blit(catImg,(catx,caty))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
    if c==1000:
        FPS=60
        c=0
    else:
        FPS+=1
        c+=1


























