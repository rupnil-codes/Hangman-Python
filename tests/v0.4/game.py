from src.gamePages.instructionPage import instructions
from src.gamePages.settingsPage import settings
from src.utils import clear
from src.gamePages.startMenu import credits, start_menu
from src.gamePages.gameMenu import game_menu
from src.gamePages.gamePage import game
from src import utils

if __name__ == '__main__':
    credits()

    while True:
        # StartMenu includes Onboarding!
        choice = start_menu()
        if choice == 1:
            while True:
                # Game Menu
                choice = game_menu()

                if choice is None:
                    break
                # Game
                game(choice)

        elif choice == 2:
            instructions()

        elif choice == 3:
            settings()

        elif choice == 4:
            clear()
            utils.fail_message("See you again! You have chosen to Exit the game.", "Exiting", None, 3)
            exit()

        else:
            clear()
            utils.fail_message("Oops! an unexpected error occured. Please restart.", "Exiting", None, 3)
            exit()

