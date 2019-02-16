import __builtin__

class Asteroid:
    
    ## field var
    radIncrement=0
    diameter=0
    angle=0
    vel=3
    xPos=0 
    yPos=0 
    xVel=0
    yVel=0

    def __init__(self,xPos,yPos,angle,radIncrement):
        self.xPos=xPos
        self.yPos=yPos
        self.angle=angle
        self.radIncrement=radIncrement
    
    ## draws an asteroid shape
    def drawAst(self):
        self.move()
        stroke("#FF0000")
        noFill()
        ellipse(self.xPos,self.yPos,self.diameter,self.diameter)
        noStroke()
    
    ## moves the asteroid
    def move(self):
        self.teleport()
        
        self.diameter=self.radIncrement*40
        self.xVel=self.vel*cos(self.angle)
        self.yVel=self.vel*sin(self.angle)
        
        self.xPos+=self.xVel
        self.yPos+=self.yVel
        
    ## teleports asteroid when off screen
    def teleport(self):
        if self.xPos<=-self.diameter/2:
            self.xPos=__builtin__.width+self.diameter/2-1
        if self.xPos>=__builtin__.width+self.diameter/2:
            self.xPos=-self.diameter/2+1
        if self.yPos<=-self.diameter/2:
            self.yPos=__builtin__.height+self.diameter/2-1
        if self.yPos>=__builtin__.height+self.diameter/2:
            self.yPos=-self.diameter/2+1
