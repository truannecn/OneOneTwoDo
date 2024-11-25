from cmu_graphics import *
from datetime import date
from landing import *
from taskPage import *

import datetime

now = datetime.datetime.now()

day = now.day
month = now.month
year = now.year

print("Day:", day)
print("Month:", month)
print("Year:", year)

today = date.today()
print(today)

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

    
    