from graphics import *

import random 

win = GraphWin("Tic-Tac-Toe", 600, 600)


b11 = Rectangle(Point(0,0), Point(200,200))
b12 = Rectangle(Point(200,0), Point(400,200))
b13 = Rectangle(Point(400,0), Point(600,200))

b21 = Rectangle(Point(0,200), Point(200,400))
b22 = Rectangle(Point(200,200), Point(400,400))
b23 = Rectangle(Point(400,200), Point(600,400))

b31 = Rectangle(Point(0,400), Point(200,600))
b32 = Rectangle(Point(200,400), Point(400,600))
b33 = Rectangle(Point(400,400), Point(600,600))

def printBoard():
    b11.draw(win)
    b12.draw(win)
    b13.draw(win)
    
    b21.draw(win)
    b22.draw(win)
    b23.draw(win)

    b31.draw(win)
    b32.draw(win)
    b33.draw(win)
    
    
    
def getBox(x, y):
    if(x > 0 and x <= 200 and y > 0 and y <= 200 ):
        return 'b11'

    if(x > 200 and x <= 400 and y > 0 and y <= 200 ):
        return 'b12'

    if(x > 400 and x <= 600 and y > 0 and y <= 200 ):
        return 'b13'

    if(x > 0 and x <= 200 and y > 200 and y <= 400 ):
        return 'b21'

    if(x > 200 and x <= 400 and y > 200 and y <= 400 ):
        return 'b22'

    if(x > 400 and x <= 600 and y > 200 and y <= 400 ):
        return 'b23'

    if(x > 0 and x <= 200 and y > 400 and y <= 600 ):
        return 'b31'

    if(x > 200 and x <= 400 and y > 400 and y <= 600 ):
        return 'b32'

    if(x > 400 and x <= 600 and y > 400 and y <= 600 ):
        return 'b33'





def playerX(mx, my, win, boxes, validMoves):
    box = getBox(mx, my)
    while checkValid(validMoves,box) == False:
        print("That move is invalid! Try again.")
        mouse = win.getMouse()
        mx, my = mouse.getX(), mouse.getY()
        box = getBox(mx, my)
        
    if box == 'b11':
        line1 = Line(Point(50, 50), Point(150, 150))
        line2 = Line(Point(50, 150), Point(150, 50))
        boxes[0] = "x"
        validMoves.remove("b11")
    elif box == 'b12':
        line1 = Line(Point(250, 50), Point(350, 150))
        line2 = Line(Point(250, 150), Point(350, 50))
        boxes[1] = "x"
        validMoves.remove("b12")
    elif box == 'b13':
        line1 = Line(Point(450, 50), Point(550, 150))
        line2 = Line(Point(450, 150), Point(550, 50))
        boxes[2] = "x"
        validMoves.remove("b13")
    elif box == 'b21':
        line1 = Line(Point(50, 250), Point(150, 350))
        line2 = Line(Point(50, 350), Point(150, 250))
        boxes[3] = "x"
        validMoves.remove("b21")
    elif box == 'b22':
        line1 = Line(Point(250, 250), Point(350, 350))
        line2 = Line(Point(250, 350), Point(350, 250))
        boxes[4] = "x"
        validMoves.remove("b22")
    elif box == 'b23':
        line1 = Line(Point(450, 250), Point(550, 350))
        line2 = Line(Point(450, 350), Point(550, 250))
        boxes[5] = "x"
        validMoves.remove("b23")
    elif box == 'b31':
        line1 = Line(Point(50, 450), Point(150, 550))
        line2 = Line(Point(50, 550), Point(150, 450))
        boxes[6] = "x"
        validMoves.remove("b31")
    elif box == 'b32':
        line1 = Line(Point(250, 450), Point(350, 550))
        line2 = Line(Point(250, 550), Point(350, 450))
        boxes[7] = "x"
        validMoves.remove("b32")
    elif box == 'b33':
        line1 = Line(Point(450, 450), Point(550, 550))
        line2 = Line(Point(450, 550), Point(550, 450))
        boxes[8] = "x"
        validMoves.remove("b33")
        
    line1.setOutline("pink")
    line2.setOutline("pink")
    line1.setWidth(5)
    line2.setWidth(5)
    line1.draw(win)
    line2.draw(win)

randX = random.randint(0, 600)
randY = random.randint(0, 600)

