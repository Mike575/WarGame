import random
import pygame
import sys
from pygame.locals import *
from WarGlobalVar import *


class SOLDIER:
    blood = 3
    attackValue = 2

    def checkEdgeRule(self,checkcoord):
        if (checkcoord['x'] > (CELLWIDTH - 1) or\
                checkcoord['x'] < 0 or\
                checkcoord['y'] > (CELLHEIGHT - 1) or\
                checkcoord['y'] < 0):
            print(False)
            return False
        else:
            print(True)
            return True



    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.coord = self.getRandomLocation()
        while (self.checkOverRule(self.coord) == False or
                self.checkEdgeRule(self.coord) == False):
            self.coord = self.getRandomLocation()
        return

    def dead(self,soldier):
        soldier.coord = {'x':-10,'y':-10}

    def checkOverRule(self,coord):
        for key in Army_Status:
            if Army_Status[key].coord['x'] == coord['x'] and\
                    Army_Status[key].coord['y'] == coord['y']:
                return False
        # ensure have already checking everybody Location
        return True

    def getRandomLocation(self):
        return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}

    def searchEnemy(self,step):
        for i in range(1,step):
            for key in Army_Status:
                if abs(Army_Status[key].coord['x'] - self.coord['x'])\
                   + abs(Army_Status[key].coord['y'] - self.coord['y'])\
                   == i and Army_Status[key].blood > 0:
                    return Army_Status[key]
        return None

    def attack(self):
        Enemy = self.searchEnemy(20)
        if Enemy == None:
            self.moveCasually()
        else:
            if self.isInAttackArea(Enemy):
                Enemy.blood = Enemy.blood - self.attackValue
            else:
                self.moveto(Enemy)
                if self.isInAttackArea(Enemy):
                    Enemy.blood = Enemy.blood - self.attackValue
            if Enemy.blood <= 0:
                self.dead(Enemy)

    def moveto(self,Enemy):
        deltax = abs(Enemy.coord['x'] - self.coord['x'])
        deltay = abs(Enemy.coord['y'] - self.coord['y'])
        nextPoint = self.coord
        if deltay > deltax and Enemy.coord['y'] < self.coord['y']:
            nextPoint['y'] = nextPoint['y'] - 1
        elif deltay > deltax and Enemy.coord['y'] >= self.coord['y']:
            nextPoint['y'] = nextPoint['y'] + 1
        elif deltay <= deltax and Enemy.coord['x'] < self.coord['x']:
            nextPoint['x'] = nextPoint['x'] - 1
        elif deltay <= deltax and Enemy.coord['x'] >= self.coord['x']:
            nextPoint['x'] = nextPoint['x'] + 1
        else:
            print('moveto error')
            if (self.checkEdgeRule(nextPoint) == True and self.checkOverRule(nextPoint) == True):
                self.coord = nextPoint





    def isInAttackArea(self,Enemy):
        if abs(Enemy.coord['x'] -self.coord['x'])\
           + abs(Enemy.coord['y'] - self.coord['y'])\
           == 1:
            return True
        else:
            return False


    def moveCasually(self):
        direct = random.randint(1, 4)
        Point = {'x': self.coord['x'], 'y': self.coord['y']}
        print('ok')
        print(self.coord)
        if direct == 1:
            print(1)
            Point['x'] = Point['x']
            Point['y'] = Point['y'] - 1
        elif direct == 2:
            print(2)
            Point['x'] = Point['x']
            Point['y'] = Point['y'] + 1
        elif direct == 3:
            print(3)
            Point['x'] = Point['x'] - 1
            Point['y'] = Point['y']
        else:
            print(4)
            Point['x'] = Point['x'] + 1
            Point['y'] = Point['y']
        if (self.checkEdgeRule(Point) == True and self.checkOverRule(Point) == True):
            self.coord = {'x': Point['x'], 'y': Point['y']}
            print(self.coord)
        print(self.coord)

    def terminate(self):
        pygame.quit()
        sys.exit()

