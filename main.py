from cmu_graphics import *
from landing import *
from taskPage import *
from scheduler import *
from timerPage import *

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
    app.homeButtonColor = None
    app.addButtonColor = None
    app.timerButtonColor = None
    
    ####################################
    ## TIMER PAGE VARIABLES
    ####################################
    app.working = True
    app.timerPaused = True
    app.workTime = 3
    app.breakTime = 300
    app.stepsPerSecond = 1

def main():
    runAppWithScreens(initialScreen = "timerPage")

main()

    
    