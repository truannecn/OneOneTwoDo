from cmu_graphics import *
from landing import *
from scheduler import *
from timerPage import *
import string

########################################
# TASK CLASSES
########################################
class Task():
    def __init__(self, taskName, taskHours, taskMinutes):
        self.taskName = taskName
        self.taskHours = taskHours
        self.taskMinutes = taskMinutes
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
    drawLine(290, 140, 480, 140)
    drawLine(290, 135, 480, 135)
    taskX = app.width*.25
    taskY = app.height*.10
    
    ## Add Task Button
    drawRect(taskX + 160, taskY + 6, 100, 30, align = 'center', fill = app.addButtonColor, border = 'black')
    drawLabel('Add Task', taskX + 160, taskY + 6, size = 15)
    
    drawTasks(app)
    
    if app.onAddTaskPopup:
        drawAddTaskPopup(app)
        
    if allFieldsFilled(app) and app.onAddTaskPopup:
        drawRect(940, 590, 100, 30, fill = None, border = 'black')
        drawLabel('Save', 990, 605, size = 20, font = 'optima')
        
def allFieldsFilled(app):
    return app.currentTask != '' and app.currentHour != '' and app.currentMinute != ''
    
def convertTime(app, time):
    if time < 60:
        return 0, time
    else:
        hours = time // 60
        minutes = time % 60
        return hours, minutes

def drawTasks(app):
    drawLabel('To Do Items:', 360, 170, font = 'optima', size = 20)
    drawLabel('Time Needed:', app.width * .50, 170, font = 'optima', size = 20)
    
    for i in range(len(app.tasks)):
        currTask = app.tasks[i]
        circleX, circleY = currTask.circleCoords
        drawCircle(circleX, circleY, 10, fill = currTask.circleFill, border = 'black')
        drawLabel(currTask.taskName, circleX + 20, circleY, align = 'left', size = 15)
        if currTask.taskHours == 1:
            hour = 'hour'
        elif currTask.taskHours > 1:
            hour = 'hours'
            
        if currTask.taskMinutes == 0:
            drawLabel(f'{currTask.taskMinutes} minutes', app.width * 0.5, circleY, size = 15)
        elif currTask.taskMinutes == 0:
            drawLabel(f'{currTask.taskHours} {hour}', app.width * 0.5, circleY, size = 15)
        else:
            drawLabel(f'{currTask.taskHours} {hour} {currTask.taskMinutes} minutes', app.width * 0.5, circleY, size = 15)
    
        

def taskPage_onMousePress(app, mouseX, mouseY):
    if app.onAddTaskPopup:
        if inSaveButton(app, mouseX, mouseY):
            currTask = Task(app.currentTask, int(app.currentHour), int(app.currentMinute))
            app.onAddTaskPopup = False
            app.tasks.append(currTask)
            currTask.addCircleCoords(app.width*.25 - 65, app.height*.10 + 80 + (40*len(app.tasks)))
    
    if inAddButton(app, mouseX, mouseY):
        # response = app.getTextInput('Enter a task:')
        # time = app.getTextInput('Time (in minutes) needed to complete task (must be in a number!):')
        app.onAddTaskPopup = True
        
        
        # if response != '' and time != '0' and isNum(time):
        #     currTask = Task(response, int(time))
        #     app.tasks.append(currTask)
        #     currTask.addCircleCoords(app.width*.25 - 65, app.height*.10 + 80 + (40*len(app.tasks)))

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
    
    ########
    # POPUP 
    ########    
    if inTaskBox(app, mouseX, mouseY):
        app.taskBoxFill = 'lightGray'
        app.hourBoxFill = None
        app.minuteBoxFill = None
        app.inTaskBox = True
        app.inHourBox = False
        app.inMinuteBox = False
        
    elif inHourBox(app, mouseX, mouseY):
        app.hourBoxFill = 'lightGray'
        app.minuteBoxFill = None
        app.taskBoxFill = None
        app.inHourBox = True
        app.inTaskBox = False
        app.inMinuteBox = False
        
    elif inMinuteBox(app, mouseX, mouseY):
        app.taskBoxFill = None
        app.hourBoxFill = None
        app.minuteBoxFill = 'lightGray'
        app.inMinuteBox = True
        app.inHourBox = False
        app.inTaskBox = False
    else:
        app.inMinuteBox = False
        app.inHourBox = False
        app.inTaskBox = False
        app.taskBoxFill = None
        app.hourBoxFill = None
        app.minuteBoxFill = None
        
            
def taskPage_onMouseMove(app, mouseX, mouseY):
    if not app.onAddTaskPopup:
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
            
def taskPage_onKeyPress(app, key):
    if app.inTaskBox:
        if key == 'space':
            app.currentTask += ' '
        if key == 'backspace' and app.currentTask != '':
            app.currentTask = app.currentTask[:-1]
        elif len(key) == 1:
            app.currentTask += key
            
    if app.inHourBox:
        if key == 'backspace' and app.currentHour != '':
            app.currentHour = app.currentHour[:-1]
        if key in string.digits:
            if app.currentHour == '':
                app.currentHour += key
            else:
                if int(app.currentHour + key) < 11:
                    app.currentHour += key
    
    if app.inMinuteBox:
        if key == 'backspace' and app.currentMinute != '':
            app.currentMinute = app.currentMinute[:-1]
        if key in string.digits:
            if app.currentMinute == '':
                app.currentMinute += key
            else:
                if int(app.currentMinute + key) < 60:
                    app.currentMinute += key
    
        
        
