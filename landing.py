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
    
    drawTaskPageButton(app, .67 * app.width, app.height/2 + 50)
    
def landing_onMouseMove(app, mouseX, mouseY):
    if inTaskOnLand(app, mouseX, mouseY):
        app.taskButtonColor = 'gray'
    else:
        app.taskButtonColor = None
    
def landing_onMousePress(app, mouseX, mouseY):
    if inTaskOnLand(app, mouseX, mouseY):
        app.taskButtonColor = None
        setActiveScreen('taskPage')

def drawTaskPageButton(app, x, y):
    drawRect(x, y, 200, 50, align = 'center', fill = app.taskButtonColor, border = 'black')
    drawLabel('Tasks', x, y, font = 'times new roman', size = 25)

def drawDailyPageButton(app, x, y):
    drawRect(x, y, 200, 50, align = 'center', fill = app.taskButtonColor, border = 'black')
    drawLabel('Daily', x, y, font = 'times new roman', size = 25)

def drawDailyPageButton(app, x, y):
    drawRect(x, y, 200, 50, align = 'center', fill = app.taskButtonColor, border = 'black')
    drawLabel('Daily', x, y, font = 'times new roman', size = 25)

def inTaskOnLand(app, mouseX, mouseY):
    return (.67 * app.width) - 100 < mouseX < (.67 * app.width) + 100 and (app.height/2 + 25) < mouseY < (app.height/2 + 75)