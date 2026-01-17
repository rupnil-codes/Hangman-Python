import os
from time import sleep
from src.colors import Colors

padding = "\t\b\b\b\b\b"

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def fail_message(message: str, ing_ing: str,hint: str = None, time: int = 3):
    print(Colors.BOLD + Colors.FAIL + message + Colors.ENDC)
    if hint is not None:
        print("Hint: " + hint)
    print("\n")
    for i in range(1, time+1):
        print(Colors.YELLOW + f"{ing_ing} in...", (time - i + 1), end='s \r' + Colors.ENDC)
        sleep(1.2)
    print("\n")

