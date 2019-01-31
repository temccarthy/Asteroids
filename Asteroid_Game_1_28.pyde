#import tabs
import __builtin__
from ship_tab import Ship
from asteroid_tab import Asteroid

#def main():
__builtin__.width=600
__builtin__.height=600
__builtin__.upBool=0
__builtin__.leftBool=0
__builtin__.rightBool=0
#astLoopBool=1
numbAst=4
#j=0

primaryShip=Ship(__builtin__.width/2,__builtin__.height/2,0)

astList=[]
for i in range(numbAst):
    astObj=Asteroid(random(0,600),random(0,600),random(0,2*PI))
    astList.append(astObj)
    
# print(len(astList))


def setup():
    background(0)
    size(__builtin__.width,__builtin__.height)
   
    
def draw():
    #ship, asteroids
    global primaryShip, anAst, numbAst
    
    #resets screen
    fill(0)
    rect(0,0,__builtin__.width,__builtin__.height)
    

    primaryShip.move()
    
    for i in range(numbAst):
        astList[i].drawAst()
    # ast1.drawAst()
    # ast2.drawAst()
    
    
#checks if buttons are pressed or released on keyboard
def keyPressed():
    global upBool, leftBool, rightBool
    
    if key == CODED:
        if keyCode == UP:
            __builtin__.upBool=1
        elif keyCode == LEFT:
            __builtin__.leftBool=1
        elif keyCode == RIGHT:
            __builtin__.rightBool=1
            
def keyReleased():
    global upBool, leftBool, rightBool
    
    if key == CODED:
        if keyCode == UP:
            __builtin__.upBool=0
        elif keyCode == LEFT:
            __builtin__.leftBool=0
        elif keyCode == RIGHT:
            __builtin__.rightBool=0


# if __name__ == "__main__":
#     main()
