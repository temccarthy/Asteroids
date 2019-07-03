import __builtin__

class Asteroid:
    
    ## field var
    radIncrement=0
    diameter=0
    angle=0
    vel=2
    xPos=0 
    yPos=0 
    xVel=0
    yVel=0
    rotateAng=0
    astpic = None
    picX=0
    picY=0

    def __init__(self,xPos,yPos,angle,radIncrement):
        self.xPos=xPos
        self.yPos=yPos
        self.angle=angle
        self.radIncrement=radIncrement
        self.rotateAng=0#random(0,2*PI)
        
        self.astpic = loadImage("asteroids.png")
        imageMode(CENTER)
        
        self.resetAstNum()
        #self.astpic = copy(self.astpic,500/4*picX,500/4*picY,500/4,500/4,0,0,self.diameter,self.diameter)
    
    ## draws an asteroid shape
    def drawAst(self):
        
        self.move()
        
        #ellipse(self.xPos,self.yPos,self.diameter,self.diameter)
        pushMatrix()
        
        translate(self.xPos,self.yPos)
        rotate(self.rotateAng)
        
        stroke("#FF0000")
        noFill()
        
        #ellipse(0,0,self.diameter,self.diameter)
        #rect(-50/2,-50/2,50,50)
        
        #image(self.astpic,0,0,50,50)
        copy(self.astpic,500/4*self.picX,500/4*self.picY,500/4,500/4,int(-self.diameter*1.1/2),int(-self.diameter*1.1/2),int(self.diameter*1.1),int(self.diameter*1.1))
        #ellipse(0,0,5,5)
        
        #self.rotateAng+=.01
        noStroke()
        
        popMatrix()
        
        
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
            self.xPos=width+self.diameter/2-1
        if self.xPos>=width+self.diameter/2:
            self.xPos=-self.diameter/2+1
        if self.yPos<=-self.diameter/2:
            self.yPos=height+self.diameter/2-1
        if self.yPos>=height+self.diameter/2:
            self.yPos=-self.diameter/2+1
            
    def resetAstNum(self):
        picNum = int(random(0,16))
        self.picX = picNum%4
        self.picY = picNum//4
