from cmu_graphics import *

## this is the main file of my term project!

def onAppStart(app):
    ####################################
    ## LANDING PAGE VARIABLES
    ####################################
    app.taskButtonColor = None
########################################
# LANDING PAGE
########################################

def landing_redrawAll(app):
    drawImage('landing.jpg', 0, 0, width = app.width, height = app.height)
    
    drawLabel("OneOneTwoDo", (.67 * app.width), app.height/2 - 100, size = 70, font = 'optima')
    drawLabel("Track Tasks, Plan Your Day, Stay Productive.", (.67 * app.width), app.height/2 - 50, font = 'helvetica')
    
    drawTaskPageButton(app, .67 * app.width, app.height/2 + 50)
    
def landing_onMouseMove(app, mouseX, mouseY):
    if  (.67 * app.width) - 100 < mouseX < (.67 * app.width) + 100 and (app.height/2 + 25) < mouseY < (app.height/2 + 75):
        app.taskButtonColor = 'lightGrey'
    else:
        app.taskButtonColor = None
    
def landing_onMousePress(app, mouseX, mouseY):
    pass

def drawTaskPageButton(app, x, y):
    drawRect(x, y, 200, 50, align = 'center', fill = app.taskButtonColor, border = 'black')
    drawLabel('Tasks', x, y, font = 'arial', size = 25)
    
def main():
    runAppWithScreens(initialScreen = "landing")
    

main()

    
    