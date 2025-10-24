# daily_reminder.py

# Ask user for details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for priority
match priority:
    case "high":
        message = f"Reminder: {task} is a HIGH priority task!"
    case "medium":
        message = f"Reminder: {task} is a MEDIUM priority task."
    case "low":
        message = f"Reminder: {task} is a LOW priority task."
    case _:
        message = f"Reminder: {task} has an UNKNOWN priority level."

# Modify message if time-bound
if time_bound == "yes":
    message += " This task is time-bound — complete it immediately!"
else:
    message += " This task is not time-bound."

# Print final reminder (inline with 'Reminder:' at start)
print(f"{message}")

