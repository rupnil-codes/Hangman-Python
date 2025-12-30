from src.colors import Colors

hangman_win = '''
   +----+
        |
        |
   \\O/  |
    |   |
   / \\  |
============='''

def gameover_win(word: str):
    print(Colors.YELLOW + Colors.BOLD + hangman_win + "\n" + Colors.ENDC)
    print("Hangman lived :D!\n")
    print("The word I chose was: " + word.upper())
    print("\nPlay again to save other hangman(s) or to flex to your friends!")
    print("\nPress Enter to continue...")


