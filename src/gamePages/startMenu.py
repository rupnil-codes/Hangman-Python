from time import sleep

from src.colors import Colors
from src import config as cog
from src.config import ONBOARDING
from src.utils import clear, fail_message, padding
from src import dataManagement as dM

def onboarding():
    try:
        user_data = dM.read(dM.user_file)
        if user_data["onboarding"]:
            print(f"Welcome Back, {user_data["username"]}! \n")

    except FileNotFoundError:
        clear()
        print(Colors.UNDERLINE + Colors.BOLD + Colors.GREEN + f"{cog.NAME} Game {cog.VERSION} ({cog.PROGRAMING_LANGUAGE})" + Colors.ENDC)
        print(Colors.YELLOW + "Made with " + Colors.RED + Colors.BOLD + "LOVE" + Colors.ENDC + Colors.YELLOW + " by " + Colors.BLUE + Colors.UNDERLINE + f"{cog.AUTHOR}\n" + Colors.ENDC)

        input("Press enter to continue onboarding...")
        clear()
        username = input("Enter Username (default: 'user'): ")


        data = {
            "onboarding": True,
            "username": username,
            "games_played": 0,
            "games_won": 0,
            "games_lost": 0,
            "win_rate": 0,
        }

        dM.write(dM.user_file, data)
        clear()

        print(f"Welcome, {username}!")

def start_menu_options(error: bool = False, message: str = None, hint: str = None):
    if not error:
        print(Colors.BOLD + f"----------{cog.NAME} Start Menu (BETA)----------\n" + Colors.ENDC)
        print(padding + "1. Start a Game")
        print(padding + "2. How to play?")
        print(padding + "3. Settings")
        print(padding + "4. Quit\n")
    else:
        print(Colors.BOLD + f"----------{cog.NAME} Start Menu (BETA)----------" + Colors.ENDC)
        print(Colors.BOLD + Colors.FAIL + message + Colors.ENDC)
        if hint is not None:
            print("Hint: " + hint)
        print("\n")
        print(padding + "1. Start a Game")
        print(padding + "2. How to play?")
        print(padding + "3. Settings")
        print(padding + "4. Quit\n")

def start_menu():
    error = False
    choice = None

    if ONBOARDING:
        onboarding()

    print(Colors.UNDERLINE + Colors.BOLD + Colors.GREEN + f"{cog.NAME} Game {cog.VERSION} ({cog.PROGRAMING_LANGUAGE})" + Colors.ENDC)
    print(Colors.YELLOW + "Made with " + Colors.RED + Colors.BOLD + "LOVE" + Colors.ENDC + Colors.YELLOW + " by " + Colors.BLUE + Colors.UNDERLINE + f"{cog.AUTHOR}\n" + Colors.ENDC)
    sleep(1.5)

    clear()

    while True:
        try:
            start_menu_options(error, "Invalid choice, please try again.", "Please enter a choice from 1-4")
            choice = int(input("Enter your choice: "))
            if choice > 4 or choice < 1:
                raise ValueError
            break
        except ValueError:
            clear()
            error = True
            continue

    return choice

