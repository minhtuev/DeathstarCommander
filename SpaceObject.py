'''
Created on Jan 21, 2011

@author: Trezitorul
This is the parent class for all space objects in the game, this will include the ships,planets, and projectiles
'''

import Utils
class SpaceObject:
    util=Utils.gravityPhysics()
    def __init__(self,type,id,health,lives,mass,velocity,x,y):
        self.setType(type)
        self.setPosition(x, y)
        self.setMass(mass)
        self.velocity=velocity
        self.setLives(lives)
        self.health=100
        self.setIdentifier(id)
        self.instantData=[mass,x,y]
    instantData=[0,0,0]#mass,x,y
    position=[0,0]
    velocity=[0,0]
    acceleration=[0,0]
    mass=0
    health=0
    isDead=False
    lives=0
    type=""
    identifier=0
    screenHeight=0
    screenWidth=0
    def clearAcceleration(self):
        self.acceleration=[0,0]
    def setMass(self,mass):
        self.mass = mass
        self.instantData[0]=mass
    def getMass(self):
        return self.mass
    def getInstantData(self):
        return [self.mass,self.position[0],self.position[1]]
    def setType(self,type):
        self.type=type
    def getType(self):
        return self.type
    def setIdentifier(self,identifier):
        self.identifier=identifier
    def getIdentifier(self):
        return self.identifier
    def gravityCalculation(self,ActingGravities):
        pass
    def modifyAcceleration(self,force):
        self.acceleration=self.util.calculateNetAcceleration(self.mass,self.acceleration,force)
    def calculateCurrentLocation(self,deltaT,screenWidth,screenHeight):
        self.position=self.util.calculateCurrentLocation(self.position,self.velocity,deltaT)
        if(self.position[0]>=screenWidth):
            self.position[0]-=screenWidth
        if(self.position[1]>=screenHeight):
            self.position[1]-=screenHeight
        if(self.position[0]<=0):
            self.position[0]+=screenWidth
        if(self.position[1]<=0):
            self.position[1]+=screenHeight
    def calculateCurrentVelocity(self,deltaT):
        self.velocity=self.util.calculateCurrentVelocity(self.velocity,self.acceleration,deltaT)
    def updateVelocityAndPosition(self,deltaT,screenWidth,screenHeight):
        self.calculateCurrentLocation(deltaT,screenWidth,screenHeight)
        self.calculateCurrentVelocity(deltaT)
    def setPosition(self,x,y):
        self.position=[x,y]
        self.instantData[1]=x
        self.instantData[2]=y
    def getPosition(self):
        return self.position
    def getHealth(self):
        return self.health
    def setHealth(self,health):
        self.health=health
    def hasDied(self):
        return self.isDead
    def getLives(self):
        return self.lives
    def setLives(self,lives):
        self.lives=lives
    def subtractOneLife(self):
        if(self.lives>1):
            self.lives-=1
        else:
            self.isDead=True
