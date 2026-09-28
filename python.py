tasks = []

def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("your Task is added!")

    elif choice == "2":
        print("\nYour Tasks are :")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

    elif choice == "3":
        num = int(input("Enter your task number to be deleted: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")
        else:
            print("Invalid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:

        print("Invalid choice")