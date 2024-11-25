from cmu_graphics import *
from landing import *
from taskPage import *
from scheduler import *


def timerPage_redrawAll(app):
    drawLabel('Pomodoro Timer', app.width/2, 100, size = 50, font = 'optima')
    
    drawRect(app.width * .25, 250, app.width * .50, 400, fill = None, border = 'black')
    if app.working == True:
        timerStatus = 'Time to Work!'
    else:
        timerStatus = "Take a Break!"
        
    drawLabel(timerStatus, app.width/2, 270, size = 30, font = 'optima')
    
    if app.workTime//60 < 10:
        minutesDisplayed = '0' + str(app.workTime//60)
    else:
        minutesDisplayed = str(app.workTime//60)
    
    if app.workTime % 60 < 10:
        secondsDisplayed = '0' + str(app.workTime % 60)
    else:
        secondsDisplayed = str(app.workTime % 60)
        
    if app.working:
        drawLabel(f'{minutesDisplayed}:{secondsDisplayed}', app.width/2, 380, size = 70, font = 'optima')
        
    if app.timerPaused:
        buttonMessage = 'Start Timer'
    else:
        buttonMessage = 'Pause Timer' 
        
    drawRect(app.width/2 - 100, 450, 200, 50, fill = None, border = 'black')
    drawLabel(buttonMessage, app.width/2, 475, size = 25, font = 'optima')
    
def timerPage_onMousePress(app, mouseX, mouseY):
    if inTimeControlButton(app, mouseX, mouseY):
        app.timerPaused = not app.timerPaused
 
def inTimeControlButton(app, mouseX, mouseY):
    return app.width/2 - 100 < mouseX < app.width/2 + 100 and 450 < mouseY < 500

def timerPage_onStep(app):
    app.stepsPerSecond = 1
    if not app.timerPaused and app.workTime > 0:
        app.workTime -= 1



    
    
    

