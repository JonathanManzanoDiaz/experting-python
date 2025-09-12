import random

# number of lives
number = 6

# word list
words = [
  "cat", "dog", "sun", "book", "tree", "fish", "ball", "star", "moon", "milk",
  "python", "guitar", "planet", "rocket", "school", "jungle", "castle", "window", "garden", "desert",
  "elephant", "adventure", "chocolate", "dinosaur", "mountain", "kangaroo", "astronomy", "microscope", "volcano",
  "technology"
]

# pick a random word
guessWord = random.choice(words)
guessedLetters = []

# START LOOP
while number > 0:
  # CLEAN THE HANGED GAME
  wordPrinted = ""
  # IF LETTER IN THE GUESS WORD AND THE LETTER IS IN GUESSED LETTERS SHOW wordprinted with the new letter
  for letter in guessWord:
    if letter in guessedLetters:
      wordPrinted += letter
    else:
      # or show _
      wordPrinted += "_"
  
  # print the word and letters you have guessed
  print("Word:", wordPrinted)
  # if the wordprinted is the same that guessword you win
  if wordPrinted == guessWord:
    print("You guessed it. The guess word was:", guessWord)
    break
    
  #Type a letter
  guessLetter = input("Guess a letter: ").lower()
  # if the letter you introduce is in the guessed letter before continue after showing it
  if guessLetter in guessedLetters:
    print("You guessed that letter before", guessLetter)
    continue
  # else append to the guessed letters
  else:
    guessedLetters.append(guessLetter)
  # if guess letter is not in guessword you lose one life
  if guessLetter not in guessWord:
    print("Wrong guess!")
    number -= 1
    #show how many lives you have left
    print(f"You have {number} guess left")
  
  # if you lost all the 5 lives, you lose.
  if number == 0:
    print("Game over! You lost! The guess word was: ", guessWord)
    break