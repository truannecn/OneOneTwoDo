from cmu_graphics import *
from landing import *
from scheduler import *
from timerPage import *
from taskPage import *
import string

def planner_redrawAll(app):
    drawTaskView(app)
    drawPlannerView(app)
    # drawScrollBar(app)
    drawBackPageButton(app)
    drawForwardPageButton(app)
    
    
def drawTaskView(app):
    # outer rectangle
    drawRect(app.width/2 - app.width/3, 125, app.width/3, app.height * .80, fill = None, border = 'black')

    # draw task boxes
    nextDrawnY = 135
    for i in range(len(app.tasks)):
        currTaskBox = app.tasks[i]
        currTaskBox.initalizeBox((app.width/2) - (app.width/3) + 15, nextDrawnY)
        currTaskBox.drawBox()
        nextDrawnY += currTaskBox.height + 10


def drawScrollBar(app):
    viewHeight = app.taskViewHeight
    totalHeight = len(app.tasks) * (max(task.height for task in app.tasks) + 10)  # Total content height
    scrollBarHeight = max(20, viewHeight * (viewHeight / totalHeight))  # Proportional height
    scrollBarY = (app.taskScrollOffset / totalHeight) * viewHeight  # Proportional Y position

    # Draw the scroll bar
    drawRect(app.taskViewLeft + app.taskViewWidth, scrollBarY, 10, scrollBarHeight, fill='darkgrey')

def drawBackPageButton(app):
    drawRect(100, 100, 50, 50)

def drawForwardPageButton(app):
    drawRect(100, 300, 50, 50)
    
def inBackPageButton(app, mouseX, mouseY):
    return 100 < mouseX < 150 and 100 < mouseY < 150

def inForwardPageButton(app, mouseX, mouseY):
    return 100 < mouseX < 150 and 300 < mouseY < 350

    
def drawPlannerView(app):
    drawRect(app.width/2, 125, app.width/2.25, app.height *.80, fill = None, border = 'black')



def planner_onMousePress(app, mouseX, mouseY):
    if inBackPageButton(app, mouseX, mouseY) and app.taskCurrPage > 1:
        app.taskCurrPage -= 1
        print(app.taskCurrPage)
        
    if inForwardPageButton(app, mouseX, mouseY) and app.taskCurrPage < app.taskTotalPages:
        app.taskCurrPage += 1
        print(app.taskCurrPage)

def planner_onMouseDrag(app, mouseX, mouseY):
    pass
