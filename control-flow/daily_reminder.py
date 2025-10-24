# daily_reminder.py

# Ask the user for details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case statement for priority
match priority:
    case "high":
        reminder_message = f"Reminder: {task} is a HIGH priority task! Make it your top focus."
    case "medium":
        reminder_message = f"Reminder: {task} is a MEDIUM priority task. Complete it soon."
    case "low":
        reminder_message = f"Reminder: {task} is a LOW priority task. Do it when convenient."
    case _:
        reminder_message = f"Reminder: {task} has an UNKNOWN priority level."

# If the task is time-bound, modify the reminder
if time_bound == "yes":
    reminder_message += " This task is time-bound — handle it immediately!"
else:
    reminder_message += " This task is not time-bound. You can plan it flexibly."

# Print the final reminder
print(reminder_message)

