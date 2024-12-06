from cmu_graphics import *
from landing import *
from taskPage import *
from scheduler import *

class Event():
    def __init__(self, eventName, startTime, endTime):
        self.eventName = eventName
        self.startTime = startTime
        self.endTime = endTime
        self.eventDuration = 0
        
        self.isAM = None
    
    def __repr__(self):
        return f'{self.eventName}'
    
    def convertStartTime(self):
        if self.startTime[len(self.startTime)-2:] == 'am':
            self.isAM = True
        else:
            self.isAM = False
        
        temp = self.startTime[:-2]
        temp = temp.strip()
        colonIndex = temp.index(':')
        
        if self.isAM == True or (self.isAM == False and int(temp[:colonIndex]) == 12):
            self.startHour = int(temp[:colonIndex])
        elif not self.isAM and int(temp[:colonIndex]) != 12:
            self.startHour = int(temp[:colonIndex])
            self.startHour += 12
        
        self.startMinute = int(temp[colonIndex+1:])
        
        self.startTimeFloat = self.startHour + (self.startMinute/60)
    
    def convertEndTime(self):
        if self.endTime[len(self.endTime)-2:] == 'am':
            self.isAM = True
        else:
            self.isAM = False
        
        temp = self.endTime[:-2]
        temp = temp.strip()
        colonIndex = temp.index(':')
        
        if self.isAM == True or (self.isAM == False and int(temp[:colonIndex]) == 12):
            self.startHour = int(temp[:colonIndex])
        elif not self.isAM and int(temp[:colonIndex]) != 12:
            self.startHour = int(temp[:colonIndex])
            self.startHour += 12
        
        self.startMinute = int(temp[colonIndex+1:])
        
        self.endTimeFloat = self.startHour + (self.startMinute/60)
        
    def __eq__(self, other):
        if isinstance(other, Event):
            return (self.eventName == other.eventName and
                    self.startTimeFloat == other.startTimeFloat and
                    self.endTimeFloat == other.endTimeFloat)
            
    def __lt__(self, other):
        if isinstance(other, Event):
            return ((self.startTimeFloat < other.startTimeFloat) or
                    (self.startTimeFloat == other.startTimeFloat and self.endTimeFloat < other.endTimeFloat))
        
    
    
        
      
        
        
def scheduler_redrawAll(app):
    ## Title Top
    drawLabel('Welcome to the Scheduler!', app.width/2, 60, font = 'optima', size = 30)
    drawLabel('We make planning out your day all the more simpler. :)', app.width/2, 100, font = 'optima', size = 22)
    
    if app.section == 'intro1':
        displayIntroSection1()    
    if app.section == 'intro2':
        displayIntroSection2() 

def scheduler_onMousePress(app, mouseX, mouseY):
    if inStartTime(mouseX, mouseY):
        response = app.getTextInput('When would you like to start your day?')
        app.startTimeDisplay = response
        app.startTimeSchedule = convertTime(response)
    if inEndTime(mouseX, mouseY):
        response = app.getTextInput('When would you like to end your day?')
        app.endTimeSchedule = response
        app.endTimeDisplay = response
        app.endTimeSchedule = convertTime(response)
        
        ## Calculate total time
        app.durationOfDay = app.endTimeSchedule - app.startTimeSchedule
        print(f'{app.startTimeSchedule} {app.endTimeSchedule} {app.durationOfDay}')
        
    if inNext1(mouseX, mouseY):
        app.section = 'intro2'
    
    if app.section == 'intro2' and inEvent(mouseX, mouseY):
        response = app.getTextInput('Enter event in [eventName, startTime, endTime] (Meeting, 1:00pm, 2:00pm):')
        if validEventResponse(response):
            ## Get event name
            temp = response
            firstIndex = temp.index(',')
            tempName = response[:firstIndex]
            temp = temp[firstIndex+1:]
            temp = temp.strip()
            
            ## Get event start time
            secondIndex = temp.index(',')
            tempStartTime = temp[:secondIndex]
            temp = temp[secondIndex+1:]
            temp = temp.strip()
            ## Get event end time
            tempEndTime = temp
            
            app.events.append(Event(tempName, tempStartTime, tempEndTime))
            
            ## Convert start and end times to floats and find how long the event will take in float time
            mostRecentEvent = app.events[-1]
            mostRecentEvent.convertStartTime()
            mostRecentEvent.convertEndTime()
            mostRecentEvent.eventDuration = mostRecentEvent 
            print(f'Start time: {mostRecentEvent.startTimeFloat}')
            print(f'End Time: {mostRecentEvent.endTimeFloat}')
            mostRecentEvent.eventDuration = mostRecentEvent.endTimeFloat - mostRecentEvent.startTimeFloat
        else:
            app.showMessage('Oops, please try again! Consider the correct format and having valid end and start times!')
        
        
    if app.section == 'intro2' and inCreate(mouseX, mouseY):
        generateSchedule()
        app.section = 'schedule'
        
        displaySchedule()
        
################################
### Displaying start/end to day
################################

