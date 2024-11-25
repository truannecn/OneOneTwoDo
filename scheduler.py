from cmu_graphics import *
from landing import *
from taskPage import *
from scheduler import *

class Task:
    def __init__(self, name, duration, priority=1):
        self.name = name
        self.duration = duration
        self.priority = priority

def timerPage_redrawAll(app):
    drawLabel('Pomodoro Timer', app.width/2, 100, size = 50, font = 'optima')
    
    drawLabel('Instructions', app.width/2, 150, size = 15, font = 'optima')
    drawLabel('Enter what time you would like to start the day', app.width/2, 160, size = 15, font = 'optima')
    drawLabel('Enter what time you would like to end the day', app.width/2, 160, size = 15, font = 'optima')
    
def optimizeSchedule(tasks, start_time, end_time):
    ##TESTER FUNCTION
    def backtrack(index, current_time, selected_tasks, best_schedule):
        # Base case: If we run out of tasks or time
        if current_time > end_time:
            return

        # Update the best schedule if the current one is better
        total_priority = sum(task.priority for task in selected_tasks)
        total_duration = sum(task.duration for task in selected_tasks)

        best_priority = sum(task.priority for task in best_schedule['tasks'])
        if total_priority > best_priority or (
            total_priority == best_priority and total_duration > sum(task.duration for task in best_schedule['tasks'])
        ):
            best_schedule['tasks'] = selected_tasks[:]
            best_schedule['duration'] = total_duration
            best_schedule['priority'] = total_priority

        # Recursive case: Try adding tasks from the remaining list
        for i in range(index, len(tasks)):
            task = tasks[i]
            # Check if the task fits within the remaining time
            if current_time + task.duration <= end_time:
                # Include the task and move forward
                selected_tasks.append(task)
                backtrack(i + 1, current_time + task.duration, selected_tasks, best_schedule)
                selected_tasks.pop()

    # Initialize the best schedule
    best_schedule = {'tasks': [], 'duration': 0, 'priority': 0}

    # Start backtracking from the first task
    backtrack(0, start_time, [], best_schedule)

    return best_schedule['tasks'], best_schedule['duration'], best_schedule['priority']


# Testing The Function
tasks = [
    Task("Task A", 60, 5),
    Task("Task B", 90, 3),
    Task("Task C", 30, 2),
    Task("Task D", 120, 4),
]

start_time = 8 * 60  # Start at 8:00 AM (480 minutes from midnight)
end_time = 17 * 60  # End at 5:00 PM (1020 minutes from midnight)

schedule, total_duration, total_priority = optimizeSchedule(tasks, start_time, end_time)

print("Optimized Schedule:")
for task in schedule:
    print(f"- {task.name} (Duration: {task.duration} minutes, Priority: {task.priority})")
print(f"Total Duration: {total_duration} minutes")
print(f"Total Priority: {total_priority}")