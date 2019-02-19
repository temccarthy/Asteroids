
## Reverse engineering of Asteroids game
## Authors: Tim McCarthy and Veronica Andrews
## Date Started: 1/23/19
## Date Completed: 2/15/19

## For funsies

import __builtin__

__builtin__.width=900
__builtin__.height=600
__builtin__.upBool=False
__builtin__.leftBool=False
__builtin__.rightBool=False
__builtin__.spaceBool=False
__builtin__.score=0
mouseBool=False
enterBool=False

from ship_tab import Ship
from asteroid_tab import Asteroid
from bullet_tab import Bullet

astList = []
bulletList=[]
shipList=[]

shipLives=3
numbAst=3

shipFrames=0
levelFrames=0
gameoverFrames=0

scoreList=[]

gameOverScreenCounter=0

typingString=""
letter=""
keyUpdated=False

############################################

## generates the given number of asteroids
def generateAsteroids(n):
    for i in range(n):
        astX=random(0,__builtin__.width)
        astY=random(0,__builtin__.height)
        if astX>shipList[0].xPos-50 and astX<shipList[0].xPos+50:
            astX=random(0,__builtin__.width)
        if astY>shipList[0].yPos-50 and astY<shipList[0].yPos+50:
            astY=random(0,__builtin__.height)
        astList.append(Asteroid(astX,astY,random(0,2*PI),3))

## increases the level of the game
def levelUp():
    global numbAst, levelFrames
    if len(astList)==0:
        levelFrames+=1
        if levelFrames==60:
            numbAst+=1
            generateAsteroids(numbAst)
            levelFrames=0

## respawns the ship when it collides with an asteroid
def respawnShip():
    global numbAst, shipFrames
    if len(shipList)==0:
        shipFrames+=1
        if shipFrames==60:
            shipList.append(Ship(__builtin__.width/2,__builtin__.height/2,-PI/2))
            shipFrames=0

## draws the bullets when the ship "shoots"
def drawAllBullets():
    if shipList[0].spaceCount==1:
        if len(bulletList)<4:
            anBullet=Bullet(shipList[0].topPoint[0],shipList[0].topPoint[1],shipList[0].angle,shipList[0].topPoint[0],shipList[0].topPoint[1])
            bulletList.append(anBullet)
    
    for x in bulletList:
        x.drawBullet()
        if x.bulletFrames>=45:
            bulletList.remove(x)

## makes the ship invincible for a set amount of time to prevent collisions with asteroids
def asteroidShipInvincibility():
    global shipLives
    if shipList[0].invincibilityBool==False:
        for x in astList:
            shipList[0].shipCollision(astList,x)
            if shipList[0].shipCollisionBool==True:
                shipList.remove(shipList[0])
                shipLives-=1
                break

## checks for collision between bullets and asteroids
def asteroidBulletCollision():
    for x in astList:
        for j in bulletList:
            j.bulletCollision(astList,x)
            if j.bulletRemoveBool==True:
                bulletList.remove(j)
        
        if x.radIncrement==0:
            astList.remove(x)

###################################################

## displays the game over screen
def gameOver():
    textAlign(CENTER)
    textSize(40)
    fill(255)
    text("GAME OVER",__builtin__.width/2,__builtin__.height/2)
    text(__builtin__.score,__builtin__.width/2,__builtin__.height/2+40)
    
## displays the play again button
def playAgain():
    global enterBool, mouseBool
    
    if (mouseX > __builtin__.width/2-100 and mouseX<__builtin__.width/2+100) and \
        (mouseY< __builtin__.height/2+190+7 and mouseY>__builtin__.height/2+190-25):
        textAlign(CENTER)
        textSize(36)
        fill(255)
        text("Play Again",__builtin__.width/2,__builtin__.height/2+192)
        if mouseBool==True:
            resetGame()
    elif enterBool==True:
        resetGame()
    else:
        textAlign(CENTER)
        textSize(32)
        fill(255)
        text("Play Again",__builtin__.width/2,__builtin__.height/2+190)

## resets the game after the play again button is clicked
def resetGame():    
        global gameoverFrames, shipLives, numbAst, typingString, gameOverScreenCounter
        gameoverFrames=0
        shipLives=3
        numbAst=2
        __builtin__.score=0
        typingString=""
        gameOverScreenCounter=0
        for i in range(len(astList)):
            astList.remove(astList[0])
        shipList.append(Ship(__builtin__.width/2,__builtin__.height/2,-PI/2))
    
## displays the score of the player, high score of the game, and lives of the ship
def scoreAndLives():
    global shipLives
    textAlign(LEFT)
    textSize(20)
    fill(255)
    livesDist=0
    livesX=20
    livesY=25
    for i in range(shipLives):
        fill(205)
        triangle(livesX+livesDist+0,livesY-20,livesX+livesDist-14,livesY+14,livesX+livesDist+14,livesY+14)
        fill(0)
        ellipse(livesX+livesDist+0,livesY+4,10,10)
        livesDist+=30
    fill(255)
    text(__builtin__.score,5,60)
    if __builtin__.score<=highScore:
        text("High Score: "+str(highScore),5,80)
    else:
        text("High Score: "+str(__builtin__.score),5,80)

###########################################

## updates the players name as they enter it
def updateTypingString():
    global typingString, keyUpdated, letter
    #print(letter)
    if keyUpdated==False:
        if letter=="" or letter=="\n" or letter==";":
            pass
        elif letter=="\x08":
            typingString=typingString[:-1]
            keyUpdated=True
        else:
            typingString=typingString+letter
            keyUpdated=True
    if keyUpdated==True:
        if letter=="":
            keyUpdated=False    

