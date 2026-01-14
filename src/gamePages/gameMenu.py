from src import config as cog
from src.colors import Colors
from src import utils
from src.utils import padding


def game_menu_options(error: bool = False, message: str = None, hint: str = None):
    if not error:
        print(Colors.BOLD + f"----------{cog.NAME} Game Menu----------" + Colors.ENDC)
        print("Choose a difficulty level (No. of wrong letters allowed):\\n" + Colors.ENDC)
        print(Colors.GREEN + Colors.BOLD + padding + "1. Easy (8 tries)" + Colors.ENDC)
        print(Colors.GREEN + Colors.BOLD + padding + "2. Medium (6 tries)" + Colors.ENDC)
        print(Colors.YELLOW + Colors.BOLD + padding + "3. Hard (4 tries)" + Colors.ENDC)
        print(Colors.YELLOW + Colors.BOLD + padding + "4. Extreme (2 tries)" + Colors.ENDC)
        print(Colors.RED + Colors.BOLD + padding + "5. Impossible (1 try)\\n" + Colors.ENDC)
        print(padding + Colors.BOLD + Colors.CYAN + "6. " + Colors.BLUE + "G" + Colors.GREEN + "a" + Colors.RED + "m" + Colors.CYAN + "b" + Colors.BLUE + "l" + Colors.GREEN + "e " + Colors.RED + "(" + Colors.CYAN + "? "  + Colors.BLUE + "t" + Colors.GREEN + "r" + Colors.RED + "y" + Colors.CYAN + ")\\n" + Colors.ENDC)
    else:
        print(Colors.BOLD + f"----------{cog.NAME} Game Menu----------" + Colors.ENDC)
        print(Colors.BOLD + Colors.FAIL + message + Colors.ENDC)
        if hint is not None:
            print("Hint: " + hint + "\\n")
        print("Choose a difficulty level (No. of wrong letters allowed):\\n")
        print(padding + "1. Easy (8 tries)")
        print(padding + "2. Medium (6 tries)")
        print(padding + "3. Hard (4 tries)")
        print(padding + "4. Extreme (2 tries)")
        print(padding + "5. Impossible (1 try(s))\\n")

def game_menu():
    error = False

    while True:
        try:
            game_menu_options(error, "Invalid choice, please try again.", "Please enter a choice from 1-5")
            choice = input("Enter your choice (X to return): ")
            utils.clear()
            if choice.upper() == "X":
                return None
            choice = int(choice)
            if choice > 6 or choice < 1:
                raise ValueError
            return choice

        except ValueError:
            utils.clear()
            error = True
            continue

