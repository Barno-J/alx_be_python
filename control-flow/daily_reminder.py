# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
print("\nReminder:", end=" ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. You should focus on this soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed soon!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but has a deadline. Try to schedule it.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please try again with high/medium/low.")