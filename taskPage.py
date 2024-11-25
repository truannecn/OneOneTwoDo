from cmu_graphics import *

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
    # if inAddButton(app, mouseX, mouseY):
    #     response = app.getTextInput('Enter a task')
    #     app.tasks.append(response)
    #     app.circleCoords.append((app.width*.25 - 65, app.height*.10 + 100 + (40*len(app.circleCoords))))
    
    # for i in range(len(app.circleCoords)):
    #     circleX, circleY = app.circleCoords[i]
    #     if distance(mouseX, mouseY, circleX, circleY) < 10:
    #         app.circleCoords
    pass
            
        
        
def inAddButton(app, mouseX, mouseY):
    return app.width*.25 - 50 < mouseX < app.width*.25 + 50 and app.height*.10 - 35 < mouseY < app.height*.10 + 65  