#------GAME CONSTANT--------

FPS = 15
Army_Status = {}
Army_A_Num = 100
Army_B_Num = 1


#-----Window setting--------
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple o    f cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple     of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
#---------------------------

#---color setting------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
DARKGRAY = ( 40, 40, 40 )
DARKGREEN = ( 0, 155, 0 )
BGCOLOR = BLACK
#----------------------

