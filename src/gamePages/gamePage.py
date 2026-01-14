import random
from time import sleep

import src.words as words

from src.gamePages.deathPage import gameover_death
from src.gamePages.winPage import gameover_win

from src.utils import clear
from src.colors import Colors

import string

full_hangman = [
        '''
    +----+
         |
         |
         |
         |
         |
=============''', '''
    +----+
    |    |
         |
         |
         |
         |
=============''', '''
    +----+
    |    |
    O    |
         |
         |
         |
=============''', '''
    +----+
    |    |
    O    |
    |    |
         |
         |
=============''', '''
    +----+
    |    |
    O    |
   /|    |
         |
         |
=============''', '''
    +----+
    |    |
    O    |
   /|\\   |
         |
         |
=============''', '''
    +----+
    |    |
    O    |
   /|\\   |
   /     |
         |
=============''', '''
    +----+
    |    |
    O    |
   /|\\   |
   / \\   |
         |
============='''
]
hangman_complete = [
    full_hangman, # EASY: Index 0 - 7 # 8 Tries; Hint at 8/2 = 4
    full_hangman[2:8], # MEDIUM: Index 2 - 8 # 6 Tries; Hint at 8/2 = 4
    full_hangman[4:8], # HARD: Index 4 - 8 # 4 Tries; Hint at 8/2 = 4
    full_hangman[6:8], # EXTREME: Index 7 - 8 # 2 Tries; Hint at 8/2 = 4
    full_hangman[7:8], # IMPOSSIBLE: Index 8 # 1 Try; Hint at None
]

alphabet = list(string.ascii_uppercase)

def choose_word():
    dictionary = random.choice(words.wordList)

    word = dictionary['word']
    hint = dictionary['hint']

    return [word, hint]

def draw_hangman(tries: int, hangman: list):
    if tries == 0:
        return
    print(Colors.YELLOW + Colors.BOLD + hangman[len(hangman) - tries] + "\n" + Colors.ENDC)

def check_win(letters_guessed_list: list, chosen_word: str) -> bool:
    word_list = *chosen_word,
    non_repeating_word_set = set(word_list)
    letters_guessed_set = set(letters_guessed_list)
    print(letters_guessed_set)

    if non_repeating_word_set in letters_guessed_set:
        return True
    else:
        return False

def check_death(tries: int):
    if tries == 0:
        return True
    else:
        return False

def think():
    print("Computer is thinking of a word.", end="\r")
    sleep(0.6)
    print("Computer is thinking of a word..", end="\r")
    sleep(0.6)
    print("Computer is thinking of a word...", end="\r")
    sleep(0.6)
    print("I have thought of a SECRET WORD. Press enter to continue: ", end="")
    input()
    clear()

def game(choice: int):
    if choice is None:
        return None

    hangman = hangman_complete[choice-1]
    tries_left = len(hangman)

    death = False
    win = False

    chosen_dict = choose_word()
    chosen_word = chosen_dict[0]
    chosen_word = chosen_word.upper()
    chosen_hint = chosen_dict[1]

    chosen_word_list = list(chosen_word)
    letters_guessed_list = []

    think()

    # draw_hangman(8, hangman_complete[0]) # Draw the default hangman!

    while win != True and death != True:
        if check_death(tries_left):
            death = True
            break
        win = True
        for letter in chosen_word_list:
            if letter in letters_guessed_list:
                pass
            else:
                win = False

        if win:
            break

        draw_hangman(tries_left, hangman)

        # print(chosen_word)

        # print(chosen_word_list)
        print("Hint: ", chosen_hint)
        print(tries_left, "/", len(hangman), " tries left")

        for letter in chosen_word_list:
            if letter in letters_guessed_list:
                print(Colors.UNDERLINE + Colors.BOLD + letter + Colors.ENDC, end=" ")
            else:
                print("＿", end=" ")

        print("\n")

        character_chosen = input("Guess a character: ")
        character_chosen = character_chosen.upper()

        if character_chosen == "":
            clear()
            continue
        elif character_chosen not in alphabet:
            clear()
            continue
        elif character_chosen in letters_guessed_list:
            clear()
            print("Already guessed, guess again...")
            continue
        else:
            letters_guessed_list.append(character_chosen)
            clear()

        if character_chosen not in chosen_word:
            tries_left -= 1

        clear()

    if win:
        gameover_win(chosen_word)
    elif death:
        gameover_death(chosen_word)

    input()
    clear()
    return None