def displayIntroSection1():
    ## Fill out start/end time instructions
    drawLabel('To begin, when would you like to start and end your day?', app.width/2, 200, font = 'optima', size = 25)
    drawLabel('1. Fill out in hh:mm am/pm format! (11:00 am, 1:00 pm)', app.width/2, 230, font = 'times new roman', size = 20)
    drawLabel('2. Please be sure that your end time is after the start time.', app.width/2, 255, font = 'times new roman', size = 20)
    
    ## Start Time Section
    drawLabel('Start Time', app.width * .4, 320, size = 25, font = 'optima')
    if app.startTimeDisplay == None:
        drawRect(app.width*.4 - 50, 350, 100, 40, fill = None, border = 'black')
        drawLabel('Click', app.width*.4, 370, size = 15, fill = 'gray')
    else:
        drawLabel(app.startTimeDisplay, app.width*.4, 370, size = 20, fill = 'black', font = 'optima')
    
    ## End Time Section
    drawLabel('End Time', app.width * .6, 320, size = 25, font = 'optima')
    if app.endTimeDisplay == None:
        drawRect(app.width*.6 - 50, 350, 100, 40, fill = None, border = 'black')
        drawLabel('Click', app.width*.6, 370, size = 15, fill = 'gray')
    else:
        drawLabel(app.endTimeDisplay, app.width*.6, 370, size = 20, font = 'optima', fill = 'black')
        
    ## Draw Next Button
    if app.startTimeDisplay != None and app.endTimeDisplay != None:
        drawRect(app.width*.5 - 50, 420, 100, 40, fill = None, border = 'black')
        drawLabel('Next', app.width*.5, 440, size = 20, fill = 'black', font = 'optima')


###############################
## Displaying Events Section ##
###############################

def displayIntroSection2():
    drawLabel('Next, enter any busy hours.', app.width/2, 180, font = 'optima', size = 25)
    drawLabel('1. Input any events you already have planned for the day (ex: meals, meetings, rehearsals.)', app.width/2, 230, font = 'times new roman', size = 20)
    drawLabel('2. Enter in [event, startTime, endTime] format. (Lunch, 12:00pm, 2:0pmm)', app.width/2, 255, font = 'times new roman', size = 20)
    drawLabel('3. Click "Generate Schedule" when done!', app.width/2, 280, font = 'times new roman', size = 20)
    
    ## Display All Events Inputted By User
    
    drawLabel('Events For Today', app.width/2, 340, font = 'optima', size = 30)
    app.events.sort()
    for i in range(len(app.events)):
        currentEvent = app.events[i]
        drawLabel(f'{currentEvent.eventName}: {currentEvent.startTime} - {currentEvent.endTime}', app.width/2, 400 + (30 * i), font = 'optima', size = 17)
    
    ## Add Events Button
    drawCircle(app.width/2, 400 + (30 * (len(app.events) + 1)), 15, fill = None, border = 'black')
    drawLabel('+', app.width/2, 400 + (30 * (len(app.events) + 1)), font = 'optima', size = 22)
    
    ## Create Schedule Button
    drawRect(app.width/2 - 100, 460 + (30 * (len(app.events) + 1)), 200, 50, fill = None, border = 'black')
    drawLabel("Create Schedule!", app.width/2, 485 + (30 * (len(app.events) + 1)), font = 'optima', size = 20)
    
###################################
## Schedule Generating Algorithm ##
###################################

def generateSchedule():
    
    
    

############################
## Other helper functions ##
############################

def inStartTime(mouseX, mouseY):
    return app.width*.4 - 50 < mouseX < app.width*.4 + 50 and 350 < mouseY < 390

def inEndTime(mouseX, mouseY):
    return app.width*.6 - 50 < mouseX < app.width*.6 + 50 and 350 < mouseY < 390

def inNext1(mouseX, mouseY):
    return app.width*.5 - 50 < mouseX < app.width*.5 + 50 and 420 < mouseY < 460

def inEvent(mouseX, mouseY):
    return distance(mouseX, mouseY, app.width/2, 400 + (30 * (len(app.events) + 1))) < 15

def inCreate(mouseX, mouseY):
    return app.width/2 - 100 < mouseX < app.width/2 + 100 and 460 + (30 * (len(app.events) + 1)) < mouseY < 510 + (30 * (len(app.events) + 1))

def distance(x0, y0, x1, y1):
    a = (x1 - x0) ** 2
    b = (y1 - y0) ** 2
    return (a + b) ** 0.5

def validEventResponse(response):
    return response.count(',') == 2

def convertTime(stringTime):
    if stringTime[len(stringTime)-2:] == 'am':
        isAM = True
    else:
        isAM = False
    
    temp = stringTime[:-2]
    temp = temp.strip()
    colonIndex = temp.index(':')
    
    if isAM == True or (isAM == False and int(temp[:colonIndex]) == 12):
        hour = int(temp[:colonIndex])
    elif not isAM and int(temp[:colonIndex]) != 12:
        hour = int(temp[:colonIndex])
        hour += 12
    
    minute = int(temp[colonIndex+1:])
    
    result = hour + (minute/60)
    return result
    