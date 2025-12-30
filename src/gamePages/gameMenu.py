from src import config as cog
from src.colors import Colors
from src import utils
from src.utils import padding


def game_menu_options():
    print(Colors.BOLD + f"----------{cog.NAME} Game Menu----------" + Colors.ENDC)
    print("Choose a difficulty level (No. of wrong letters allowed):\n")
    print(padding + "1. Easy (8 tries)")
    print(padding + "2. Medium (6 tries)")
    print(padding + "3. Hard (4 tries)")
    print(padding + "4. Extreme (2 tries)")
    print(padding + "5. Impossible (1 try)\n")

def game_menu():
    while True:
        utils.clear()
        game_menu_options()
        try:
            choice = int(input("Enter your choice: "))
            utils.clear()
            return choice

        except ValueError:
            utils.clear()
            utils.fail_message("Invalid choice, please try again.", "Redirecting", "Please enter a choice from 1-5", 3)
            utils.clear()
            continue
