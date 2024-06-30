task_description = input("Enter your task:")
task_priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match task_priority :
    case "high":
        print("Reminder:","'",task_description,"'", "is a high priority task")
            
    case "medium":
        print("Reminder:","'",task_description,"'", "is a high priority task")

    case "low":
        print("Note:","'",task_description,"'", "is a low priority task.")
        

if time_bound == "yes":
    print("that requires immediate attention today!")
else:
     print("Consider completing it when you have free time.")
