from cmu_graphics import *
from landing import *
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
        self.page = 1
        
        self.taskFloat = self.taskHours + (self.taskMinutes / 60)
        print(self.taskFloat)
        self.startTimeFloat = 0
        self.endTimeFloat = 0
        
    def __repr__(self):
        return f'{self.taskName}'
    
    def addCircleCoords(self, x, y):
        self.circleCoords = (x, y)
    
    def addDeleteCoords(self, x, y):
        self.deleteCoords = (x, y)
        
    def addEditCoords(self, x, y):
        self.editCoords = (x, y)
        
    def completeTask(self):
        self.circleFill = "black"
        
    def initalizeBox(self, boxLeft, boxTop, baseHeight = 60, width = 430):
        self.totalTimeInHours = self.taskHours + (self.taskMinutes/60)
        ## For the planner view page
        self.boxLeft = boxLeft
        self.boxTop = boxTop
        self.width = width
        self.height = max(70, baseHeight * self.totalTimeInHours)
        self.height = min(app.taskViewTop + app.taskViewHeight - 20, self.height)
        
    def drawBox(self):
        drawRect(self.boxLeft, self.boxTop, self.width, self.height, fill = 'burlyWood', border = 'black')
        drawLabel(self.taskName, self.boxLeft+20, self.boxTop + 20, font = 'optima', size = 25, align = 'left')
    
    def assignEndTime(self):
        self.endTimeFloat = self.startTimeFloat + self.taskFloat
    
    def assignStartDisplay(self):
        if self.startTimeFloat < 12:
            self.startIsAM = True
            halfOfDay = 'am'
        else:
            self.startIsAM = False
            halfOfDay = 'pm'
        
        startHour = self.startTimeFloat // 1
        if startHour > 12:
            startHour %= 12
        
        startHour = int(startHour)
        
        startMinute = (self.startTimeFloat % 1) * 60
        if startMinute < 10:
            startMinute = '0' + str(int(startMinute))
        else:
            startMinute = int(startMinute)
        self.startTimeDisplay = f'{startHour}:{startMinute}{halfOfDay}'
    
    def assignEndDisplay(self):
        if self.endTimeFloat < 12:
            halfOfDay = 'am'
        else:
            halfOfDay = 'pm'
        
        endHour = self.endTimeFloat // 1
        if endHour > 12:
            endHour %= 12
        endHour = int(endHour)
        
        endMinute = (self.endTimeFloat % 1) * 60
        if endMinute < 10:
            endMinute = '0' + str(int(endMinute))
        else:
            endMinute = int(endMinute)
        self.endTimeDisplay = f'{endHour}:{endMinute}{halfOfDay}'
        
        
        
########################################
# TASK PAGE
########################################

def taskPage_redrawAll(app):
    drawImage(app.todoListImage, 0, 0, width = app.width, height = app.height)
    ## Side Navigation Bar
    
    ##HomeButton
    drawHomeButton(app, 20, app.height*.3, 200, 50)
    drawPlannerButton(app, 20, app.height*.4, 200, 50)
    drawTimerButton(app, 20, app.height*.5, 200, 50)
    
    # ## Timer Button
    # drawRect(20, app.height*.35, 200, 50, fill = app.timerButtonColor, border = 'black')
    # drawLabel('Timer', 120, app.height*.35 + 25, size = 30, font = 'optima')
    
    # ## Schedule Button
    # drawRect(20, app.height*.35, 200, 50, fill = None, border = 'black')
    
    drawLabel('Task List', app.width * .25, app.height * .10, size = 50, font = 'optima')
    drawLine(290, 140, 480, 140)
    drawLine(290, 135, 480, 135)
    taskX = app.width*.25
    taskY = app.height*.10
    
    ## Add Task Button
    drawRect(taskX + 160, taskY + 6, 100, 30, align = 'center', fill = app.addButtonColor, border = 'black')
    drawLabel('Add Task', taskX + 160, taskY + 6, size = 15, font = 'optima')
    
    ## Edit mode button
    drawRect(taskX + 270, taskY + 6, 100, 30, align = 'center', fill = app.editButtonFill, border = 'black')
    drawLabel(app.editMessage, taskX + 270, taskY + 6, size = 15, font = 'optima')
    
    drawTasks(app)
    if app.editMode:
        drawEditModeButtons(app)
    
    if app.onAddTaskPopup:
        drawAddTaskPopup(app)
        
    if allFieldsFilled(app) and app.onAddTaskPopup:
        drawRect(940, 590, 100, 30, fill = None, border = 'black')
        drawLabel('Save', 990, 605, size = 20, font = 'optima')
        
