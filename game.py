import os
import random
from time import sleep as sleep
from words import wordList

hangman = [
'''  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========='''
]
# Index 0 - 7

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def choose_word():
    word = random.choice(wordList)
    return word

def dict_to_str(dictionary):
    word = dictionary['word']
    hint = dictionary['hint']

    return [word, hint]

def start_game(chosen_word: str, tries: int, win: bool, death: bool):
    clear()
    print('Now its your time to guess the word!')
    print(chosen_word)

    
