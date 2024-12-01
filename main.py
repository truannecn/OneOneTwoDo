from cmu_graphics import *
from landing import *
from taskPage import *
from scheduler import *
from timerPage import *
from planner import *
from urllib.request import urlopen
from PIL import Image

## this is the main file of my term project!

def loadPilImage(url):
    # Loads a PIL image (not a CMU image!) from a url:
    return Image.open(urlopen(url))

def onAppStart(app):
    ####################################
    ## LANDING PAGE VARIABLES
    ####################################
    app.taskButtonColor = None
    ## CITATION: IMAGE LOADING PIL FROM CMU COURSE PAGE TP RELATED DEMOS -- AUSTIN SCHICK
    # 1. Load a PIL image from a url:
    ## CITATION: IMAGE IS FROM: https://unsplash.com/s/photos/minimalist ##
    url = 'https://images.unsplash.com/photo-1487700160041-babef9c3cb55?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWluaW1hbGlzdHxlbnwwfHwwfHx8MA%3D%3D'
    landingImage = loadPilImage(url)

    # 3. Convert from PIL images to CMU images before drawing:
    app.landingImage = CMUImage(landingImage)
    
    ####################################
    ## TASK PAGE VARIABLES
    ####################################
    app.tasks = []
    app.circleCoords = []
    app.homeButtonColor = None
    app.addButtonColor = None
    app.timerButtonColor = None
    app.onAddTaskPopup = False
    
    app.inTaskBox = False
    app.inHourBox = False
    app.inMinuteBox = False
    
    #in popup
    app.currentTask = ''
    app.currentHour = ''
    app.currentMinute = ''
    app.taskBoxFill = None
    app.hourBoxFill = None
    app.minuteBoxFill = None
    
    ####################################
    ## TIMER PAGE VARIABLES
    ####################################
    app.working = True
    app.timerPaused = True
    app.workTime = 3
    app.breakTime = 300
    app.stepsPerSecond = 1
    
    ####################################
    ## DAILY PLANNER PAGE VARIABLES
    ####################################
    app.taskViewLeft = app.width/2 - app.width/3
    app.taskViewTop = 125
    app.taskViewWidth = app.width/3
    app.taskViewHeight = app.height * .80
    
    app.taskScrollOffset = 0
    app.taskCurrPage = 1
    app.taskTotalPages = 5

def main():
    runAppWithScreens(initialScreen = "taskPage")

main()

    
    