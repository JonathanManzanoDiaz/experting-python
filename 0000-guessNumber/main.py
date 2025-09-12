# CREATE A GUESSING NUMBER GAME
import random
randomNumber = random.randint(1, 50)
giveNumber = 0
while giveNumber != randomNumber:
  giveNumber = int(input("Enter number to give: "))
  if giveNumber == randomNumber:
    print("You Win!")
  elif giveNumber > randomNumber:
    print("Your number is bigger")
  elif giveNumber < randomNumber:
    print("Your number is smaller")