def drawAddTaskPopup(app):
    print(app.inTaskBox, app.inHourBox, app.inMinuteBox)
    drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 40)
    drawRect(app.width/2, app.height/2, app.width/2.5, app.height/2.5, align = 'center', fill = 'white', border = 'black')
    boxLeft = app.width/2 - (app.width/2.5/2)
    boxTop = app.height/2 - (app.height/2.5/2)
    boxWidth = app.width/2.5
    boxHeight = app.height/2.5
    
    drawLabel('Enter task below:', boxLeft + boxWidth/2, boxTop + 50, size = 20, font = 'optima')
    drawRect(boxLeft + boxWidth/2, boxTop + 90, 400, 40, fill = app.taskBoxFill, border = 'black', align = 'center')
    if not app.inTaskBox and app.currentTask == '':
        drawLabel('Click to type:', boxLeft + boxWidth/2, boxTop + 90, fill = 'gray')
    elif app.inTaskBox or app.currentTask != '':
        drawLabel(app.currentTask, boxLeft + boxWidth/2, boxTop + 90, fill = 'black')
    
    drawLabel('Hours needed:', boxLeft + (boxWidth*0.33), boxHeight + 100, size = 20, font = 'optima')
    drawLabel('(0-10)', boxLeft + (boxWidth*0.33), boxHeight + 120, size = 15, font = 'optima')
    drawRect(boxLeft + (boxWidth*0.33), boxHeight + 165, 60, 35, align = 'center', fill = app.hourBoxFill, border = 'black')
    if not app.inHourBox and app.currentHour == '':
        drawLabel('Click:', boxLeft + (boxWidth*0.33), boxHeight + 165, fill = 'gray')
    elif app.inHourBox or app.currentHour != '':
        drawLabel(app.currentHour, boxLeft + (boxWidth*0.33), boxHeight + 165, fill = 'black')
    
    drawLabel('Minutes needed:', boxLeft + (boxWidth*0.66), boxHeight + 100, size = 20, font = 'optima')
    drawLabel('(0-59)', boxLeft + (boxWidth*0.66), boxHeight + 120, size = 15, font = 'optima')
    drawRect(boxLeft + (boxWidth*0.66), boxHeight + 165, 60, 35, align = 'center', fill = app.minuteBoxFill, border = 'black')
    if not app.inMinuteBox and app.currentMinute == '':
        drawLabel('Click:', boxLeft + (boxWidth*0.66), boxHeight + 165, fill = 'gray')
    elif app.inMinuteBox or app.currentMinute != '':
        drawLabel(app.currentMinute, boxLeft + (boxWidth*0.66), boxHeight + 165, fill = 'black')

def inTaskBox(app, mouseX, mouseY):
    boxLeft = app.width/2 - (app.width/2.5/2)
    boxTop = app.height/2 - (app.height/2.5/2)
    boxWidth = app.width/2.5
    boxHeight = app.height/2.5
    
    taskBoxLeft = boxLeft + boxWidth/2 - 200
    taskBoxTop = boxTop + 90 - 20
    taskBoxWidth = 400
    taskBoxHeight = 40
    return taskBoxLeft < mouseX < taskBoxLeft + taskBoxWidth and taskBoxTop < mouseY < taskBoxTop + taskBoxHeight

def inHourBox(app, mouseX, mouseY):
    boxLeft = app.width/2 - (app.width/2.5/2)
    boxTop = app.height/2 - (app.height/2.5/2)
    boxWidth = app.width/2.5
    boxHeight = app.height/2.5
    
    hourBoxLeft = boxLeft + (boxWidth*0.33) - 30
    hourBoxTop = boxHeight + 165 - 17.5
    hourBoxWidth = 60
    hourBoxHeight = 35
    
    return hourBoxLeft < mouseX < hourBoxLeft + hourBoxWidth and hourBoxTop < mouseY < hourBoxTop + hourBoxHeight

def inMinuteBox(app, mouseX, mouseY):
    boxLeft = app.width/2 - (app.width/2.5/2)
    boxTop = app.height/2 - (app.height/2.5/2)
    boxWidth = app.width/2.5
    boxHeight = app.height/2.5
    
    minuteBoxLeft = boxLeft + (boxWidth*0.66) - 30
    minuteBoxTop = boxHeight + 165 - 17.5
    minuteBoxWidth = 60
    minuteBoxHeight = 35
    
    return minuteBoxLeft < mouseX < minuteBoxLeft + minuteBoxWidth and minuteBoxTop < mouseY < minuteBoxTop + minuteBoxHeight


def inAddButton(app, mouseX, mouseY):
    return app.width*.25 + 160 - 50 < mouseX < app.width*.25 + 160 + 50 and app.height*.10 + 6 - 15 < mouseY < app.height*.10 + 6 + 15

def inHomeButton(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.25 < mouseY < app.height*.25 + 50

def inTimerButton(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.35 < mouseY < app.height*.35 + 50

def inSaveButton(app, mouseX, mouseY):
    return 940 < mouseX < 1040 and 590 < mouseY < 620

def isNum(time):
    for chr in time:
        if not chr.isdigit():
            return False
    return True

def distance(x0, y0, x1, y1):
    a = (x1-x0) ** 2
    b = (y1- y0) ** 2
    return (a+b) ** 0.5