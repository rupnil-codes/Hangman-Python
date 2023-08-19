import os
import random

hangman = ['''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# Index: 0 - 6

def clear():
  os.system('cls')

clear()

print("----Hangman Game----")

print("\nPress enter to start: ")
input("")

while True:
  clear()
  try:
     print("The word was " + chosen_word)
  except:
    pass
  
  chosen_word = ""
  random_line = 1
  tries = 7
  death = False
  win = False
  letters_guessed = 0
  letters_remain = 0

  print("Select your desired mode:\n")
  print("1. Computer VS Player")
  print("2. Player 1 VS Player 2")
  print("\n*Press enter to exit*")
  mode_selection = input("\nEnter your selection: ")

  if mode_selection == "":
      clear()
      exit()
  elif mode_selection == "1":
      clear()
      print("Computer is thinking of a word...")

      with open("words.txt", 'r') as file:
        random_line = int(random.randint(1, 466551))
        lines = file.readlines()
        print("\nI have thought of a secret word. Press enter to continue")
        chosen_word = lines[random_line]
        chosen_word = chosen_word.upper()
        input("")
      
      clear()
      print("Now its your time to guess the word!")
      print(chosen_word)

      chosen_word_list = *chosen_word,
      chosen_word_list = list(chosen_word_list)
      chosen_word_list.pop(-1)
      print(chosen_word_list, "\n")

      print("Hints: \n\n- The word has", len(chosen_word_list), "letters")
      print("\nPress enter to continue")
      input()

      clear()

      while win != True and death != True:
          g1 = input("Guess a letter: ").upper()
          if g1 in chosen_word_list and tries != 0 and death != True:
              letters_guessed = chosen_word_list.count(g1) + letters_guessed
              letters_remain = len(chosen_word_list) - letters_guessed
              
              print('\nYou guessed a letter correctly! \n\n- The letter exists', chosen_word_list.count(g1), "times.\n-", letters_remain, "letters remain.\n-",letters_guessed, "letters guessed\n-", tries, "tries left.")
              input()
          elif tries == 0:
             win = False
             death = True
          else:
            tries -= 1
            print("You guessed a wrong letter.\n", letters_remain, "letters remain.\n-", tries, "tries left.")
            input()

  elif mode_selection == "2":
      pass
  else:
      pass
