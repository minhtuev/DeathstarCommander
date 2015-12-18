import time
import random
import pygame
import math
import Utils
import SpaceObject
import Ship
import Painter
import sys
#from win32api import GetSystemMetrics
#print "width =", GetSystemMetrics (0)
#print "height =",GetSystemMetrics (1)
'''
Created on Jan 21, 2011

@author: Trezitorul
This is the main class where the central loop of the program will occur
'''

class world():
    painter=0
    lastTime=0
    utils = Utils.gravityPhysics()
    objects=[]
    output=[]
    gameInProgress=True
    deltaT=0
    shipInstructions=[]
    latestId=0
    screenWidth=0
    screenHeight=0
    maxMass=5000.0
    minMass=100.0
    minSpeed=0.0
    maxSpeed=10.0
    numberOfPlanets=2
    maxSize=160
    minSize=40  
    def __init__(self):
        self.screenWidth=800
        self.screenHeight=600
        self.painter = Painter.painter(self.screenWidth,self.screenHeight)
        self.objects.append(Ship.Ship("DeathStar",self.latestId,100.0,1.0,1000,[0,0], self.screenWidth/2,self.screenHeight/2))
        self.latestId+=1
        self.randomPlanetGenerator(self.numberOfPlanets)
        self.mainGameLoop()
    def mainGameLoop(self):
        self.lastTime=time.time()
        while self.gameInProgress:     
            self.deltaT=(time.time()-self.lastTime)
            self.lastTime=time.time()         
            self.updateObjectsCurrentVelocityAndPosition()
            self.clearAccelerations()
            self.updateAcceleration()
            self.parseOutput()
            self.checkEvent()
            self.painter.ClearBackground()
            self.painter.Paint(self.output)
                        
    def checkEvent(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                print "Forward"
                if "thrusterForward" in self.objects[0].modules:
                    self.objects[0].modules["thrusterForward"](self, self.objects[0], self.deltaT)
                #CurrentEvents.append("Forward")
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                print "Forward"
                if "thrusterBackward" in self.objects[0].modules:
                    self.objects[0].modules["thrusterBackward"](self, self.objects[0], self.deltaT)
                #CurrentEvents.append("Forward")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                print "left"
                if "turn" in self.objects[0].modules:
                    self.objects[0].modules["turn"](self, self.objects[0], self.deltaT, math.radians(10))
                #CurrentEvents.append("Left")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                print "Right"
                if "turn" in self.objects[0].modules:
                    self.objects[0].modules["turn"](self, self.objects[0], self.deltaT, math.radians(-10))
                #CurrentEvents.append("Right")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                print "Forward"
                #CurrentEvents.append("Fire")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.gameInProgress=False
                pygame.display.quit()
                sys.exit()
                print "Escape"
                
                #sys.exit()
            else:
                pass
    def randomPlanetGenerator(self, nPlanets):
        position=[0,0]       
        for x in range(nPlanets):
            positionX=0
            positionY=0
            positionX=random.randint(0,self.screenWidth)
            positionY=random.randint(0,self.screenHeight)
            while (self.invalidSpawn(positionX,positionY)==False):
                positionX=random.randint(0,self.screenWidth)
                positionY=random.randint(0,self.screenHeight)
            self.objects.append(SpaceObject.SpaceObject("planet",self.latestId,100.0,1.0,random.randint(self.minMass,self.maxMass),position,positionX,positionY))
            self.latestId+=1
    def invalidSpawn(self,positionX,positionY):
        invalidSpawn = False
        for y in range(len(self.objects)):
            if((positionX-self.objects[y].getPosition()[0])<self.maxSize+self.minSize):
                invalidSpawn=True
            if((positionY-self.objects[y].getPosition()[1])<self.maxSize+self.minSize):
                invalidSpawn=True
            return invalidSpawn
    def parseOutput(self):
        self.output=[]
        spriteSize=0
        for x in range(len(self.objects)):
            spriteSize=0
            spriteSize=self.spriteSizeCalculator(self.objects[x])
            spriteSize=int(spriteSize)
            print spriteSize
            self.output.append([self.objects[x].getType(),self.objects[x].getIdentifier(),self.objects[x].getPosition()[0],self.objects[x].getPosition()[1],spriteSize])
    def spriteSizeCalculator(self,object):
        return self.minSize+self.maxSize*((object.getMass()-self.minMass)/(self.maxMass-self.minMass))
    def parseInput(self):
        pass
    def updateHealth(self):
        pass
    def updateObjectsCurrentVelocityAndPosition(self):
        for x in range(len(self.objects)):
            self.objects[x].updateVelocityAndPosition(self.deltaT,self.screenWidth,self.screenHeight)
    def clearAccelerations(self):
        for x in range(len(self.objects)):
            self.objects[x].clearAcceleration()
    def updateAcceleration(self):
        force =0
        for x in range(len(self.objects)-1):
            force=0
            for y in range(len(self.objects)-x-1):
                force=0
                force=self.utils.calculateGravityForce(self.objects[x].getInstantData(), self.objects[x+y+1].getInstantData())
                force=[-force[0],-force[1]]
                self.objects[x].modifyAcceleration(force)
                force=[-force[0],-force[1]]
                self.objects[x+y+1].modifyAcceleration(force)     
worlds = world()
