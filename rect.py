
from SOLDIER import *


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    global Army_Status
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption('War')
    initWarGame()
    while True:
        runGame()


def initWarGame():
    DISPLAYSURF.fill(BGCOLOR)
    drawGrid()
    drawPressMsg()
    for i in range(Army_A_Num):
        Army_Status['A'+ str(i)] = SOLDIER('A'+str(i), RED)
    for i in range(Army_B_Num):
        Army_Status['B'+ str(i)] = SOLDIER('B'+str(i), GREEN)

def runGame():
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        checkForKeyPress()
        drawGrid()
        drawPressMsg()

        #----Strategy-----------
        for key in Army_Status:
            if Army_Status[key].color == RED:
                if Army_Status[key].blood > 0:
                    Army_Status[key].moveCasually()
                else:
                    Army_Status[key].dead(Army_Status[key])
            else:
                Army_Status[key].attack()

        #-----------------------

        BlockFlush()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def BlockFlush():
    for key in Army_Status:
        if Army_Status[key].blood > 0:
            drawBlock( Army_Status[key].coord, Army_Status[key].color )
    return

def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
    return None

def drawBlock(coord,color):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    BlockRect = pygame.Rect( x, y, CELLSIZE, CELLSIZE )
    pygame.draw.rect( DISPLAYSURF, color, BlockRect )

def drawGrid():
    for x in range( 2, WINDOWWIDTH, CELLSIZE ):
        pygame.draw.line( DISPLAYSURF, DARKGRAY, (x,2), (x,WINDOWHEIGHT))
    for y in range( 2, WINDOWHEIGHT, CELLSIZE ):
        pygame.draw.line( DISPLAYSURF, DARKGRAY, (2,y), (WINDOWWIDTH,y))

def drawPressMsg():
    pressKeySurf = BASICFONT.render('Press Esc to exit War Game.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 202, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit( pressKeySurf, pressKeyRect )

def drawPressKeyMsg():

    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 202, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()














