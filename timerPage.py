from cmu_graphics import *
from landing import *
from taskPage import *
from scheduler import *
import string


def timerPage_redrawAll(app):
    
    ## outer rectangle
    drawLabel('Pomodoro Timer', app.width/2, 100, size = 50, font = 'optima')
    drawRect(app.width * .25, 250, app.width * .50, 400, fill = None, border = 'black')
    
    ## NAVI BUTTONS
    drawHomeButton(app, app.width * .2 - 100, app.height * .85, 200, 50)
    drawTasksButton(app, app.width * .4 - 100, app.height * .85, 200, 50)
    drawPlannerButton(app, app.width * .6 - 100, app.height * .85, 200, 50)
    drawSchedulerButton(app, app.width * .8 - 100, app.height * .85, 200, 50)
    
    ## SETUP PAGE
    boxLeft = app.width*.25
    boxTop = 250
    boxWidth = app.width * .5
    boxHeight = 400
    
    if app.setUpPage:
        ## instructions
        
        drawLabel('Welcome to the pomodoro timer!', boxLeft + boxWidth/2, boxTop + 20, size = 15, font = 'optima')
        
        drawLabel('To begin, enter the number of minutes you would like to work at a time.', boxLeft + boxWidth/2, boxTop + 50, size = 14, font = 'optima')
        drawLabel('(25 is the most standard if you are not sure where to start!)', boxLeft + boxWidth/2, boxTop + 70, size = 12, font = 'optima')
        
        drawLabel('Next, etner the number of minutes you would like to take breaks for at a time.', boxLeft + boxWidth/2, boxTop + 100, size = 14, font = 'optima')
        drawLabel('(5 is the most standard for breaks!)', boxLeft + boxWidth/2, boxTop + 120, size = 12, font = 'optima')
        
        drawLabel('Finally, etner the total number of hours you plan to work for!', boxLeft + boxWidth/2, boxTop + 150, size = 14, font = 'optima')
        
        
        drawLabel('Work time:', boxLeft + (boxWidth*0.20), boxTop + 200, size = 20, font = 'optima')
        drawLabel('(in minutes)', boxLeft + (boxWidth*0.20), boxTop + 220, size = 15, font = 'optima')
        drawRect(boxLeft + (boxWidth*0.20), boxTop + 255, 60, 35, align = 'center', fill = app.workBoxFill, border = 'black')
        if not app.inWorkBox and app.currWorkTime == '':
            drawLabel('Click:', boxLeft + (boxWidth*0.20), boxTop + 255, fill = 'gray')
        elif app.inWorkBox or app.currWorkTime != '':
            drawLabel(app.currWorkTime, boxLeft + (boxWidth*0.20), boxTop + 255, fill = 'black')
        
        drawLabel('Break time:', boxLeft + (boxWidth*0.50), boxTop + 200, size = 20, font = 'optima')
        drawLabel('(in minutes)', boxLeft + (boxWidth*0.5), boxTop + 220, size = 15, font = 'optima')
        drawRect(boxLeft + (boxWidth*0.5), boxTop + 255, 60, 35, align = 'center', fill = app.breakBoxFill, border = 'black')
        if not app.inBreakBox and app.currBreakTime == '':
            drawLabel('Click:', boxLeft + (boxWidth*0.5), boxTop + 255, fill = 'gray')
        elif app.inBreakBox or app.currBreakTime != '':
            drawLabel(app.currBreakTime, boxLeft + (boxWidth*0.5), boxTop + 255, fill = 'black')

        drawLabel('Total work time:', boxLeft + (boxWidth*0.80), boxTop + 200, size = 20, font = 'optima')
        drawLabel('(in hours)', boxLeft + (boxWidth*0.8), boxTop + 220, size = 15, font = 'optima')
        drawRect(boxLeft + (boxWidth*0.8), boxTop + 255, 60, 35, align = 'center', fill = app.totalBoxFill, border = 'black')
        if not app.inTotalBox and app.currTotalTime == '':
            drawLabel('Click:', boxLeft + (boxWidth*0.8), boxTop + 255, fill = 'gray')
        elif app.inTotalBox or app.currTotalTime != '':
            drawLabel(app.currTotalTime, boxLeft + (boxWidth*0.8), boxTop + 255, fill = 'black')


        ### CHECK IF ALL FIELDS FILLED
        if allFieldsFilled(app) and app.setUpPage:
            drawRect(boxLeft + boxWidth*.5 - 100, boxTop + 325, 200, 50, fill = None, border = 'black')
            drawLabel('Start working!', boxLeft + boxWidth*.5, boxTop + 350, size = 20, fill = 'black', font = 'optima')
        
        return
        
    if app.working == True:
        timerStatus = 'Time to Work!'
    else:
        timerStatus = "Take a Break!"
        
    drawLabel(timerStatus, app.width/2, 270, size = 30, font = 'optima')
    
    if app.working and not app.setUpPage:
        if app.currWorkTimeDisplayed//60 < 10:
            minutesDisplayed = '0' + str(app.currWorkTimeDisplayed//60)
        else:
            minutesDisplayed = str(app.currWorkTimeDisplayed//60)
        
        if app.currWorkTimeDisplayed % 60 < 10:
            secondsDisplayed = '0' + str(app.currWorkTimeDisplayed % 60)
        else:
            secondsDisplayed = str(app.currWorkTimeDisplayed % 60)
        
        # if app.currWorkTimeDisplayed == 0:
        #     app.working = False
        
        drawLabel(f'{minutesDisplayed}:{secondsDisplayed}', app.width/2, 380, size = 70, font = 'optima')
            
        if app.timerPaused:
            buttonMessage = 'Start Timer'
        else:
            buttonMessage = 'Pause Timer'
            
        drawRect(app.width/2 - 100, 450, 200, 50, fill = None, border = 'black')
        drawLabel(buttonMessage, app.width/2, 475, size = 25, font = 'optima')
    
    if not app.working and not app.setUpPage:
        if app.currBreakTimeDisplayed//60 < 10:
            minutesDisplayed = '0' + str(app.currBreakTimeDisplayed//60)
        else:
            minutesDisplayed = str(app.currBreakTimeDisplayed//60)
        
        if app.currBreakTimeDisplayed % 60 < 10:
            secondsDisplayed = '0' + str(app.currBreakTimeDisplayed % 60)
        else:
            secondsDisplayed = str(app.currBreakTimeDisplayed % 60)
            

        drawLabel(f'{minutesDisplayed}:{secondsDisplayed}', app.width/2, 380, size = 70, font = 'optima')
            
        if app.timerPaused:
            buttonMessage = 'Start Timer'
        else:
            buttonMessage = 'Pause Timer'
            
        drawRect(app.width/2 - 100, 450, 200, 50, fill = None, border = 'black')
        drawLabel(buttonMessage, app.width/2, 475, size = 25, font = 'optima')
    
def timerPage_onMousePress(app, mouseX, mouseY):
    if inStartButton(app, mouseX, mouseY):
        app.workTime = int(app.currWorkTime) 
        app.currWorkTimeDisplayed = app.workTime
        app.breakTime = int(app.currBreakTime) 
        app.currBreakTimeDisplayed = app.breakTime
        app.setUpPage = False
        app.working = True
        app.timerPaused = True
    
    if inTimeControlButton(app, mouseX, mouseY):
        app.timerPaused = not app.timerPaused
    
    if inWorkBox(app, mouseX, mouseY):
        app.workBoxFill = 'lightGray'
        app.breakBoxFill = None
        app.totalBoxFill = None
        app.inWorkBox = True
        app.inBreakBox = False
        app.inTotalBox = False
        
    elif inBreakBox(app, mouseX, mouseY):
        app.breakBoxFill = 'lightGray'
        app.totalBoxFill = None
        app.workBoxFill = None
        app.inBreakBox = True
        app.inWorkBox = False
        app.inTotalBox = False
        
    elif inTotalBox(app, mouseX, mouseY):
        app.taskBoxFill = None
        app.breakBoxFill = None
        app.totalBoxFill = 'lightGray'
        app.inTotalBox = True
        app.inBreakBox = False
        app.inWorkBox = False
    else:
        app.inTotalBox = False
        app.inBreakBox = False
        app.inWorkBox = False
        app.workBoxFill = None
        app.breakBoxFill = None
        app.totalBoxFill = None
        
        ## NAVI BAR EVENTS
        
    if inHome(app, mouseX, mouseY):
        app.homeOnTimerFill = None
        setActiveScreen('landing')
    
    if inTasks(app, mouseX, mouseY):
        app.tasksOnTimerFill = None
        setActiveScreen('taskPage')
    
    if inPlanner(app, mouseX, mouseY):
        app.plannerOnTimerFill = None
        setActiveScreen('planner')

def timerPage_onKeyPress(app, key):
    if app.inWorkBox:
        if key == 'backspace' and app.currWorkTime != '':
            app.currWorkTime = app.currWorkTime[:-1]
        if key in string.digits:
            if app.currWorkTime == '':
                app.currWorkTime += key
            else:
                if int(app.currWorkTime + key) < 60:
                    app.currWorkTime += key
            
    if app.inBreakBox:
        if key == 'backspace' and app.currBreakTime != '':
            app.currBreakTime = app.currBreakTime[:-1]
        if key in string.digits:
            if app.currBreakTime == '':
                app.currBreakTime += key
            else:
                if int(app.currBreakTime + key) < 60:
                    app.currBreakTime += key
    
    if app.inTotalBox:
        if key == 'backspace' and app.currTotalTime != '':
            app.currTotalTime = app.currTotalTime[:-1]
        if key in string.digits:
            if app.currTotalTime == '':
                app.currTotalTime += key
            else:
                if int(app.currTotalTime + key) < 24:
                    app.currTotalTime += key
            print(app.currTotalTime)


def timerPage_onMouseMove(app, mouseX, mouseY):
    if inHome(app, mouseX, mouseY):
        app.homeOnTimerFill = 'gray'
    else:
        app.homeOnTimerFill = None
        
    if inTasks(app, mouseX, mouseY):
        app.tasksOnTimerFill = 'gray'
    else:
        app.tasksOnTimerFill = None
        
    if inPlanner(app, mouseX, mouseY):
        app.plannerOnTimerFill = 'gray'
    else:
        app.plannerOnTimerFill = None
    
    if inScheduler(app, mouseX, mouseY):
        app.schedulerOnTimerFill = 'gray'
    else:
        app.schedulerOnTimerFill = None
        


def inTimeControlButton(app, mouseX, mouseY):
    return app.width/2 - 100 < mouseX < app.width/2 + 100 and 450 < mouseY < 500

def inWorkBox(app, mouseX, mouseY):
    boxLeft = app.width*.25
    boxTop = 250
    boxWidth = app.width * .5
    boxHeight = 400
    return boxLeft + (boxWidth*0.20) - 30 < mouseX < boxLeft + (boxWidth*0.20) + 30 and boxTop + 255 - 17.5 < mouseY < boxTop + 255 + 17.5

def inBreakBox(app, mouseX, mouseY):
    boxLeft = app.width*.25
    boxTop = 250
    boxWidth = app.width * .5
    boxHeight = 400
    return boxLeft + (boxWidth*0.50) - 30 < mouseX < boxLeft + (boxWidth*0.50) + 30 and boxTop + 255 - 17.5 < mouseY < boxTop + 255 + 17.5

def inTotalBox(app, mouseX, mouseY):
    boxLeft = app.width*.25
    boxTop = 250
    boxWidth = app.width * .5
    boxHeight = 400
    return boxLeft + (boxWidth*0.8) - 30 < mouseX < boxLeft + (boxWidth*0.8) + 30 and boxTop + 255 - 17.5 < mouseY < boxTop + 255 + 17.5

def inStartButton(app, mouseX, mouseY):
    boxLeft = app.width*.25
    boxTop = 250
    boxWidth = app.width * .5
    boxHeight = 400
    return boxLeft + boxWidth*.5 - 100 < mouseX < boxLeft + boxWidth*.5 + 100 and boxTop + 325 < mouseY < boxTop + 375

def timerPage_onStep(app):
    app.stepsPerSecond = 1
    if not app.setUpPage:
        if app.working:
            if not app.timerPaused and app.currWorkTimeDisplayed > 0:
                app.currWorkTimeDisplayed -= 1
            if app.currWorkTimeDisplayed == 0:
                app.working = False
                app.timerPaused = True
                app.currBreakTimeDisplayed = app.breakTime
        
        else:
            if not app.timerPaused and app.currBreakTimeDisplayed > 0:
                app.currBreakTimeDisplayed -= 1
            if app.currBreakTimeDisplayed == 0:
                app.working = True
                app.timerPaused = True
                app.currWorkTimeDisplayed = app.workTime


def allFieldsFilled(app):
    return app.currWorkTime != '' and app.currBreakTime != '' and app.currTotalTime != ''

def drawHomeButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.homeOnTimerFill, border = 'black')
    drawLabel(f'Home', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)
  
def drawTasksButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.tasksOnTimerFill, border = 'black')
    drawLabel(f'Tasks', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)

def drawPlannerButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.plannerOnTimerFill, border = 'black')
    drawLabel(f'Planner', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)
    
def drawSchedulerButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.schedulerOnTimerFill, border = 'black')
    drawLabel(f'Scheduler', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)
    
def inHome(app, mouseX, mouseY):
    return app.width * .2 - 100 < mouseX < app.width * .2 - 100 + 200 and app.height * .85 < mouseY < app.height * .85 + 50

def inTasks(app, mouseX, mouseY):
    return app.width * .4 - 100 < mouseX < app.width * .4 - 100 + 200 and app.height * .85 < mouseY < app.height * .85 + 50

def inPlanner(app, mouseX, mouseY):
    return app.width * .6 - 100 < mouseX < app.width * .6 - 100 + 200 and app.height * .85 < mouseY < app.height * .85 + 50

def inScheduler(app, mouseX, mouseY):
    return app.width * .8 - 100 < mouseX < app.width * .8 - 100 + 200 and app.height * .85 < mouseY < app.height * .85 + 50
