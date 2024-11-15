import random 

def play():
  print('Welcome to Slots!')
  print('Let\'s play!')
  print('              ')
  
  symbols = '🍒',' 🍇', '🍉', '7️⃣'
  
  results = print(random.choice(symbols) + " |" + random.choice(symbols) + " |" + random.choice(symbols))

  if results == ['7️⃣', '7️⃣', '7️⃣']:
    print('Jackpot!💰')
    print('          ')
  else:
    print('Thanks for playing!')
    print('          ')

def main():
  while True:
    play()
    continue_playing = input('Would you like to play again?(Y or N): ')
    if continue_playing == 'Y':
      continue
    elif continue_playing == 'N':
      print('Thank you for playing Slots!')
      break
    else:
      print("Invalid response.")

main()