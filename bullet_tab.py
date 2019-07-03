import __builtin__
from asteroid_tab import Asteroid
class Bullet:
    
    ## field var
    xPos=0
    yPos=0
    xVel=0
    yVel=0
    angle=0
    vel=7
    bulletWidth=2
    bulletHeight=2
    initX=0
    initY=0
    bulletRemoveBool=False
    astRemoveBool=False
    bulletFrames=0
    
    def __init__(self,xPos,yPos,angle,initX,initY):
        self.xPos=xPos
        self.yPos=yPos
        self.angle=angle
        self.initX=initX
        self.initY=initY
    
    ## draws a bullet
    def drawBullet(self):
        self.move()
        noStroke()
        fill("#FFFFFF")
        rect(self.xPos,self.yPos,self.bulletWidth,self.bulletHeight)
        self.bulletFrames+=1
    
    ## moves the bullet
    def move(self):
        self.teleport()
        self.xVel=self.vel*cos(self.angle)
        self.yVel=self.vel*sin(self.angle)
        
        self.xPos+=self.xVel
        self.yPos+=self.yVel
        
    ## teleports the bullet when off screen
    def teleport(self):
        if self.xPos<=-0:
            self.xPos=width+0-1
        if self.xPos>=width+0:
            self.xPos=-0+1
        if self.yPos<=-0:
            self.yPos=height+0-1
        if self.yPos>=height+0:
            self.yPos=-0+1
            
    ## checks collision with an asteroid from astList
    def bulletCollision(self, astList, anAst):
        if dist(self.xPos,self.yPos,anAst.xPos,anAst.yPos)<=anAst.diameter/2:
            if anAst.radIncrement==3:
                __builtin__.score+=20
            elif anAst.radIncrement==2:
                __builtin__.score+=50
            elif anAst.radIncrement==1:
                __builtin__.score+=100
            anAst.radIncrement-=1
            anAst.resetAstNum()
            astList.append(Asteroid(anAst.xPos,anAst.yPos,random(0,2*PI),anAst.radIncrement))
            self.bulletRemoveBool=True
        else:
            self.bulletRemoveBool=False
            self.astRemoveBool=False
        
