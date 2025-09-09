
# open the file as read and write
tasks_file = open("tasks.txt", "a+")

def read_tasks(f):
  #READ ALL THE LINES AGAIN
  f.seek(0)
  return f.readlines()

def write_tasks(f, lines):
  #WRITE ALL THE TASKS AGAIN
  norm = [(ln.rstrip("\n") + "\n") for ln in lines]
  f.seek(0)
  f.truncate(0)
  f.writelines(norm)
  f.flush()

def ask_int(prompt):
  val = input(prompt).strip()
  return int(val) if val.isdigit() else None

# Option input
option = -1
# Option loop
while option != 0:
  tasks_file.seek(0)

  #MENU TASKS
  title = "Menu".upper()
  print(title.center(20, "="))
  print("Tasks".center(20))
  
  # READ LINES of the file
  content = read_tasks(tasks_file)
  
  # PRINT THE TASKS, IF It's empty, Tell there is no task
  if len(content) == 0:
    print("You don't have any tasks yet")
  else:
    for index, task in enumerate(content, start=1):
      print(index, task.strip())
  
  # print "---" for separate the options from the tasks
  print("-".center(20, "-"))
  
  # Print the options
  print("Add".ljust(16, ".") + "1".rjust(4))
  print("Delete".ljust(16, ".") + "2".rjust(4))
  print("Update Task".ljust(16, ".") + "3".rjust(4))
  print("Exit".ljust(16, ".") + "0".rjust(4))
  
  
  # Select the option
  option = int(input("Enter your option: "))
  if option == 1:
    # ADD THE TASK
    task = input("Enter the task you want to add: ")
    tasks_file.write(task + "\n")
    tasks_file.flush()
  
  elif option == 2:
    # DELETE THE TASK
    if not content:
      print("There are no tasks to delete.")
      continue
    n = ask_int("Enter the number of the task you want to delete: ")
    if n is None or n < 1 or n > len(content):
      print("This number is out of range")
      continue
    content.pop(n - 1)
    write_tasks(tasks_file, content)
    
  elif option == 3:
    # UPDATE THE TASK
    idx = ask_int("Enter the number of the task you want to update: ") - 1
    
    if idx < 0 or idx >= len(content):
      print("This number is out of range")
    else:
      new_task = input("Enter the update of the task: ").strip()
      content[idx] = new_task.rstrip("\n") + "\n"
      write_tasks(tasks_file, content)
  elif option == 0:
    # EXIT THE APP
   print("\n Goodbye. Have a nice day!")

tasks_file.close()
