import random

def start_game(scorePlayer, scoreAI):
  options = ['Rock', 'Paper', 'Scissors']
  
  print('\nSelect your option: ')
  print('1. Rock')
  print('2. Paper')
  print('3. Scissors')
  print('0. Exit')
  
  try:
    optionPlayer = int(input('What do you want? '))
  except ValueError:
    print("Please enter a number (0-3).")
    return scorePlayer, scoreAI, True
  
  if optionPlayer == 0:
    return scorePlayer, scoreAI, False
  
  if optionPlayer not in [1, 2, 3]:
    print("Invalid choice, try again.")
    return scorePlayer, scoreAI, True
  
  player = options[optionPlayer - 1]
  optionAI = random.choice(options)
  
  print(player, 'vs', optionAI)
  
  if player == 'Rock' and optionAI == 'Scissors' or player == 'Paper' and optionAI == 'Rock' or player == 'Scissors' and optionAI == 'Paper':
    scorePlayer += 1
  elif player == optionAI:
    print("DRAW!")
  else:
    print("Computer Wins!")
    scoreAI += 1
  
  print('Your score is:', scorePlayer)
  print('AI score:', scoreAI)
  
  return scorePlayer, scoreAI, True


scorePlayer = 0
scoreAI = 0
playing = True

while playing:
  scorePlayer, scoreAI, playing = start_game(scorePlayer, scoreAI)
