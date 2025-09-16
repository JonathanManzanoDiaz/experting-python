import csv
def ask_add_item(num):
  name = input('What is the name of what you payed? ')
  price = float(input('What is the price you payed? '))
  print(f"{name} added with the {price} correctly to {num}")
  with open('costs.csv', 'a', newline="") as file:
    writer = csv.writer(file)
    writer.writerow([num, name, price])
  
def add_item():
  categoriesTitle = 'Categories'.center(20, '=')
  print(categoriesTitle)
  print('1. Costs')
  print('2. Food')
  print('3. Fun')
  ask_category_to_add()

def ask_category_to_add():
  optionCategory = int(input("What category do you want? "))
  if optionCategory == 1:
    ask_add_item('Costs')
  elif optionCategory == 2:
    ask_add_item('Food')
  elif optionCategory == 3:
    ask_add_item('Fun')
  else:
    print("Invalid number, try again!")

def delete_item():
  listItems = []
  with open('costs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i, item in enumerate(csv_reader):
      listItems.append(item)
      print(i, item)
  ask_delete = int(input('Type the number of the item you want to delete: '))
  if 0 <= ask_delete < len(listItems):
    listItems.pop(ask_delete)
  else:
    print("Invalid number!")
  with open('costs.csv', 'w', newline="") as file:
    f = csv.writer(file)
    clean_list = [row for row in listItems if row and len(row) == 3]
    f.writerows(clean_list)
    
def show_all():
  with open('costs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    categoriesTitle = 'Categories'.center(20, '=')
    print(categoriesTitle)
    print('What category do you want?')
    print('1. Show All ')
    print('2. Costs')
    print('3. Food')
    print('4. Fun')
    ask_show = int(input("Of what category do you want to show: ")) - 1
    for row in csv_reader:
      if ask_show == 0:
        print(row)
      if row[0] == "Costs" and ask_show == 1:
        print(row)
      if row[0] == "Food" and ask_show == 2:
        print(row)
      if row[0] == "Fun" and ask_show == 3:
        print(row)
    
    

option = -1
while option != 0:
  title = 'Menu'.center(20, '=')
  print(title)
  print('1. Add Cost')
  print('2. Delete Cost')
  print('3. Show All')
  print('4. Exit')
  option = int(input("What do you want to do? "))
  if option == 1:
    add_item()
  elif option == 2:
    delete_item()
  elif option == 3:
    show_all()
  else:
    option = 0