import sys
from importlib.metadata import version

from cli_ui import print_logo, clear, goto, get_termcol, display_width, text_center, screen_center, \
    get_term_size, prompt, prompt_yn, prompt_int

col1 = get_termcol((20, 245, 170))
col2 = get_termcol((255, 73, 158))
offset = 0


def get_offset():
    return ((get_term_size()[0] // 2) - 26)


def main():
    while get_term_size()[0] <= 64:
        clear()
        input(
            f"{col1}Your terminal is too small!\nIt must be at least {col2}64{col1}x{col2}12{col1}.\nHit {col2}Enter{col1} to retry...")
    clear()

    print_logo(center=True)
    print(screen_center(f"{col1}(by {col2}@qwik{col1}, version {col2}v0.1{col1})!!"))
    print()
    print(screen_center(f"{col1}╔════════════════════════════════════════════════╗"))
    print(screen_center(f"{col1}║  Thanks for picking {col2}bahhh{col1}!! you are very cool  ║"))
    print(screen_center(f"{col1}╠════════════════════════════════════════════════╣"))
    print(screen_center(f"{col1}║ {col2}Step 1{col1}: How (where) should bahhh be installed? ║"))
    print(screen_center(f"{col1}╟────────────────────────────────────────────────╢"))
    print(screen_center(f"{col1}║ {col2}[1] {col1}Server install (/srv/bahhh/*) {col2}(req. root!) {col1}║"))
    print(screen_center(f"{col1}║ {col2}[2] {col1}User install (~/bahhh/*)                   ║"))
    print(screen_center(f"{col1}║ {col2}[3] {col1}Custom directory! {col2}(may require root!)      {col1}║"))
    print(screen_center(f"{col1}╚════════════════════════════════════════════════╝"))
    install_type = prompt_int(default=1, min_val=1, max_val=3, offset=get_offset())


def entry():
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print(f"{col1}goodbye!{col2}")
        sys.exit(0)

entry()
# print("\x1b[38;2;00;100;200mJohn F Kennedy")
# print("\033[38;2;00;100;200mJohn F Kennedy")
# print("\x1b[2J\x1b[20;10H\x1b[48;2;50;50;50m\x1b[38;2;0;255;255m\x1B[1m\x1B[3mHELLO LMAO")
# input()