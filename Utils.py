import math
'''
Created on Jan 21, 2011

@author: Trezitorul
This class contains all of the physics calculations for the program
'''
#This contains all of the physics calculations we need

def rotate(vector, angle):
    v=[0.0, 0.0]
    v[0]=vector[0]*math.cos(angle)+vector[1]*math.sin(angle)
    v[1]=vector[1]*math.cos(angle)-vector[0]*math.sin(angle)
    return v

class gravityPhysics():
    G=1
    def __init__(self):
        pass
    def calculateCurrentVelocity(self,velocity,acceleration,deltaT):
        xvelocity=velocity[0]+acceleration[0]*deltaT
        yvelocity=velocity[1]+acceleration[1]*deltaT
        velocity = [xvelocity,yvelocity]
        return velocity
    def calculateCurrentLocation(self,currentPosition,velocity,deltaT):
        xPos=currentPosition[0]+velocity[0]*deltaT
        yPos=currentPosition[1]+velocity[1]*deltaT
        currentPosition=[xPos,yPos]
        return currentPosition
    def calculateAbsoluteDistance(self,xPosObj1,yPosObj1,xPosObj2,yPosObj2):
        return math.sqrt((xPosObj1-xPosObj2)**2+(yPosObj1-yPosObj2)**2)
    def calculateGravityForce(self,Object1InstantData,Object2InstantData):
        radius=0.0
        radius=self.calculateAbsoluteDistance(Object1InstantData[1],Object1InstantData[2],Object2InstantData[1],Object2InstantData[2])
        force=0.0
        force=((self.G*Object1InstantData[0]*Object2InstantData[0])/(radius**2))
        forceX=(force/radius)*(Object1InstantData[1]-Object2InstantData[1])
        forceY=(force/radius)*(Object1InstantData[2]-Object2InstantData[2])
        force=[forceX,forceY]
        return force
    def calculateNetAcceleration(self,mass,currentAcceleration,force):
        xForceAcceleration=(1.0/mass)*(force[0])   
        yForceAcceleration=(1.0/mass)*(force[1]) 
        xNetAcceleration=0.0
        yNetAcceleration=0.0
        xNetAcceleration=currentAcceleration[0]+xForceAcceleration  
        yNetAcceleration=currentAcceleration[1]+yForceAcceleration
        return [xNetAcceleration,yNetAcceleration]
 
#test=gravityPhysics(1)
#print test.calculateAbsoluteDistance(1, 2, 2, 2)
