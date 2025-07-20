# Prompt for task description
task = input("Enter your task: ").strip()

# Prompt for task priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Match case based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unspecified priority"

# Check time sensitivity and add final message
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the final message
print("\n" + message)