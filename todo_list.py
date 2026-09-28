tasks = []

while True:
    print()
    print("===== TO-DO LIST =====")
    print("1. Add a task")
    print("2. View the tasks")
    print("3. Exit")
    
    choice = input("\nChoose an option: ")
    
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")
        
    elif choice == "2":
        if tasks == []:
            print("You don't have any tasks!")
        else:
            print("Your tasks: ")
            
            number = 1
            for task in tasks:
                print(number, task)
                number = number + 1
                
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Please choose 1, 2, or 3.")