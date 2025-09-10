import csv
import time
# MENU AGENDA
option = -1

def read_contacts():
  with open('contacts.csv', 'r', encoding='utf-8') as f:
    contacts = list(csv.reader(f))
  return contacts

while option != 0:
  title = "Menu".upper()
  print(title.center(20, '='))

  print("Select your option")
  print("1. Add a contact")
  print("2. Delete a contact")
  print("3. View all contacts")
  print("4. Exit")
  option = int(input("Select option: "))

  if option == 1:
    name = input("Type the name you want to add: ")
    number = input(f"Type the number of {name}: ")
    print("Contact added successfully")
    with open('contacts.csv', 'a', newline='') as f:
      writer = csv.writer(f)
      writer.writerow([name, number])
    time.sleep(1)
  
  elif option == 2:
    contacts = read_contacts()
    for i, contact in enumerate(contacts, start=1):
      print(i, contact)
    ask_del = int(input("Type the number you want to delete: "))
    if 1 <= ask_del <= len(contacts):
      contacts.pop(ask_del - 1)
      with open('contacts.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(contacts)
      print("Contact deleted successfully")
    else:
      print("Invalid number")
      time.sleep(1)
    
  elif option == 3:
    print(" ".center(20))
    print("Contacts".center(20))
    
    contacts = read_contacts()
    for i, contact in enumerate(contacts, start=1):
      print(i, contact)
    print("-".center(20, "-"))
  
  elif option == 4:
    print("Exiting... Goodbye, have a nice day!")
    time.sleep(1)
    option = 0
    