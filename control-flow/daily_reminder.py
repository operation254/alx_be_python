# daily_reminder.py

# Ask user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case structure
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a HIGH priority task that is time-bound. Complete it immediately!")
        else:
            print(f"Reminder: {task} is a HIGH priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a MEDIUM priority task that is time-bound. Try to do it soon!")
        else:
            print(f"Reminder: {task} is a MEDIUM priority task. You can schedule it later.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a LOW priority task but is time-bound. Don’t forget it!")
        else:
            print(f"Reminder: {task} is a LOW priority task. You can do it whenever you have time.")
    case _:
        print(f"Reminder: {task} has an UNKNOWN priority. Please review your entry.")
