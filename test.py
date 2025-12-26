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
=========''']
# Index: 0 - 6


import os
import random
from time import sleep as sleep

def clear():
    os.system('cls')

def listToString(lst: list) -> str:
    string = ""
    for element in lst:
        string += element

    return string

def match_with_list(list1: list, list2: list) -> list:
    output = []

    for item in list1:
        if item in list2:
            output.append(item)
        else:
            output.append("")

    return output

def start_game(chosen_word: str, tries: int, win: bool, death: bool):
      clear()
      print("Now its your time to guess the word!")
      # print(chosen_word)

      chosen_word_list = *chosen_word,
      chosen_word_list = list(chosen_word_list)
      chosen_word_list.pop(-1)
      chosen_word = listToString(chosen_word_list)
      # print(chosen_word_list, "")

      print("Hints: - The word has", len(chosen_word_list), "letters")
      print("Press enter to continue")
      input()

      clear()

      while win != True and death != True:
          g1 = input("Guess a letter: ").upper()
          if g1 in chosen_word_list and tries != 0 and death != True and not g1 in letters_guessed_list:
              letters_guessed = chosen_word_list.count(g1) + letters_guessed
  
              letters_remain = len(chosen_word_list) - letters_guessed
              
              letters_guessed_list.append(g1)
              
              print('\nYou guessed a letter correctly! \n\n- The letter exists', chosen_word_list.count(g1), "times.\n-", letters_remain, "letters remain.\n-",letters_guessed, "letters guessed\n- The letters you have guessed are: ", letters_guessed_list,"\n-", tries, "tries left.")
              print("\nThe current word is: ", match_with_list(chosen_word_list, letters_guessed_list))
              # input()
          elif g1 in letters_guessed_list:
             print("\nYou already guessed the letter\n")
             print("\nThe current word is: ", match_with_list(chosen_word_list, letters_guessed_list))

          elif g1 == chosen_word:
             sleep(0.1)
             clear()
             print("Bravo! You guessed the word correctly!\n\nYour Stats:\n- Tries left: ", tries ,"\n")
             print("Press enter to continue")
             input()
             win = True
             death = False

          elif tries == 0:
             sleep(0.1)
             clear()
             print(hangman[6])
             print("\nYou lost the game of hangman :(. Hangman died\nThe word I choose was: ", chosen_word)
             print("\n- You guessed", letters_guessed, "letters correctly\n- The letters were: ",letters_guessed_list,"\n")
             print("Press enter to continue")
             input()
             win = False
             death = True

          else:
            print(hangman[6 - tries])
            print("You guessed a wrong letter.\n", letters_remain, "letters remain.\n-", tries, "tries left.")
            print("\nThe current word is: ", match_with_list(chosen_word_list, letters_guessed_list))
            # input()
            tries -= 1
# clear()

print("----Hangman Game----")

print("\nPress enter to start: ")
input("")

while True:
  clear()

  chosen_word = ""
  random_line = 1
  tries = 6
  death = False
  win = False
  letters_guessed = 0
  letters_remain = 0
  letters_guessed_list = []

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
      # print(chosen_word)

      chosen_word_list = *chosen_word,
      chosen_word_list = list(chosen_word_list)
      chosen_word_list.pop(-1)
      chosen_word = listToString(chosen_word_list)
      # print(chosen_word_list, "\n")

      print("Hints: \n\n- The word has", len(chosen_word_list), "letters")
      print("\nPress enter to continue")
      input()

      clear()

      while win != True and death != True:
          g1 = input("\nGuess a letter: ").upper()
          if g1 in chosen_word_list and tries != 0 and death != True and not g1 in letters_guessed_list:
              letters_guessed = chosen_word_list.count(g1) + letters_guessed
              letters_remain = len(chosen_word_list) - letters_guessed
              letters_guessed_list.append(g1)
              print('\nYou guessed a letter correctly! \n\n- The letter exists', chosen_word_list.count(g1), "times.\n-", letters_remain, "letters remain.\n-",letters_guessed, "letters guessed\n- The letters you have guessed are: ", letters_guessed_list,"\n-", tries, "tries left.")
              print("\nThe current word is: ", match_with_list(chosen_word_list, letters_guessed_list))
              # input()
          elif g1 in letters_guessed_list:
             print("\nYou already guessed the letter\n")
             print("\nThe current word is: ", match_with_list(chosen_word_list, letters_guessed_list))

          elif g1 == chosen_word:
             sleep(0.1)
             clear()
             print("Bravo! You guessed the word correctly!\n\nYour Stats:\n- Tries left: ", tries ,"\n")
             print("Press enter to continue")
             input()
             win = True
             death = False

          elif tries == 0:
             sleep(0.1)
             clear()
             print(hangman[6])
             print("\nYou lost the game of hangman :(. Hangman died\nThe word I choose was: ", chosen_word)
             print("\n- You guessed", letters_guessed, "letters correctly\n- The letters were: ",letters_guessed_list,"\n")
             print("Press enter to continue")
             input()
             win = False
             death = True

          else:
            print(hangman[6 - tries])
            print("You guessed a wrong letter.\n", letters_remain, "letters remain.\n-", tries, "tries left.")
            print("\nThe current word is: ", match_with_list(chosen_word_list, letters_guessed_list))
            # input()
            tries -= 1

  elif mode_selection == "2":
      clear()
      print("Its time for Player 1 to choose a word for Player 2")
      chosen_word = input("\nPlayer 1 enter any word: ")
      chosen_word = chosen_word.upper()

      clear()
      print("Now its Player 2's time to guess the word!\n")
      # print(chosen_word)

      chosen_word_list = *chosen_word,
      chosen_word_list = list(chosen_word_list)

      print("Hints: \n\n- The word has", len(chosen_word_list), "letters")
      print("\nPress enter to continue")
      input()

      clear()

      while win != True and death != True:
          g1 = input("\nGuess a letter: ").upper()
          if g1 in chosen_word_list and tries != 0 and death != True and not g1 in letters_guessed_list:
              letters_guessed = chosen_word_list.count(g1) + letters_guessed
              letters_remain = len(chosen_word_list) - letters_guessed
              letters_guessed_list.append(g1)
              print('\nYou guessed a letter correctly! \n\n- The letter exists', chosen_word_list.count(g1), "times.\n-", letters_remain, "letters remain.\n-",letters_guessed, "letters guessed\n- The letters you have guessed are: ", letters_guessed_list,"\n-", tries, "tries left.")
              print("\nThe current word is: ", match_with_list(chosen_word_list, letters_guessed_list))
              # input()
          elif g1 in letters_guessed_list:
             print("\nYou already guessed the letter\n")
             print("\nThe current word is: ", match_with_list(chosen_word_list, letters_guessed_list))

          elif g1 == chosen_word:
             sleep(0.1)
             clear()
             print("Bravo! You guessed the word correctly!\n\nYour Stats:\n- Tries left: ", tries ,"\n")
             print("Press enter to continue")
             input()
             win = True
             death = False

          elif tries == 0:
             sleep(0.1)
             clear()
             print(hangman[6])
             print("\nYou lost the game of hangman :(. Hangman died\nThe word I choose was: ", chosen_word)
             print("\n- You guessed", letters_guessed, "letters correctly\n- The letters were: ",letters_guessed_list,"\n")
             print("Press enter to continue")
             input()
             win = False
             death = True

          else:
            print(hangman[6 - tries])
            print("You guessed a wrong letter.\n", letters_remain, "letters remain.\n-", tries, "tries left.")
            print("\nThe current word is: ", match_with_list(chosen_word_list, letters_guessed_list))
            # input()
            tries -= 1
  else:
      pass
