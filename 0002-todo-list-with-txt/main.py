def show_options():
    print('\nWelcome to To Do List with File txt')
    print('1 - Add task')
    print('2 - Delete task')
    print('3 - Show all tasks')
    print('0 - Exit')

def add_tasks(task):
    with open("tasks.txt", 'a') as f:
        f.write(task)
        print(f"The task is added succesfully!")

def delete_task():
    tasks = []
    with open("tasks.txt", "r", encoding="utf8") as f:
        f.seek(0)
        lines = f.readlines()
        for line in lines:
            tasks.append(line)
        f.close()
    if len(tasks) > 0:
        show_tasks()
    else:
        print("There is not tasks in the list.")
        
    task = int(input('What task do you want to delete?: '))
    try:
        if len(tasks) >= task:
            tasks.pop(task - 1)
        else:
            print("Error, this task number doesn't exist")
    except ValueError:
        print('The list is empty!')
    with open('tasks.txt', 'w', encoding='utf8') as f:
        f.seek(0)
        for task in tasks:
            f.write(task)

def show_tasks():
    with open("tasks.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        if len(lines) > 0:
            for i, line in enumerate(lines, start=1):
                print(i, line.strip('\n'))
            f.close()
        else:
            print("There is not tasks in the list.")

while True:
    show_options()
    option = int(input('Select an option: '))
    if option == 1:
        task = input('What task do you want to add?: ')
        add_tasks(f"{task}\n" )
    elif option == 2:
        delete_task()
    elif option == 3:
        show_tasks()
    else:
        print('Goodbye, Have a nice day!')
        break