def computer(randX, randY, win):
    box = getBox(randX, randY)
    while checkValid(validMoves, box) == False:
        randX = random.randint(0, 600)
        randY = random.randint(0, 600)
        box = getBox(randX, randY)
        
    if box == 'b11':
        center = Point(100,100)
        boxes[0] = "o"
        validMoves.remove("b11")
    elif box == 'b12':
        center = Point(300, 100)
        boxes[1] = "o"
        validMoves.remove("b12")
    elif box == 'b13':
        center = Point(500, 100)
        boxes[2] = "o"
        validMoves.remove("b13")
    elif box == 'b21':
        center = Point(100, 300)
        boxes[3] = "o"
        validMoves.remove("b21")
    elif box == 'b22':
        center = Point(300, 300)
        boxes[4] = "o"
        validMoves.remove("b22")
    elif box == 'b23':
        center = Point(500, 300)
        boxes[5] = "o"
        validMoves.remove("b23")
    elif box == 'b31':
        center = Point(100, 500)
        boxes[6] = "o"
        validMoves.remove("b31")
    elif box == 'b32':
        center = Point(300, 500)
        boxes[7] = "o"
        validMoves.remove("b32")
    elif box == 'b33':
        center = Point(500, 500)
        boxes[8] = "o"
        validMoves.remove("b33")
    
        
    
    circle = Circle(center,50)
    circle.setOutline('purple')
    circle.setWidth(5)
    circle.draw(win)
    
def check(win):
    if boxes[0] == boxes[1] == boxes[2]:
        finishLine = Line(Point(50, 100), Point(550, 100))
        finishLine.setWidth(5)
        finishLine.setOutline("magenta")
        finishLine.draw(win)
        return True
    
    elif boxes[0] == boxes[3] == boxes[6]:
        finishLine = Line(Point(100, 50), Point(100, 550))
        finishLine.setWidth(5)
        finishLine.setOutline("magenta")
        finishLine.draw(win)
        return True
    
    elif boxes[1] == boxes[4] == boxes[7]:
        finishLine = Line(Point(300, 50), Point(300, 550))
        finishLine.setWidth(5)
        finishLine.setOutline("magenta")
        finishLine.draw(win)
        return True

    elif boxes[2] == boxes[5] == boxes[8]:
        finishLine = Line(Point(500, 50), Point(500, 550))
        finishLine.setWidth(5)
        finishLine.setOutline("magenta")
        finishLine.draw(win)
        return True

    elif boxes[0] == boxes[4] == boxes[8]:
        finishLine = Line(Point(50, 50), Point(550, 550))
        finishLine.setWidth(5)
        finishLine.setOutline("magenta")
        finishLine.draw(win)
        return True

    elif boxes[2] == boxes[4] == boxes[6]:
        finishLine = Line(Point(550, 50), Point(50, 550))
        finishLine.setWidth(5)
        finishLine.setOutline("magenta")
        finishLine.draw(win)
        return True
    elif boxes[3]== boxes[4]== boxes[5]:
        finishLine = Line(Point(50, 300), Point(550, 300))
        finishLine.setWidth(5)
        finishLine.setOutline("magenta")
        finishLine.draw(win)
        return True
    elif boxes[6] == boxes[7] == boxes[8]:
        finishLine = Line(Point(50, 500), Point(550, 500))
        finishLine.setWidth(5)
        finishLine.setOutline("magenta")
        finishLine.draw(win)
        return True
    
def checkValid(validMoves, box):
    if box in validMoves:
        return True
    else:
        return False
        
validMoves = ['b11', 'b12', 'b13', 'b21','b22', 'b23', 'b31', 'b32', 'b33']    
        
boxes = ['b11', 'b12', 'b13', 'b21','b22', 'b23', 'b31', 'b32', 'b33']

    
    
printBoard()
mouse = win.getMouse()
mx, my = mouse.getX(), mouse.getY()
randX = random.randint(0, 600)
randY = random.randint(0, 600)
while True:
    playerX(mx, my, win, boxes, validMoves)
    if check(win) == True:
        print("Congradulations! You won against the computer!")
        break
    computer(randX, randY, win)
    if check(win) == True:
        print("Aw man! You lost to the computer :(")
        break
    
    mouse = win.getMouse()
    mx, my = mouse.getX(), mouse.getY()
    randX = random.randint(0, 600)
    randY = random.randint(0, 600)
    




