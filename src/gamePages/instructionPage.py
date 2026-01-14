from src.utils import clear


def instructions():
    clear()
    print("========== How to Play ==========\n")

    print("This is a classic Hangman-style word guessing game.\n")
    print("""1. The computer will choose a secret word.
2. You must guess the word one letter at a time.
3. Each wrong guess adds a part to the hangman.
4. You WIN if you guess the word before the drawing is complete.
5. You LOSE if the hangman is fully drawn and hence, HANGED.

Rules:
- Only single-letter guesses are allowed.
- Repeating a guessed letter will not help you.
- Guess wisely. You have limited chances.

Good luck. Your vocabulary is your only weapon.

======================================================
""")
    input("Press Enter to go back...")