def allFieldsFilled(app):
    return app.currentTask != '' and app.currentHour != '' and app.currentMinute != '' and not (int(app.currentHour) == 0 and int(app.currentMinute) == 0)
    
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
        drawLabel(currTask.taskName, circleX + 20, circleY, align = 'left', size = 20, font = 'times new roman')
        if currTask.taskHours == 1:
            hour = 'hour'
        elif currTask.taskHours > 1:
            hour = 'hours'
            
        if currTask.taskHours == 0:
            drawLabel(f'{currTask.taskMinutes} minutes', app.width * 0.5, circleY, size = 20, font = 'times new roman')
        elif currTask.taskMinutes == 0:
            drawLabel(f'{currTask.taskHours} {hour}', app.width * 0.5, circleY, size = 20, font = 'times new roman')
        else:
            drawLabel(f'{currTask.taskHours} {hour} {currTask.taskMinutes} minutes', app.width * 0.5, circleY, size = 20, font = 'times new roman')
    
        

def taskPage_onMousePress(app, mouseX, mouseY):
    if app.editMode:
        for i in range(len(app.tasks)):
            currTask = app.tasks[i]
            deleteLeft, deleteTop = currTask.deleteCoords
            deleteLeft = deleteLeft - 15
            deleteTop -= 15
            
            editLeft, editTop = currTask.editCoords
            editLeft -= 15
            editTop -= 15
            
            if deleteLeft < mouseX < deleteLeft + 30 and deleteTop < mouseY < deleteTop + 30:
                deleteTask(app, i)
                moveOtherTasks(app, i)
                return
            
            if editLeft < mouseX < editLeft + 30 and editTop < mouseY < editTop + 30:
                app.onAddTaskPopup = True
                app.currentTaskBeingEdited = app.tasks[i]
            
        
    
    if app.onAddTaskPopup:
        if app.editMode and not inSaveButton(app, mouseX, mouseY):
            app.currentTask = app.currentTaskBeingEdited.taskName
            app.currentHour = str(app.currentTaskBeingEdited.taskHours)
            app.currentMinute = str(app.currentTaskBeingEdited.taskMinutes)
            
        if inSaveButton(app, mouseX, mouseY):
            if not app.editMode:
                currTask = Task(app.currentTask, int(app.currentHour), int(app.currentMinute))
                app.onAddTaskPopup = False
                app.tasks.append(currTask)
                currTask.addCircleCoords(app.width*.25 - 65, app.height*.10 + 100 + (40*len(app.tasks)))
                currTask.addDeleteCoords(app.width*.25 - 100, app.height*.10 + 100 + (40*len(app.tasks)))
                currTask.addEditCoords(app.width*.25 - 130, app.height*.10 + 100 + (40*len(app.tasks)))
                resetPopup(app)
            
            elif app.editMode:
                app.currentTaskBeingEdited.taskName = app.currentTask
                print(f'{app.currentTask}')
                app.currentTaskBeingEdited.taskHours = int(app.currentHour)
                app.currentTaskBeingEdited.taskMinutes = int(app.currentMinute)
                resetPopup(app)
                app.onAddTaskPopup = False
        
        if inExitButton(app, mouseX, mouseY):
            resetPopup(app)
            app.onAddTaskPopup = False
            
    
    if inAddButton(app, mouseX, mouseY):
        app.addButtonColor = None
        # response = app.getTextInput('Enter a task:')
        # time = app.getTextInput('Time (in minutes) needed to complete task (must be in a number!):')
        app.onAddTaskPopup = True
        
        
        # if response != '' and time != '0' and isNum(time):
        #     currTask = Task(response, int(time))
        #     app.tasks.append(currTask)
        #     currTask.addCircleCoords(app.width*.25 - 65, app.height*.10 + 80 + (40*len(app.tasks)))

    if inEditButton(app, mouseX, mouseY):
        app.editMode = not app.editMode
        
        if app.editMode:
            app.editMessage = 'Done!'
        else:
            app.editMessage = 'Edit Mode'
        
    
    if inHomeOnTasks(app, mouseX, mouseY): 
        app.homeButtonColor = None
        setActiveScreen('landing')
        
    if inTimerOnTasks(app, mouseX, mouseY):
        app.timerOnTasksFill = None
        setActiveScreen('timerPage')
        
    if inPlannerOnTasks(app, mouseX, mouseY):
        app.timerButtonColor = None
        nextDrawnY = 135
        setActiveScreen('planner')
    
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
        
def deleteTask(app, i):
    app.tasks.pop(i)

def moveOtherTasks(app, i):
    for task in app.tasks[i:]:
        print(task)
        task.circleCoords = (task.circleCoords[0], task.circleCoords[1]-40)
        task.deleteCoords = (task.deleteCoords[0], task.deleteCoords[1]-40)
            
