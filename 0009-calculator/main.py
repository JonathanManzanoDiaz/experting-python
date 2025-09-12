title = "Menu".upper()
print(title.center(20, "="))
print("Operators".center(20))
print("Add".ljust(16, ".") + "1".rjust(4))
print("Substract".ljust(16, ".") + "2".rjust(4))
print("Multiply".ljust(16, ".") + "3".rjust(4))
print("Divide".ljust(16, ".") + "4".rjust(4))
print("Cube".ljust(16, ".") + "5".rjust(4))
print("Exit".ljust(16, ".") + "0".rjust(4))

operator = input("Tell me what do you want to do: ")

while operator != "exit":
  if operator == "1":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print("Result:", first_number + second_number)
    exit()
  elif operator == "2":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print("Result:", first_number - second_number)
    exit()
  elif operator == "3":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print("Result:", first_number * second_number)
    exit()
  elif operator == "4":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print("Result:", first_number / second_number)
    exit()
  elif operator == "5":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print("Result:", first_number ** second_number)
    exit()
  elif operator == "0":
    exit();