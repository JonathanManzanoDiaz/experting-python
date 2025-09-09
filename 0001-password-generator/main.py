import random
import string
print("Welcome to the Password Generator by Jonathan Manzano Diaz")
# Here is the password length you want to generate
password_length = int(input("Enter the password length: "))
generatedPassword = ""

listPassword = string.ascii_letters + string.digits + string.punctuation
number = int(len(listPassword))

for i in range(password_length):
  random_char = random.randrange(0, number)
  generatedPassword = generatedPassword + listPassword[random_char]
print(generatedPassword)
exit()