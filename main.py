from cmu_graphics import *

## this is the main file of my term project!

def onAppStart(app):
    ####################################
    ## LANDING PAGE VARIABLES
    ####################################
    app.taskButtonColor = None
    
    ####################################
    ## TASK PAGE VARIABLES
    ####################################
    app.tasks = []
    app.circleCoords = []
    
    
########################################
# LANDING PAGE
########################################

def landing_redrawAll(app):
    drawImage('landing.jpg', 0, 0, width = app.width, height = app.height)
    
    drawLabel("OneOneTwoDo", (.67 * app.width), app.height/2 - 100, size = 70, font = 'optima')
    drawLabel("Track Tasks, Plan Your Day, Stay Productive.", (.67 * app.width), app.height/2 - 50, font = 'helvetica')
    
    drawTaskPageButton(app, .67 * app.width, app.height/2 + 50)
    
def landing_onMouseMove(app, mouseX, mouseY):
    if inTaskOnLand(app, mouseX, mouseY):
        app.taskButtonColor = 'lightGrey'
    else:
        app.taskButtonColor = None
    
def landing_onMousePress(app, mouseX, mouseY):
    if inTaskOnLand(app, mouseX, mouseY):
        setActiveScreen('taskPage')

def drawTaskPageButton(app, x, y):
    drawRect(x, y, 200, 50, align = 'center', fill = app.taskButtonColor, border = 'black')
    drawLabel('Tasks', x, y, font = 'arial', size = 25)

def inTaskOnLand(app, mouseX, mouseY):
    return (.67 * app.width) - 100 < mouseX < (.67 * app.width) + 100 and (app.height/2 + 25) < mouseY < (app.height/2 + 75)
    
########################################
# TASK PAGE
########################################

def taskPage_redrawAll(app):
    drawLabel('Task List', app.width * .25, app.height * .10, size = 50, font = 'optima')
    
    drawRect(app.width * .25, (app.height*.10) + 50, 100, 30, align = 'center', fill = None, border = 'black')
    drawLabel('Add Task', app.width * .25, (app.height*.10) + 50, size = 15)
    
    for i in range(len(app.tasks)):
        drawCircle(app.width*.25 - 65, app.height*.10 + 100 + (40*i), 10, fill = None, border = 'black')
        drawLabel(app.tasks[i], app.width*.25 - 50, app.height*.10 + 100 + (40*i), align = 'left', size = 15)

def taskPage_onMousePress(app, mouseX, mouseY):
    if inAddButton(app, mouseX, mouseY):
        response = app.getTextInput('Enter a task')
        app.tasks.append(response)
        app.circleCoords.append((app.width*.25 - 65, ))
        
def inAddButton(app, mouseX, mouseY):
    return app.width*.25 - 50 < mouseX < app.width*.25 + 50 and app.height*.10 - 35 < mouseY < app.height*.10 + 65
        
    


def main():
    runAppWithScreens(initialScreen = "taskPage")
    

main()

    
    