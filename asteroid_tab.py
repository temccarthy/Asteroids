import __builtin__

class Asteroid:
    #field var
    radIncrement=3
    radius=radIncrement*40
    angle=0#random(0,2*PI)
    vel=1.5
    xPos=0#random(0,600)
    yPos=0#random(0,600)
    xVel=0
    yVel=0
    
    
    #constructor __init__(self,)
    def __init__(self,xPos,yPos,angle):
        self.xPos=xPos
        self.yPos=yPos
        self.angle=angle
    
    #drawAst method
    def drawAst(self):
        self.move()
        stroke("#FF0000")
        noFill()
        ellipse(self.xPos,self.yPos,self.radius,self.radius)
        noStroke()
    
    #movement method
    def move(self):
        
        self.xVel=self.vel*cos(self.angle)
        self.yVel=self.vel*sin(self.angle)
        
        self.xPos+=self.xVel
        self.yPos+=self.yVel
        
        #teleporting functions
        if self.xPos<=-self.radius/2:
            self.xPos=__builtin__.width+self.radius/2-1
        if self.xPos>=__builtin__.width+self.radius/2:
            self.xPos=-self.radius/2+1
        if self.yPos<=-self.radius/2:
            self.yPos=__builtin__.height+self.radius/2-1
        if self.yPos>=__builtin__.height+self.radius/2:
            self.yPos=-self.radius/2+1
        
    #break up method
    
    #collision method
        
