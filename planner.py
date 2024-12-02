from cmu_graphics import *
from landing import *
from scheduler import *
from timerPage import *
from taskPage import *
import string

def planner_redrawAll(app):
    drawImage(app.plannerImage, 0, 0, width = app.width, height = app.height)
    
    drawLabel('Daily Planner', app.taskViewLeft, app.taskViewTop - 40, align = 'left', font = 'optima', size = 35)
    
    drawHomeButton(app, 20, app.height*.3, 200, 50)
    drawTasksButton(app, 20, app.height*.4, 200, 50)
    drawTimerButton(app, 20, app.height*.5, 200, 50)
    
    drawTaskView(app)
    drawPlannerView(app)
    if len(app.tasks) > 0:
        drawScrollBar(app)
    
    
def drawTaskView(app):
    # outer rectangle
    drawRect(app.width/2 - app.width/3, 125, app.width/3, app.height * .80, fill = 'snow', border = 'black')

    # draw task boxes
    nextDrawnY = 135
    if len(app.tasks) == 0:
        drawLabel('No tasks to display!', app.taskViewLeft + app.taskViewWidth/2, app.taskViewTop + app.taskViewHeight/2, font = 'optima', fill = 'gray', size = 20)
    
    if len(app.tasks) > 0:
        currentTasksCompleted = 0
        for i in range(len(app.tasks)):
            cTask = app.tasks[i]
            if cTask.taskCompleted:
                currentTasksCompleted += 1
        
        if currentTasksCompleted == len(app.tasks):
            drawLabel('Yay! You have completed all tasks.', app.taskViewLeft + app.taskViewWidth/2, app.taskViewTop + app.taskViewHeight/2,font = 'optima', fill = 'gray', size = 20)
            return
            
    
    for i in range(len(app.tasks)):
        #get current task
        currTaskBox = app.tasks[i]
        
        if currTaskBox == app.draggingTask:
            currTaskBox.drawBox()
        else:
            if currTaskBox.taskCompleted:
                continue
            #make the box and initalize its properties
            currTaskBox.initalizeBox((app.width/2) - (app.width/3) + 15, nextDrawnY)
            
            #get the adjusted top
            adjustedTop = currTaskBox.boxTop - app.taskScrollOffset
            
            #if the current task box is within the visible bounds then drawww
            if 135 <= adjustedTop < 125 + (app.height * .80) and 135 <= adjustedTop + currTaskBox.height < 125 + (app.height * .80):
                currTaskBox.boxTop = adjustedTop
                currTaskBox.drawBox()

            nextDrawnY += currTaskBox.height + 10
        
    


def drawScrollBar(app):
    viewHeight = app.taskViewHeight
    totalHeight = len(app.tasks) * (max(task.height for task in app.tasks) + 10)  # Total content height

    if totalHeight <= viewHeight:
        drawRect(app.taskViewLeft + app.taskViewWidth - 16, 128, 13, viewHeight - 5, fill='darkgrey')
        return 
    
    scrollBarHeight = max(20, viewHeight * (viewHeight / totalHeight))  # Proportional height
    scrollBarTop = 128 + (app.taskScrollOffset / totalHeight) * viewHeight  # Proportional Y position

    drawRect(app.taskViewLeft + app.taskViewWidth - 16, scrollBarTop, 13, scrollBarHeight, fill='darkgrey')

def drawBackPageButton(app):
    drawRect(100, 100, 50, 50)

def drawForwardPageButton(app):
    drawRect(100, 300, 50, 50)
    
def drawHomeButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.homeOnPlannerFill, border = 'black', opacity = 50)
    drawLabel(f'Home', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)
  
def drawTimerButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.timerOnPlannerFill, border = 'black', opacity = 50)
    drawLabel(f'Timer', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)

def drawTasksButton(app, buttonLeft, buttonTop, width, height):
    drawRect(buttonLeft, buttonTop, width, height, fill = app.tasksOnPlannerFill, border = 'black', opacity = 50)
    drawLabel(f'Tasks', buttonLeft + width/2, buttonTop + height/2, font = 'optima', size = 20)
  
def inBackPageButton(app, mouseX, mouseY):
    return 100 < mouseX < 150 and 100 < mouseY < 150

def inForwardPageButton(app, mouseX, mouseY):
    return 100 < mouseX < 150 and 300 < mouseY < 350


##################################
# DAILY VIEW
###################################
    
