from cmu_graphics import *

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
    drawLabel('Task List', app.width * .25, app.height * .10, size = 50, font = 'optima')
    
    ## Add Task Button
    drawRect(app.width * .25, (app.height*.10) + 50, 100, 30, align = 'center', fill = None, border = 'black')
    drawLabel('Add Task', app.width * .25, (app.height*.10) + 50, size = 15)
    
    for i in range(len(app.tasks)):
        drawCircle(app.width*.25 - 65, app.height*.10 + 100 + (40*i), 10, fill = None, border = 'black')
        drawLabel(app.tasks[i], app.width*.25 - 50, app.height*.10 + 100 + (40*i), align = 'left', size = 15)

def taskPage_onMousePress(app, mouseX, mouseY):
    if inAddButton(app, mouseX, mouseY):
        response = app.getTextInput('Enter a task')
        time = app.getTextInput('How much time (in minutes) do yu need to complete this task?')
        
        
        currTask = Task(response, time)
        app.tasks.append(currTask)
        currTask.addCircleCoords(app.width*.25 - 65, app.height*.10 + 100 + (40*len(app.tasks)))
    
    for i in range(len(app.tasks)):
        currTask = app.tasks[i]
        print(currTask.taskName, currTask.timeToComplete, currTask.circleCoords)
    
    # for i in range(len(app.circleCoords)):
    #     circleX, circleY = app.circleCoords[i]
    #     if distance(mouseX, mouseY, circleX, circleY) < 10:
    #         app.circleCoords
         
        
def inAddButton(app, mouseX, mouseY):
    return app.width*.25 - 50 < mouseX < app.width*.25 + 50 and app.height*.10 - 35 < mouseY < app.height*.10 + 65

def distance(x0, y0, x1, y1):
    a = (x1-x0) ** 2
    b = (y1- y0) ** 2
    return (a+b) ** 0.5    