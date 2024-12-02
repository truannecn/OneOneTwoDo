from cmu_graphics import *
from taskPage import *
from scheduler import *
from timerPage import *

########################################
# LANDING PAGE
########################################

def landing_redrawAll(app):
    drawImage(app.landingImage, 0, 0, width = app.width, height = app.height)
    
    drawLabel("OneOneTwoDo", (.67 * app.width), app.height/2 - 100, size = 70, font = 'optima')
    drawLabel("Track Tasks  -  Plan Your Day  -  Stay Productive", (.67 * app.width), app.height/2 - 50, font = 'Times New Roman', size = 20)
    
    drawTasksButton(app, 913, app.height/2 + 50, 200, 50)
    drawPlannerButton(app, 913, app.height/2 + 125, 200, 50)
    drawTimerButton(app, 913, app.height/2 + 200, 200, 50)
    
def landing_onMouseMove(app, mouseX, mouseY):
    if inTasksOnLand(app, mouseX, mouseY):
        print('in!')
        app.tasksOnLandingFill = 'gray'
    else:
        app.tasksOnLandingFill = None
        
    if inPlannerOnLand(app, mouseX, mouseY):
        app.plannerOnLandingFill = 'gray'
    else:
         app.plannerOnLandingFill = None
        
    if inTimerOnLand(app, mouseX, mouseY):
        app.timerOnLandingFill = 'gray'
    else:
        app.timerOnLandingFill = None
        
def landing_onMousePress(app, mouseX, mouseY):
    if inTasksOnLand(app, mouseX, mouseY):
        app.tasksOnLandingFill = None
        setActiveScreen('taskPage')
    
    if inPlannerOnLand(app, mouseX, mouseY):
        app.plannerOnLandingFill = None
        setActiveScreen('planner')
    
    if inTimerOnLand(app, mouseX, mouseY):
        app.timerOnLandingFill = None
        setActiveScreen('timerPage')
        
        

def drawTasksButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.tasksOnLandingFill, border = 'black', opacity = 50)
    drawLabel(f'Tasks', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)

def drawPlannerButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.plannerOnLandingFill, border = 'black', opacity = 50)
    drawLabel(f'Planner', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)
  
def drawTimerButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.timerOnLandingFill, border = 'black', opacity = 50)
    drawLabel(f'Timer', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)


def inTasksOnLand(app, mouseX, mouseY):
    return 913 < mouseX < 1113 and app.height/2 + 50 < mouseY < app.height/2 + 100

def inPlannerOnLand(app, mouseX, mouseY):
    return 913 < mouseX < 1113 and app.height/2 + 125 < mouseY < app.height/2 + 175

def inTimerOnLand(app, mouseX, mouseY):
    return 913 < mouseX < 1113 and app.height/2 + 200 < mouseY < app.height/2 + 250