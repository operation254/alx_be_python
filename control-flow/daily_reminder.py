# Uses match/case for priority handling plus if for time sensitivity.

task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        priority_text = "a high priority task"
    case "medium":
        priority_text = "a medium priority task"
    case "low":
        priority_text = "a low priority task"
    case _:
        priority_text = "a task"

if time_bound in {"y", "yes"}:
    print(f"Reminder: '{task}' is {priority_text} that requires immediate attention today!")
else:
    if priority in {"high", "medium", "low"}:
        print(f"Note: '{task}' is {priority_text}. Consider completing it when you have free time.")
    else:
        print(f"Note: '{task}' has unspecified priority. Consider completing it when you have free time.")
