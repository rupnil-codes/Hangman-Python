import os
import random
from time import sleep as sleep
from words import wordList
import config as cog

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
    dictionary = random.choice(wordList)

    word = dictionary['word']
    hint = dictionary['hint']

    return [word, hint]


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    WARNING = '\033[93m' # YELLOW
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def start_menu_options():
    print(colors.BOLD + "----------Start Menu----------\n" + colors.ENDC)
    print("1. Play Game")
    print("2. How to play?")
    print("3. Exit\n")
def fail_message(message: str, ing_ing: str,hint: str = None, time: int = 3):
    print(colors.BOLD + colors.FAIL + message + colors.ENDC)
    if hint is not None:
        print("Hint: " + hint)
    print("\n")
    for i in range(1, time+1):
        print(colors.YELLOW + f"{ing_ing} in...", (time - i + 1), end='s \r' + colors.ENDC)
        sleep(1.3)
    print("\n")

if __name__ == '__main__':
    clear()
    print(colors.UNDERLINE + colors.BOLD + colors.OKGREEN + f"{cog.NAME} Game {cog.VERSION} ({cog.PROGRAMING_LANGUAGE})" + colors.ENDC)
    print(colors.YELLOW + "Made with " + colors.RED + colors.BOLD + "LOVE" + colors.ENDC + colors.YELLOW + " by " + colors.OKBLUE + colors.UNDERLINE + f"{cog.AUTHOR}\n" + colors.ENDC)

    input("Press enter to continue...")
    clear()

    # Start Menu
    while True:
        start_menu_options()
        try:
            choice = int(input("Enter your choice: "))
            clear()
            break
        except ValueError:
            clear()
            fail_message("Invalid choice, please try again.", "Redirecting", "Please enter a choice from 1-3", 3)
            clear()
            continue

    if choice == 1:
        tries = 8
        death = False
        win = False
        letters_guessed = 0
        letters_remaining = 0
        letters_guessed_list = []

        chosen_dict = choose_word()
        chosen_word = "rainbowing"
        chosen_hint = chosen_dict[1]
        chosen_word_list = list(chosen_word)
        print(chosen_word_list, chosen_hint)
        print(chosen_word_list.remove("i"))

        print("Computer is thinking of a word...\n")
        input("I have thought of a secret word. Press enter to continue...")



    elif choice == 2:
        print("How to play?")

    elif choice == 3:
        clear()
        fail_message("See you again! You have chosen to Exit the game.", "Exiting", None, 3)
        exit()

    else:
        print(colors.BOLD + colors.RED + "Oops! an error occured." + colors.ENDC)

