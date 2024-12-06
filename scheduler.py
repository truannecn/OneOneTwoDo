from cmu_graphics import *
from landing import *
import taskPage
from scheduler import *
import copy
from datetime import date

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
            self.endHour = int(temp[:colonIndex])
        elif not self.isAM and int(temp[:colonIndex]) != 12:
            self.endHour = int(temp[:colonIndex])
            self.endHour += 12
        
        self.endMinute = int(temp[colonIndex+1:])
        
        self.endTimeFloat = self.endHour + (self.endMinute/60)
        
    def __eq__(self, other):
        if isinstance(other, taskPage.Task):
            return (self.eventName == other.eventName and
                    self.startTimeFloat == other.startTimeFloat and
                    self.endTimeFloat == other.endTimeFloat)
            
    def __lt__(self, other):
        if isinstance(other, Event):
            return ((self.startTimeFloat < other.startTimeFloat) or
                    (self.startTimeFloat == other.startTimeFloat and self.endTimeFloat < other.endTimeFloat))
        
    
    
        
      
        
        
def scheduler_redrawAll(app):
    ## Title Top
    if app.section == 'intro1' or app.section == 'intro2':
        drawLabel('Welcome to the Scheduler!', app.width/2, 60, font = 'optima', size = 30)
        drawLabel('We make planning out your day all the more simpler. :)', app.width/2, 100, font = 'optima', size = 22)
        
    if app.section == 'intro1':
        displayIntroSection1()    
    if app.section == 'intro2':
        displayIntroSection2() 
    if app.section == 'schedule':
        displaySchedule(app)

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
        for i in range(len(app.schedule)):
            currItem = app.schedule[i]
            if isinstance(currItem, taskPage.Task):
                currItem.assignStartDisplay()
                currItem.assignEndDisplay()
                
        app.section = 'schedule'
        
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
    schedule = copy.copy(app.events)
    tasks = copy.copy(app.tasks)
    app.schedule = []
    result = generate(schedule, tasks, app.leftOverTasks)
    app.schedule = result
    
    
def generate(schedule, tasks, leftOverTasks):
    if tasks == []:
        app.leftOverTasks = leftOverTasks
        return schedule
    else:
        for i in range(len(schedule) + 1):
            currentTask = tasks[0]
            
            if isLegal(schedule, currentTask, i):
                schedule.insert(i, currentTask)
                solution = generate(schedule, tasks[1:], leftOverTasks)
                if solution != None:
                    return solution

                schedule.pop(i)
        
        leftOverTasks.append(tasks[0])
        return generate(schedule, tasks[1:], leftOverTasks)

def isLegal(schedule, currentTask, insertIndex):
    ## Checks when you are inserting something at the very beginning of the schedule
    if insertIndex == 0:
        if schedule != []:
            currEvent = schedule[0]
            gap = currEvent.startTimeFloat - app.startTimeSchedule
            if gap >= currentTask.taskFloat:
                currentTask.startTimeFloat = app.startTimeSchedule
                currentTask.assignEndTime()
                return True
        else: ## Chatgpt suggested I implement a check for if the schedule list is empty
            if app.endTimeSchedule - app.startTimeSchedule >= currentTask.taskTime:
                currentTask.startTimeFloat = app.startTimeSchedule
                currentTask.assignEndTime()
                return True
    ## checks when the task is at the very end of the schedule list
    elif insertIndex == len(schedule):
        currItem = schedule[-1]
        gap = app.endTimeSchedule - currItem.endTimeFloat
        if currentTask.taskFloat <= gap:
            currentTask.startTimeFloat = currItem.endTimeFloat
            currentTask.assignEndTime()
            return True
    
    ## checks when the tasks are just in the middle of the list
    else:
        prevItem = schedule[insertIndex-1]
        nextItem = schedule[insertIndex]
        gap = nextItem.startTimeFloat - prevItem.endTimeFloat
        if currentTask.taskFloat <= gap:
            currentTask.startTimeFloat = prevItem.endTimeFloat
            currentTask.assignEndTime()
            return True
    
    return False


############################
## DISPLAY FINAL SCHEDULE ##
############################

def displaySchedule(app):
    
    ## TITLE ##
    today = date.today()
    
    drawLabel(f'Recommended Schedule for {today.month}/{today.day}/{today.year}', app.width/2, 150, font = 'optima', size = 35, bold = True)    
    drawLine(app.width/2-50, 200, app.width/2+50, 200, lineWidth=2)
    for i in range(len(app.schedule)):
        currItem = app.schedule[i]
        if isinstance(currItem, taskPage.Task):
            drawLabel(f'{currItem.taskName}: {currItem.startTimeDisplay} - {currItem.endTimeDisplay}', app.width/2, 230 + 35*i, font = 'optima', size = 22)
        elif isinstance(currItem, Event):
            drawLabel(f'{currItem.eventName}: {currItem.startTime} - {currItem.endTime}', app.width/2, 230 + 35*i, font = 'optima', size = 22)

    if app.leftOverTasks != []:
        drawLabel('Leftover Tasks', app.width/2, 300 + (len(app.schedule) * 35), font = 'optima', size = 35, bold = True)    
        drawLine(app.width/2-50, 370, app.width/2+50, 370, lineWidth=2)
        for i in range(len(app.leftOverTasks)):
            currItem = app.leftOverTasks[i]
            if isinstance(currItem, taskPage.Task):
                drawLabel(f'{currItem.taskName}: {currItem.taskHours} hours and {currItem.taskMinutes} minutes', app.width/2, (360 + (len(app.schedule) * 35) + (30*i)), font = 'optima', size = 20)
                
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
    