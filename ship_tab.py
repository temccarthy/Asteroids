import __builtin__

class Ship:
    
    #field var
    xPos=0
    yPos=0
    angle=0 #angle ship is facing
    dirAngle=0 #angle the ship has to go in order to achieve maximum velocity in direction of angle
    xVel=0 #x and y velocity
    yVel=0
    xVelEnd=0 #x and y max velocity
    yVelEnd=0
    
    #import bullet class
    
    #constructs objects
    def __init__(self,xPos,yPos,angle):
        self.xPos=xPos
        self.yPos=yPos
        self.angle=angle
        
    #movement method
    def move(self): 
        
        #method var
        accel=.045 #rate of acceleration
        maxVel=7 #maximum velocity
        
        #if up is pressed, ship accelerates in direction of dirAngle
        #if up not pressed, ship decelerates to 0
        if __builtin__.upBool==1:
            self.xVelEnd=maxVel*cos(self.angle-PI/2)
            self.yVelEnd=maxVel*sin(self.angle-PI/2)
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
        
        #checks if left or right is pressed, increases/decreases angle according to left or right
        if __builtin__.leftBool==1:
            self.angle -= radians(6)
        if __builtin__.rightBool==1:
            self.angle += radians(6)
        
        #teleporting functions
        if self.xPos<=-10:
            self.xPos=__builtin__.width-1
        if self.xPos>=__builtin__.width+10:
            self.xPos=-9
        if self.yPos<=-10:
            self.yPos=__builtin__.height-1
        if self.yPos>=__builtin__.height+10:
            self.yPos=-9 
                
        #changes position of ship according to velocity
        self.xPos+=self.xVel
        self.yPos+=self.yVel
        
        #rotates ship when left or right is pressed
        pushMatrix()
        
        translate(self.xPos,self.yPos)
        rotate(self.angle)
        
        
        #drawing functions
        noStroke()
        fill(255)
        triangle(0,-20,15,14,-15,14)
        fill(0)
        ellipse(0,4,10,10)
        translate(-self.xPos,-self.yPos)
        
        popMatrix()
