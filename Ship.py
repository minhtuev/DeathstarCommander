'''
Created on Jan 21, 2011

@author: Minh-Tue
This is the ship implementation class of the space object it is here that the modules can be called and activated on the ship
''' 
import SpaceObject
import ShipModules
import Utils
class Ship(SpaceObject.SpaceObject):
    modules={}
    direction=[1,1]
    util=Utils.gravityPhysics()
    modules["thrusterForward"]=ShipModules.thrusterForward
    modules["thrusterBackward"]=ShipModules.thrusterBackward
    modules["turn"]=ShipModules.turn
    def setDirection(self, direction):
        self.direction=direction
        return
    

##    def __init__(self,type,id,health,lives,mass,velocity,x,y):
##        self.setType(type)
##        self.setPosition(x, y)
##        self.setMass(mass)
##        self.velocity=velocity
##        self.setLives(1)
##        self.health=100
##        self.setIdentifier(id)
##        self.instantData=[mass,x,y]
##        self.modules["thruster"]=ShipModules.thruster
    
