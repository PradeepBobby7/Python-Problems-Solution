import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    
print(logo)
word_list = ["apple","banana","tomato","coffee"]
word = random.choice(word_list)
result = []
for _ in range(len(word)):
    result += '_'
print(result)
game = False
lives=6
while not game:
    letter = input("Guess a letter on the word: ")
    for position in range(len(word)):
        new=word[position]
        if letter==new:
            result[position] = new
    if letter not in word:
        lives-=1
        if lives==0:
            game=True
            print("You Loss")
    print(result)
    if '_' not in result:
        print("You Win")
    print(stages[lives])
