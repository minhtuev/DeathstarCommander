import Utils

def thrusterForward(world, ship, deltaT):
    ship.clearAcceleration()
    force=[0.0, 0.0]
    force[0]=100*ship.getMass()*ship.direction[0]
    force[1]=100*ship.getMass()*ship.direction[1]
    ship.modifyAcceleration(force)
    return

def thrusterBackward(world, ship, deltaT):
    ship.clearAcceleration()
    force=[0.0, 0.0]
    force[0]=-100*ship.getMass()*ship.direction[0]
    force[1]=-100*ship.getMass()*ship.direction[1]
    ship.modifyAcceleration(force)
    return

def turn(world, ship, deltaT, angle):
    ship.setDirection(Utils.rotate(ship.direction, angle))
    ship.modules["thrusterForward"](world, ship, deltaT)
    return

class ShipModules():
    type=""
    identification=0
    def getType(self):
        return self.type
    def setType(self,type):
        self.type
    def setIdentification(self,id):
        self.identification=id
    def getIdentification(self):
        return self.identification
    def activate(self,ship):
        pass