def drawBackupPlannerView(app):
    drawRect(app.width/2, 5, app.width/2.25, app.height -10, fill = 'snow', border = 'black')

    visibleTop = 5
    visibleHeight = app.height -10
    totalHeight = app.dayViewHeight
    startTime = 6
    intervalHeight = 25
    
    for i in range(36):
        currIncrement = i
        top = visibleTop + i * intervalHeight - app.dailyScrollOffset
        if top > visibleTop + visibleHeight: 
            break
        
        drawRect(app.width / 2, top, app.width / 2.25, intervalHeight, fill='white', border='lightgrey')
        if currIncrement % 2 == 0:
            if currIncrement < 11:    
                halfOfDay = 'am'
            else:
                halfOfDay = 'pm'
            
            currTime = startTime + (currIncrement // 2)
            if currTime == 0 or currTime == 12:
                currTime = 12
            else:
                currTime = currTime % 12
            # currTime = startTime + currIncrement // 4
            # if currIncrement // 4 == 12:
            #     currTime = 12
            # else:
            #     currTime = currIncrement // 4 * 12
            drawLabel(f'{currTime}:00 {halfOfDay}', app.width / 2 + 4, top + 10, align='left-top')
    

def drawPlannerView(app):

    visibleTop = 125
    visibleHeight = app.height * 0.80
    totalHeight = app.dayViewHeight
    startTime = 0
    intervalHeight = 32
    
    for i in range(96):
        currIncrement = i
        top = visibleTop + i * intervalHeight - app.dailyScrollOffset
        if top < 125:
            continue
        if top > visibleTop + visibleHeight: 
            break
        
        drawRect(app.width / 2, top, app.width / 2.25, intervalHeight, fill='white', border='lightgrey')
        if currIncrement % 4 == 0:
            if currIncrement < 48:    
                halfOfDay = 'am'
            else:
                halfOfDay = 'pm'
            
            currTime = startTime + (currIncrement // 4)
            if currTime == 0:
                currTime = 12
            else:
                currTime = currTime % 12
            # currTime = startTime + currIncrement // 4
            # if currIncrement // 4 == 12:
            #     currTime = 12
            # else:
            #     currTime = currIncrement // 4 * 12
            drawLabel(f'{currTime}:00 {halfOfDay}', app.width / 2 + 4, top + 10, align='left-top')
    
    drawDailyScrollBar(app)
    
def drawDailyScrollBar(app):
    visibleHeight = app.height * 0.80 
    totalHeight = app.dayViewHeight
    scrollBarHeight = max(20, visibleHeight * (visibleHeight / totalHeight))  # Proportional height
    scrollBarTop = 125 + (app.dailyScrollOffset / totalHeight) * visibleHeight  # Position relative to offset

    # Draw the scroll bar background and handle
    drawRect(app.width/2 + app.dailyViewWidth, 125, 15, visibleHeight, fill='lightgrey')  # Background track
    drawRect(app.width/2 + app.dailyViewWidth, scrollBarTop, 13, scrollBarHeight, fill='darkgrey')  # Scroll bar

def planner_onMouseMove(app, mouseX, mouseY):
    if inHomeOnPlanner(app, mouseX, mouseY):
        app.homeOnPlannerFill = 'gray'
    else:
        app.homeOnPlannerFill = None
        
    if inTasksOnPlanner(app, mouseX, mouseY):
        app.tasksOnPlannerFill = 'gray'
    else:
        app.tasksOnPlannerFill = None
    
    if inTimerOnPlanner(app, mouseX, mouseY):
        app.timerOnPlannerFill = 'gray'
    else:
        app.timerOnPlannerFill = None

def planner_onMousePress(app, mouseX, mouseY):
    if inHomeOnPlanner(app, mouseX, mouseY):
        setActiveScreen('landing')
    if inTasksOnPlanner(app, mouseX, mouseY):
        setActiveScreen('taskPage')
    if inTimerOnPlanner(app, mouseX, mouseY):
        setActiveScreen('timerPage')
    
    if len(app.tasks) > 0:
        viewHeight = app.taskViewHeight
        totalHeight = len(app.tasks) * (max(task.height for task in app.tasks) + 10)  # Total content height
        
        scrollBarLeft = app.taskViewLeft + app.taskViewWidth - 16
        scrollBarWidth = 13
        scrollBarHeight = max(20, viewHeight * (viewHeight / totalHeight))  # Proportional height
        scrollBarTop = 128 + (app.taskScrollOffset / totalHeight) * viewHeight  # Proportional Y position

        # Check if the click is inside the scroll bar
        if scrollBarLeft <= mouseX <= scrollBarLeft + scrollBarWidth:
            if scrollBarTop <= mouseY <= scrollBarTop + scrollBarHeight:
                app.scrollBarDragging = True
    
    ## CHECKING FOR DAILY VIEW SCROLL BAR
    visibleHeight = app.height * 0.80
    totalHeight = app.dayViewHeight
    scrollBarHeight = max(20, visibleHeight * (visibleHeight / totalHeight))
    scrollBarTop = 125 + (app.dailyScrollOffset / totalHeight) * visibleHeight

    if app.width/2 + (app.width/2.25) <= mouseX <= app.width/2 + (app.width/2.25) + 13 and scrollBarTop <= mouseY <= scrollBarTop + scrollBarHeight:
        app.dailyScrollBarDragging = True
        app.lastMouseY = mouseY  
    
    ### Dragging blocks -- sets the block to the one selected
    for task in app.tasks:
        if (task.boxLeft <= mouseX <= task.boxLeft + task.width and
                task.boxTop <= mouseY <= task.boxTop + task.height):
            app.draggingTask = task
            app.dragOffsetX = mouseX - task.boxLeft
            app.dragOffsetY = mouseY - task.boxTop
            break
    
def planner_onMouseDrag(app, mouseX, mouseY):
    if len(app.tasks) > 0: 
    
        if app.scrollBarDragging == True:
            viewHeight = app.taskViewHeight
            totalHeight = len(app.tasks) * (max(task.height for task in app.tasks) + 10)

            if totalHeight <= viewHeight:
                app.taskScrollOffset = 0
                return
            
            scrollBarHeight = max(20, viewHeight * (viewHeight / totalHeight))
            
            scrollBarTop = min(max(0, mouseY - scrollBarHeight / 2), viewHeight - scrollBarHeight)
            app.taskScrollOffset = (scrollBarTop / (viewHeight - scrollBarHeight)) * (totalHeight - viewHeight)

    if app.dailyScrollBarDragging:
        visibleHeight = app.height * 0.80
        totalHeight = app.dayViewHeight
        scrollBarHeight = max(20, visibleHeight * (visibleHeight / totalHeight))

        # Calculate the new scroll position based on mouse movement
        deltaY = mouseY - app.lastMouseY
        maxScrollBarTop = 125 + visibleHeight - scrollBarHeight
        scrollBarTop = min(max(125, 125 + (app.dailyScrollOffset / totalHeight) * visibleHeight + deltaY), maxScrollBarTop)

        # Update dayScrollOffset based on scroll bar position
        app.dailyScrollOffset = (scrollBarTop - 125) / (visibleHeight - scrollBarHeight) * (totalHeight - visibleHeight)
        app.lastMouseY = mouseY  # Update the last mouse position
        
    # dragging block
    if app.draggingTask is not None:
        print(mouseX, mouseY)
        app.draggingTask.boxLeft = mouseX - app.dragOffsetX
        app.draggingTask.boxTop = mouseY - app.dragOffsetY

def planner_onMouseRelease(app, mouseX, mouseY):
    app.scrollBarDragging = False
    app.dailyScrollBarDragging = False
    
    # check for dragging box releases
    if app.draggingTask is not None:
        # Check if dropped in the daily view
        if app.validDropZoneLeft <= mouseX <= app.validDropZoneLeft + app.validDropZoneWidth:
            # Calculate the closest time interval
            intervalHeight = 32  # Height of each time interval
            top = app.draggingTask.boxTop - 125 + app.dailyScrollOffset
            snappedInterval = rounded(top / intervalHeight) * intervalHeight

            # Snap within the daily view bounds
            if 0 <= snappedInterval <= app.dayViewHeight - intervalHeight:
                app.draggingTask.boxLeft = app.width / 2  # Snap to daily view column
                app.draggingTask.boxTop = 125 + snappedInterval - app.dailyScrollOffset
                
                app.draggingTask.assignedTime = snappedInterval // intervalHeight
            else:
                # Snap back to the task view
                app.draggingTask.boxLeft = app.taskViewLeft + 15
                app.draggingTask.boxTop = 135 + len(app.tasks) * (app.draggingTask.height + 10)
        else:
            # Snap back to the task view
            app.draggingTask.boxLeft = app.taskViewLeft + 15
            app.draggingTask.boxTop = 135 + len(app.tasks) * (app.draggingTask.height + 10)
        
        # End dragging
        app.draggingTask = None
    
def inHomeOnPlanner(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.3 < mouseY < app.height*.3 + 50

def inTasksOnPlanner(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.4 < mouseY < app.height*.4 + 50

def inTimerOnPlanner(app, mouseX, mouseY):
    return 20 < mouseX < 220 and app.height*.5 < mouseY < app.height*.5 + 50

# def planner_onKeyPress(app, key):
    
#     totalHeight = len(app.tasks) * (max(task.height for task in app.tasks) + 10)  
#     maxScroll = max(0, totalHeight - app.taskViewHeight - 30)  # Maximum scrolling range
#     if key == 'up':
#         app.taskScrollOffset = max(app.taskScrollOffset - 20, 0)
#     elif key == 'down':
#         app.taskScrollOffset = min(app.taskScrollOffset + 20, maxScroll)
        