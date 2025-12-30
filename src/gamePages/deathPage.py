from src.colors import Colors

hangman_death = '''
   +----+
   |    |
   O    |
  /|\\   |
  / \\   |
  X X   |
=========='''

def gameover_death(word: str):
    print(Colors.YELLOW + Colors.BOLD + hangman_death + "\n" + Colors.ENDC)
    print("Hangman died T-T\n")
    print("The word I chose was: " + word.upper())
    print("\n Play again to save other hangman(s) or to flex to your friends!")
    print("\nPress Enter to continue...")