## reads the high score file and adds values and names in file to a list
def readScoreFile():
    global highScore
    try: 
        scoreFile=open("highScore.txt","r")
    except:
        checkFileExist=open("highScore.txt","w")
        checkFileExist.write("0 Player")
        checkFileExist.close()
        scoreFile=open("highScore.txt","r")
    
    for x in scoreFile:
        a=x.split(";")
        if len(a)!=0:
            scoreList.append((int(a[0]),str(a[1])))
    scoreFile.close()
    
    l=[]
    for x in scoreList:
        l.append(x[0])
    highScore=max(l)
    
## rewrites high score file with updated scores and names
def writeToScoreFile():
    scoreFile=open("highScore.txt","w")
    for x in scoreList:
        scoreFile.write(str(x[0])+";"+str(x[1]))#+"\n")
    scoreFile.close()
    
## displays the game over and name entry screens
def gameOverScreen1():
    global gameoverFrames, typingString, mouseBool, enterBool, gameOverScreenCounter
    gameoverFrames+=1
    if gameoverFrames>=0 and gameoverFrames<120:
        gameOver()
    if gameoverFrames>=120:
        updateTypingString()
        textAlign(CENTER)
        textSize(30)
        fill(255)
        text("Enter Name: "+typingString,__builtin__.width/2,__builtin__.height/2)
        
        if (mouseX > __builtin__.width/2-20 and mouseX<__builtin__.width/2+20) and \
            (mouseY< __builtin__.height/2+30+7 and mouseY>__builtin__.height/2+30-22):
            textSize(22)
            text("OK",__builtin__.width/2,__builtin__.height/2+31)
            if mouseBool==True:
                gameOverScreenCounter+=1
                gameoverFrames=0
        elif enterBool==True:
            gameOverScreenCounter+=1
            gameoverFrames=0
        else:
            textSize(20)
            text("OK",__builtin__.width/2,__builtin__.height/2+30)
        
## displays the high score screen and prompts the player to play again
def gameOverScreen2():
    global gameoverFrames 
    gameoverFrames+=1
            
    fill(255)
    textAlign(CENTER)
    textSize(30)
    text("High Scores",__builtin__.width/2,__builtin__.height/2-170)
    
    scoresHeight=0
    
    textSize(24)
    
    scoreList.sort()
    scoreList.reverse()
    
    if len(scoreList)>10:
        scoreList.pop(10)
    
    for x in scoreList:
        textAlign(RIGHT)
        text(x[0],__builtin__.width/2-20,__builtin__.height/2-130+scoresHeight)
        scoresHeight+=30

    scoresHeight=0
    for x in scoreList:
        textAlign(LEFT)
        text(x[1],__builtin__.width/2+20,__builtin__.height/2-130+scoresHeight)
        scoresHeight+=30
    
    if gameoverFrames>=120:
        playAgain()

############################################

## checks for when mouse is pressed
def mousePressed():
    global mouseBool
    mouseBool=True

## checks for when mouse is released
def mouseReleased():
    global mouseBool
    mouseBool=False

## checks which key is pressed on the keyboard
def keyTyped():
    global letter
    letter=str(key)
    
## checks if certain keys on the keyboard are pressed (space, enter, arrow keys)
def keyPressed():
    global enterBool
    if key == " ":
        __builtin__.spaceBool=True
    if key == "\n":
        enterBool=True
    if key == CODED:
        if keyCode == UP:
            __builtin__.upBool=True
        if keyCode == LEFT:
            __builtin__.leftBool=True
        if keyCode == RIGHT:
            __builtin__.rightBool=True

## checks if any key on the keyboard is released
def keyReleased():
    global letter, enterBool
    if letter==str(key):
        letter=""
    if key == " ":
        __builtin__.spaceBool=False
    if key == "\n":
        enterBool=False
    if key == CODED:
        if keyCode == UP:
            __builtin__.upBool=False
        if keyCode == LEFT:
            __builtin__.leftBool=False
        if keyCode == RIGHT:
            __builtin__.rightBool=False

############################################

def setup():
    background(0)
    size(__builtin__.width,__builtin__.height)
    #frameRate(5)
    
    shipList.append(Ship(__builtin__.width/2,__builtin__.height/2,-PI/2))

    generateAsteroids(numbAst)

    readScoreFile()
    
def draw():
    global shipLives, typingString, gameOverScreenCounter
    
    #resets screen
    fill(0)
    rect(0,0,__builtin__.width,__builtin__.height)
    
    levelUp()
    
    for anAst in astList: 
        anAst.drawAst()
        
    if shipLives > 0:
        respawnShip()
                
        if len(shipList)==1:
            shipList[0].drawShip()
            shipList[0].shooting(bulletList)
            
            drawAllBullets()

            asteroidShipInvincibility()

        asteroidBulletCollision()
        
        scoreAndLives()
    else:
        if gameOverScreenCounter==0:
            gameOverScreen1()
            
        if gameOverScreenCounter==1:
            gameOverScreenCounter+=1        
            
            if typingString=="":
                typingString="Player"
            scoreList.append((__builtin__.score,typingString))
            
            writeToScoreFile()
            
        if gameOverScreenCounter==2:
            gameOverScreen2()
            
##############################################
