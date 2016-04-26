import random, pygame, sys
from pygame.locals import *

FPS = 15
winwidth = 640
winheight = 480
cellsize = 20
assert winwidth % cellsize == 0, "Window width must be a multiple of cell size."
assert winheight % cellsize == 0, "Window height must be a multiple of cell size."
cellwidth = int(winwidth / cellsize)
cellheight = int(winheight / cellsize)

# R G B
WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)
RED = (255, 0, 0)
BLUE = (0,50,50)
GREEN = (0, 255,0)
DGREEN = (0,55,0)
DARKGREEN = ( 0, 155, 0)
DARKGRAY = ( 40, 40, 40)
BGCOLOR = BLUE
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # syntactic sugar: index of the worm's head

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((winwidth, winheight))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snaky(by Wasi))')
    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    # Set a random start point.
    startx = random.randint(5, cellwidth - 6)
    starty = random.randint(5, cellheight - 6)
    wormCoords = [{'x': startx, 'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT
    # Start the apple in a random place.
    apple = getRandomLocation()

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
            elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
            elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
            elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
            elif event.key == K_ESCAPE:
                    terminate()

# check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == cellwidth or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == cellheight:
                return # game over
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return # game over

# check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
# don't remove worm's tail segment
            apple = getRandomLocation() # set a new apple somewhere
        else:
            del wormCoords[-1] # remove worm's tail segment

# move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (winwidth - 200, winheight - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Snaky!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Snaky!', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (winwidth / 2, winheight / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (winwidth / 2, winheight / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


def terminate():
    pygame.quit()
    sys.exit()

def getRandomLocation(): return {'x': random.randint(0, cellwidth - 1), 'y': random.randint(0, cellheight - 1)}

def showGameOverScreen():
 gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
 gameSurf = gameOverFont.render("Game", True, WHITE)
 overSurf = gameOverFont.render('Over', True, WHITE)
 gameRect = gameSurf.get_rect()
 overRect = overSurf.get_rect()
 gameRect.midtop = (winwidth / 2, 10)
 overRect.midtop = (winwidth / 2, gameRect.height + 10 + 25)

 DISPLAYSURF.blit(gameSurf, gameRect)
 DISPLAYSURF.blit(overSurf, overRect)
 drawPressKeyMsg()
 pygame.display.update()
 pygame.time.wait(500)
 checkForKeyPress() # clear out any key presses in the event queue

 while True:
     if checkForKeyPress():
         pygame.event.get() # clear event queue
         return

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (winwidth - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawWorm(wormCoords):
    color_switcher = True
    for coord in wormCoords:
        x = coord['x'] * cellsize
        y = coord['y'] * cellsize
        wormSegmentRect = pygame.Rect(x, y, cellsize, cellsize)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, cellsize - 8, cellsize - 8)
        pygame.draw.rect(DISPLAYSURF, DGREEN if color_switcher else GREEN, wormInnerSegmentRect)
        color_switcher = not color_switcher


def drawApple(coord):
     x = coord['x'] * cellsize
     y = coord['y'] * cellsize
     appleRect = pygame.Rect(x, y, cellsize, cellsize)
     pygame.draw.rect(DISPLAYSURF, RED, appleRect)


def drawGrid():
    for x in range(0, winwidth, cellsize): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, winheight))
    for y in range(0, winheight, cellsize): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (winwidth, y))

if __name__ == '__main__':main()
