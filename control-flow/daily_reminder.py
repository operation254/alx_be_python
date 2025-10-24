# daily_reminder.py

# Ask the user for details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine the reminder message
reminder_message = f"Reminder: {task} is a {priority} priority task."

# Modify if the task is time-bound
if time_bound == "yes":
    reminder_message += " Make sure to complete it as soon as possible!"
else:
    reminder_message += " You can complete it when you have free time."

# Print final reminder
print(reminder_message)
