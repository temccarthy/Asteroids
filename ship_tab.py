import __builtin__
from asteroid_tab import Asteroid
from bullet_tab import Bullet

class Ship:
    
    ##field var
    
    dirAngle=0 #angle the ship has to go in order to achieve maximum velocity in direction of angle
    xVel=0 #x and y velocity
    yVel=0
    xVelEnd=0 #x and y max velocity
    yVelEnd=0
    bullDrawnBool=0
    
    #collision checking points
    topPoint=[0,0]
    leftPoint=[0,0]
    rightPoint=[0,0]
    midLeftPoint=[0,0]
    midRightPoint=[0,0]
    midBottomPoint=[0,0]
    
    spaceCount=0
    updateAlready=0
        
    shipCollisionBool=0
    astRemoveBool=0
    
    invincibilityBool=1
    invincibilityFrames=0
    
    transparency=255
    
    def __init__(self,xPos,yPos,angle):
        self.xPos=xPos
        self.yPos=yPos
        self.angle=angle
    
    ## draws a ship   
    def drawShip(self):
        self.move()
        self.invincibility()
        
        #establishes separate rotation matrix
        pushMatrix()
        
        #rotates drawing of ship
        translate(self.xPos,self.yPos)
        rotate(self.angle)
                
        #drawing functions
        noStroke()
        fill(255,self.transparency)
        triangle(20,0,-14,14,-14,-14)
        fill(0,self.transparency)
        ellipse(-4,0,10,10)
        if __builtin__.upBool==1:
            stroke(200,self.transparency)
            noFill()
            triangle(-25,0,-14,7,-14,-7)
            noStroke()
            
        translate(-self.xPos,-self.yPos)
        
        #resets rotation matrix back to 0
        popMatrix()
    
    ## makes the ship invincible for a period of time, the ship blinks during this time
    def invincibility(self):
        if self.invincibilityBool==1:
            self.invincibilityFrames+=1
            
            if self.invincibilityFrames%(7*2)>=0 and self.invincibilityFrames%(7*2)<7:
                self.transparency=255
            if self.invincibilityFrames%(7*2)>=7 and self.invincibilityFrames%(7*2)<7*2:
                self.transparency=0
            elif self.invincibilityFrames>140:
                self.transparency=255
                self.invincibilityFrames=0
                self.invincibilityBool=0
            
    ## moves the ship
    def move(self): 
        self.changingCollisionPoints()
        self.teleport()
        self.turning()
        
        accel=.065 #rate of acceleration
        maxVel=6 #maximum velocity
        
        #if up is pressed, ship accelerates in direction of dirAngle
        #if up not pressed, ship decelerates to 0
        if __builtin__.upBool==1:
            self.xVelEnd=maxVel*cos(self.angle)
            self.yVelEnd=maxVel*sin(self.angle)
        else:
            self.xVelEnd=0
            self.yVelEnd=0
            
        #calculates angle in which ship will travel
        self.dirAngle=atan2(self.yVelEnd-self.yVel,self.xVelEnd-self.xVel)
        
        #calculates velocity of ship as it accelerates or decelerates in the direction of dirAngle
        self.xVel+=accel*cos(self.dirAngle)
        self.yVel+=accel*sin(self.dirAngle)
        
        #corrects margin of error as ship decelerates to 0
        if abs(self.xVel)<=accel and self.xVelEnd==0:
            self.xVel=0
        if abs(self.yVel)<=accel and self.yVelEnd==0:
            self.yVel=0
                    
        #changes position of ship according to velocity
        self.xPos+=self.xVel
        self.yPos+=self.yVel
    
    ## turns the ship based on player input
    def turning(self):
        #checks if left or right is pressed, increases/decreases angle according to left or right
        if __builtin__.leftBool==1:
            self.angle -= radians(6)
        if __builtin__.rightBool==1:
            self.angle += radians(6)
            
        if self.angle>2*PI:
            self.angle-=2*PI
        if self.angle<0:
            self.angle+=2*PI
    
    ## teleports the ship when off screen
    def teleport(self):
        if self.xPos<=-10:
            self.xPos=__builtin__.width-1
        if self.xPos>=__builtin__.width+10:
            self.xPos=-9
        if self.yPos<=-10:
            self.yPos=__builtin__.height-1
        if self.yPos>=__builtin__.height+10:
            self.yPos=-9     
    
    ## sets collision points for ship collision with asteroid
    def changingCollisionPoints(self):
        self.topPoint=[self.xPos+(20)*cos(self.angle),self.yPos+20*sin(self.angle)]
        self.leftPoint=[self.xPos+(14*sqrt(2))*cos(self.angle+3*PI/4),self.yPos+(14*sqrt(2))*sin(self.angle+3*PI/4)]
        self.rightPoint=[self.xPos+(14*sqrt(2))*cos(self.angle+5*PI/4),self.yPos+(14*sqrt(2))*sin(self.angle+5*PI/4)]
        self.midLeftPoint=[self.xPos+(sqrt(58))*cos(self.angle+atan(7/3)),self.yPos+(sqrt(58))*sin(self.angle+atan(7/3))]
        self.midRightPoint=[self.xPos+(sqrt(58))*cos(self.angle+atan(-7/3)),self.yPos+(sqrt(58))*sin(self.angle+atan(-7/3))]
        self.midBottomPoint=[self.xPos+(14)*cos(self.angle+PI),self.yPos+(14)*sin(self.angle+PI)]
        
    ## checks for ship collision with an asteroid from astList
    def shipCollision(self,astList, anAst):
        if dist(self.topPoint[0],self.topPoint[1],anAst.xPos,anAst.yPos) < anAst.diameter/2 or dist(self.leftPoint[0],self.leftPoint[1],anAst.xPos,anAst.yPos) < anAst.diameter/2 or dist(self.rightPoint[0],self.rightPoint[1],anAst.xPos,anAst.yPos) < anAst.diameter/2 or dist(self.midLeftPoint[0],self.midLeftPoint[1],anAst.xPos,anAst.yPos) < anAst.diameter/2 or dist(self.midRightPoint[0],self.midRightPoint[1],anAst.xPos,anAst.yPos) < anAst.diameter/2 or dist(self.midBottomPoint[0],self.midBottomPoint[1],anAst.xPos,anAst.yPos) < anAst.diameter/2:
            if anAst.radIncrement==3:
                __builtin__.score+=20
            elif anAst.radIncrement==2:
                __builtin__.score+=50
            elif anAst.radIncrement==1:
                __builtin__.score+=100
            anAst.radIncrement-=1    
            self.shipCollisionBool=1
            astList.append(Asteroid(anAst.xPos,anAst.yPos,random(0,2*PI),anAst.radIncrement))
        else:
            self.shipCollisionBool=0
            self.astRemoveBool=0
    
    ## shoots a bullet
    def shooting(self, bulletList):
        if __builtin__.spaceBool==1:
            if self.updateAlready==0:
                self.spaceCount=1
            if self.updateAlready==1:
                self.spaceCount=0
            self.updateAlready=1
        if __builtin__.spaceBool==0:
            self.updateAlready=0
