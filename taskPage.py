from cmu_graphics import *
from landing import *
from scheduler import *
from timerPage import *

########################################
# TASK CLASSES
########################################
class Task():
    def __init__(self, taskName, timeToComplete):
        self.taskName = taskName
        self.timeToComplete = timeToComplete
        self.taskCompleted = False
        self.circleFill = None
        
    def __repr__(self):
        return f'{self.taskName}'
    
    def addCircleCoords(self, x, y):
        self.circleCoords = (x, y)
        
    def completeTask(self):
        self.circleFill = "black"

########################################
# TASK PAGE
########################################

def taskPage_redrawAll(app):
    
    ## Side Navigation Bar
    
    ##HomeButton
    drawRect(20, app.height*.25, 200, 50, fill = app.homeButtonColor, border = 'black')
    drawLabel('Home', 120, app.height*.25+25, size = 30, font = 'optima')
    
    ## Timer Button
    drawRect(20, app.height*.35, 200, 50, fill = app.timerButtonColor, border = 'black')
    drawLabel('Timer', 120, app.height*.35 + 25, size = 30, font = 'optima')
    
    ## Schedule Button
    drawRect(20, app.height*.35, 200, 50, fill = None, border = 'black')
    
    drawLabel('Task List', app.width * .25, app.height * .10, size = 50, font = 'optima')
    taskX = app.width*.25
    taskY = app.height*.10
    
    ## Add Task Button
    drawRect(taskX + 160, taskY + 6, 100, 30, align = 'center', fill = app.addButtonColor, border = 'black')
    drawLabel('Add Task', taskX + 160, taskY + 6, size = 15)
    
    for i in range(len(app.tasks)):
        currTask = app.tasks[i]
        circleX, circleY = currTask.circleCoords
        drawCircle(circleX, circleY, 10, fill = currTask.circleFill, border = 'black')
        drawLabel(currTask.taskName, circleX + 20, circleY, align = 'left', size = 15)


def taskPage_onMousePress(app, mouseX, mouseY):
    if inAddButton(app, mouseX, mouseY):
        response = app.getTextInput('Enter a task:')
        time = app.getTextInput('Time (in minutes) needed to complete task (must be in a number!):')

        if response != '' and time != '0' and isNum(time):
            currTask = Task(response, time)
            app.tasks.append(currTask)
            currTask.addCircleCoords(app.width*.25 - 65, app.height*.10 + 50 + (40*len(app.tasks)))

    if inHomeButton(app, mouseX, mouseY): 
        app.homeButtonColor = None
        setActiveScreen('landing')
        
    if inTimerButton(app, mouseX, mouseY):
        app.timerButtonColor = None
        setActiveScreen('timerPage')
    
    for i in range(len(app.tasks)):
        currTask = app.tasks[i]
        circleX, circleY = currTask.circleCoords
        if distance(mouseX, mouseY, circleX, circleY) < 10:
            if not currTask.taskCompleted:
                currTask.circleFill = "black"
                currTask.taskCompleted = True
            else:
                currTask.circleFill = None
                currTask.taskCompleted = False
            
def taskPage_onMouseMove(app, mouseX, mouseY):
    if inHomeButton(app, mouseX, mouseY):
        app.homeButtonColor = 'gray'
    else:
        app.homeButtonColor = None
    
    if inAddButton(app, mouseX, mouseY):
        app.addButtonColor = 'gray'
    else:
        app.addButtonColor = None
        
    if inTimerButton(app, mouseX, mouseY):
        app.timerButtonColor = 'gray'
    else:
        app.timerButtonColor = None
        
def inAddButton(app, mouseX, mouseY):
    return app.width*.25 + 160 - 50 < mouseX < app.width*.25 + 160 + 50 and app.height*.10 + 6 - 15 < mouseY < app.height*.10 + 6 + 15

def inHomeButton(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.25 < mouseY < app.height*.25 + 50

def inTimerButton(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.35 < mouseY < app.height*.35 + 50

def isNum(time):
    for chr in time:
        if not chr.isdigit():
            return False
    return True

def distance(x0, y0, x1, y1):
    a = (x1-x0) ** 2
    b = (y1- y0) ** 2
    return (a+b) ** 0.5