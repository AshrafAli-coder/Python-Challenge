import random
import hangman_words
from hangman_words import word_list
process=[r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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
lives=6
correct_guess=[]
chosen_word=random.choice(word_list)
print(chosen_word)
display=""
for i in range(len(chosen_word)):
    display+="_"
print(f"Word to be guessed: "+display)
while lives!=0:
    display1=""
    guess=input("Guess a letter: ")
    for letter in chosen_word:
        if guess==letter:
            display1+=letter
            correct_guess.append(letter)
        elif letter in correct_guess:
            display1+=letter
        else:
            display1+="_"
    print(display1)
    if guess not in chosen_word:
        print(f"You guessed {guess}, not in the word, You looses a life")
        lives-=1
        print(f"********{lives}/6 are left********")
        print(process[lives])
    if display1==chosen_word:
        break
if lives==0:
    print(f"****It is {chosen_word} GAME OVER!****")
elif display1==chosen_word:
    print("********HURRAY!!!You Win*********")