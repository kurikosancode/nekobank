from constants import WIDTH, HEADING_COLOR, SUB_FILL, FILL_COLOR
from utils.print import get_heading
from utils.input import get_option
from .functions import register, login, credit
from admin import admin
from utils.print import print_break


MINIMUM, MAXIMUM = 1, 5


def print_options() -> None:
    print(get_heading("OPTIONS", HEADING_COLOR, WIDTH, " "))
    print("1. Register")
    print("2. Log in")
    print("3. Admin")
    print("4. Credits")
    print("5. Quit")
    print()


def registration() -> int:
    running = True
    while running:
        print_options()
        option = get_option(MINIMUM, MAXIMUM)
        if option == 1:
            return register()
        elif option == 2:
            return login()
        elif option == 3:
            print_break(WIDTH, SUB_FILL, FILL_COLOR)
            admin()
        elif option == 4:
            credit()
        elif option == 5:
            return -1

