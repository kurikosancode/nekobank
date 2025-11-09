
from constants import MAIN_FILL, SUB_FILL, WIDTH, HEADING_COLOR, SUCCESS_COLOR, FILL_COLOR
from utils.print import get_heading, print_break, text_with_color
from utils.input import get_option
from .functions import check_accounts, remove_accounts
MINIMUM, MAXIMUM = 1, 3
TITLE = get_heading("ADMIN", HEADING_COLOR, WIDTH, SUB_FILL)


# show account number, name, age, street, balance

def print_title(title: str) -> None:
    print(MAIN_FILL * WIDTH)
    print(title)
    print(MAIN_FILL * WIDTH)


def print_options() -> None:
    print(get_heading("ADMIN", HEADING_COLOR, WIDTH, " "))
    print("1. Check Accounts")
    print("2. Remove Accounts")
    print("3. Leave Admin")
    print()


def admin() -> None:
    while True:
        print_options()
        option = get_option(MINIMUM, MAXIMUM)
        if option == 1:
            check_accounts()
        elif option == 2:
            remove_accounts()
        elif option == 3:
            print(text_with_color(f"\nYou have successfully left admin.", color=SUCCESS_COLOR))
            print_break(WIDTH, SUB_FILL, FILL_COLOR)
            return

