
import random
import os 
stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game=False
lives=6
display=[]
for _ in range(word_length):
    display +="_"

#print(display)  


while not end_of_game:
    guess =input("Guess a letter :").lower()

    os.system('cls')

    if guess in display:
        print(f"You'v already guessed{guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        #print(f"Current position :{position}\nCurrent letter:{letter}\nGuessed letter:{guess}")
        if letter == guess:
            display [position]=letter

    if guess  not in  chosen_word :
        print(f"You guesse{guess},that's not in the word. You lose a life. ")
        lives-=1            
        if lives==0:
            end_of_game=True
            print("You lose")

    print(f"{''.join(display)}")       
    
    if "_" not in display:
        end_of_game =True
        print("You win")
    print(stages[lives])        
    