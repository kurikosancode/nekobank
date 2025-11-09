
from constants import MAIN_FILL, SUB_FILL, WIDTH, HEADING_COLOR, SUCCESS_COLOR, FILL_COLOR
from utils.print import get_heading, print_break, text_with_color
from utils.input import get_option
from account_manager import accounts, ACCOUNT_INFO, ACCOUNT_NUMBER
from .functions import deposit, withdraw, transfer, transaction_history, check_account, change_pin

MINIMUM, MAXIMUM = 1, 7
TITLE = get_heading("MAIN MENU", HEADING_COLOR, WIDTH, SUB_FILL)


def print_title(title: str) -> None:
    print(MAIN_FILL * WIDTH)
    print(title)
    print(MAIN_FILL * WIDTH)


def print_options() -> None:
    print(get_heading("MAIN MENU", HEADING_COLOR, WIDTH, " "))
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4 Transaction History")
    print("5. Check Account")
    print("6. Change Pin")
    print("7. Log Out")
    print()


def main_menu(user_index: int) -> None:
    account = accounts[user_index]
    account_number = account[ACCOUNT_NUMBER]
    account_info = account[ACCOUNT_INFO]
    while True:
        print_options()
        option = get_option(MINIMUM, MAXIMUM)
        if option == 1:
            deposit(account_info)
        elif option == 2:
            withdraw(account_info)
        elif option == 3:
            transfer(account_info)
        elif option == 4:
            transaction_history(account_info)
        elif option == 5:
            check_account(account_info)
        elif option == 6:
            change_pin(user_index)
        elif option == 7:
            print(text_with_color(f"\nYou have successfully logged out of account {account_number}.",
                                  color=SUCCESS_COLOR))
            print_break(WIDTH, SUB_FILL, FILL_COLOR)
            return