def taskPage_onMouseMove(app, mouseX, mouseY):
    if not app.onAddTaskPopup:
        if inHomeOnTasks(app, mouseX, mouseY):
            app.homeOnTasksFill = 'gray'
        else:
            app.homeOnTasksFill = None
        
        if inAddButton(app, mouseX, mouseY):
            app.addButtonColor = 'gray'
        else:
            app.addButtonColor = None
            
        if inTimerOnTasks(app, mouseX, mouseY):
            app.timerOnTasksFill = 'gray'
        else:
            app.timerOnTasksFill = None
            
        if inPlannerOnTasks(app, mouseX, mouseY):
            app.plannerOnTasksFill = 'gray'
        else:
            app.plannerOnTasksFill = None
            
        if inEditButton(app, mouseX, mouseY):
            app.editButtonFill = 'gray'
        else:
            app.editButtonFill = None
            

            
def taskPage_onKeyPress(app, key):
    if app.inTaskBox:
        if key == 'space':
            app.currentTask += ' '
        if key == 'backspace' and app.currentTask != '':
            app.currentTask = app.currentTask[:-1]
        elif len(key) == 1:
            app.currentTask += key
        
        print(app.currentTask)
            
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
    drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 40)
    drawRect(app.width/2, app.height/2, app.width/2.5, app.height/2.5, align = 'center', fill = 'white', border = 'black')
    boxLeft = app.width/2 - (app.width/2.5/2)
    boxTop = app.height/2 - (app.height/2.5/2)
    boxWidth = app.width/2.5
    boxHeight = app.height/2.5
    
    ## CITATION
    ## ICON BELOW FOUND FROM https://icons8.com/icon/ZV8D2YZ6852I/x 
    drawImage('exit.png', boxLeft + boxWidth - 45, boxTop + 15, width = 35, height = 35)
    
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

def inHomeOnTasks(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.3 < mouseY < app.height*.3 + 50

def inPlannerOnTasks(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.4 < mouseY < app.height*.4 + 50

def inTimerOnTasks(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.5 < mouseY < app.height*.5 + 50

def inSaveButton(app, mouseX, mouseY):
    return 940 < mouseX < 1040 and 590 < mouseY < 620

def inEditButton(app, mouseX, mouseY):
    return app.width*.25 + 270 - 50 < mouseX < app.width*.25 + 370 - 50 and app.height*.10 + 6 - 15 < mouseY < app.height*.10 + 6 + 15


def inExitButton(app, mouseX, mouseY):
    boxLeft = app.width/2 - (app.width/2.5/2)
    boxTop = app.height/2 - (app.height/2.5/2)
    boxWidth = app.width/2.5
    boxHeight = app.height/2.5
    return boxLeft + boxWidth - 45 < mouseX < boxLeft + boxWidth - 45 + 35 and boxTop + 15 < mouseY < boxTop + 15 + 35

def isNum(time):
    for chr in time:
        if not chr.isdigit():
            return False
    return True

def resetPopup(app):
    app.currentTask = ''
    app.currentHour = ''
    app.currentMinute = ''
    
    app.taskBoxFill = None
    app.hourBoxFill = None
    app.minuteBoxFill = None

def distance(x0, y0, x1, y1):
    a = (x1-x0) ** 2
    b = (y1- y0) ** 2
    return (a+b) ** 0.5

# def setUpTasks(app):
#     for i in range(len(app.tasks)):
#         currTaskBox = app.tasks[i]
        
#         currTaskBox.initalizeBox((app.width/2) - (app.width/3) + 15, nextDrawnY)
#         currTaskBox.page = app.taskCurrPage
#         nextDrawnY += currTaskBox.height
        
#         if nextDrawnY >= app.taskViewTop + app.taskViewHeight:
#             app.taskTotalPages += 1
#             currTaskBox.page = app.taskTotalPages
#             nextDrawnY = 135
#             currTaskBox.initalizeBox((app.width/2) - (app.width/3) + 15, nextDrawnY)

def drawHomeButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.homeOnTasksFill, border = 'black', opacity = 50)
    drawLabel(f'Home', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)
  
def drawTimerButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.timerOnTasksFill, border = 'black', opacity = 50)
    drawLabel(f'Timer', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)

def drawPlannerButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.plannerOnTasksFill, border = 'black', opacity = 50)
    drawLabel(f'Planner', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)
    
def drawEditModeButtons(app):
    for i in range(len(app.tasks)):
        currTask = app.tasks[i]
        deleteX, deleteY = currTask.deleteCoords
        editX, editY = currTask.editCoords
        ## CITATION - IMAGE FROM https://icons8.com/icon/set/x/sf-regular
        drawImage('deleteIcon.png', deleteX, deleteY, align='center', width = 30, height = 30)
        ## CITATION - IMAGE FROM https://icons8.com/icon/set/edit/sf-regular
        drawImage('editIcon.png', editX, editY, align = 'center', width = 30, height = 30)