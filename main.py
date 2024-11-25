from cmu_graphics import *
from landing import *
from taskPage import *

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

def main():
    runAppWithScreens(initialScreen = "landing")
    

main()

    
    