from cmu_graphics import *

# Constants for the planner
scrollBarX = 380
scrollBarY = 50
scrollBarWidth = 20
scrollBarHeight = 300
thumbHeight = 50
thumbY = scrollBarY

# Planner dimensions
plannerX = 50
plannerY = 50
plannerWidth = 300
plannerHeight = scrollBarHeight

# Time labels
timeLabels = [f"{hour:02d}:00" for hour in range(24)]
labelHeight = 50  # Height of each time block

# Vertical scroll offset
scrollOffset = 0
targetScrollOffset = 0  # Target scroll position for smooth transition

# Function to constrain thumb position
def clamp(value, minValue, maxValue):
    return max(minValue, min(value, maxValue))

def onMouseDrag(app, mouseX, mouseY):
    global thumbY, targetScrollOffset
    # Move the scrollbar thumb and update the target scroll offset
    if scrollBarX <= mouseX <= scrollBarX + scrollBarWidth:
        thumbY = clamp(mouseY - thumbHeight // 2, scrollBarY, scrollBarY + scrollBarHeight - thumbHeight)
        percentScrolled = (thumbY - scrollBarY) / (scrollBarHeight - thumbHeight)
        targetScrollOffset = percentScrolled * (len(timeLabels) * labelHeight - plannerHeight)

def onStep(app):
    global scrollOffset
    # Smoothly transition towards the target scroll offset
    step = 10  # Step size for smooth scrolling
    if abs(targetScrollOffset - scrollOffset) > step:
        if targetScrollOffset > scrollOffset:
            scrollOffset += step
        elif targetScrollOffset < scrollOffset:
            scrollOffset -= step
    else:
        scrollOffset = targetScrollOffset

def redrawAll(app):
    # Draw the static planner frame
    drawRect(plannerX, plannerY, plannerWidth, plannerHeight, fill='white', border='black', borderWidth=2)

    # Draw the visible time blocks
    visibleStartIndex = int(scrollOffset // labelHeight)
    visibleEndIndex = int((scrollOffset + plannerHeight) // labelHeight) + 1

    for i in range(visibleStartIndex, visibleEndIndex):
        if 0 <= i < len(timeLabels):
            y = plannerY + i * labelHeight - scrollOffset
            # Only draw if the block is within the planner's visible area
            if plannerY <= y + labelHeight and y < plannerY + plannerHeight:
                drawRect(plannerX, y, plannerWidth, labelHeight, fill='lightblue', border='black')
                drawLabel(timeLabels[i], plannerX + 10, y + labelHeight // 2, size=15, align='left', fill='black')

    # Draw the scrollbar background
    drawRect(scrollBarX, scrollBarY, scrollBarWidth, scrollBarHeight, fill='lightgrey')
    # Draw the scrollbar thumb
    drawRect(scrollBarX, thumbY, scrollBarWidth, thumbHeight, fill='darkgrey')

# Run the application
runApp()
