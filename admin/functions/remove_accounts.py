from utils.print import print_break, get_heading, print_error, text_with_color
from utils.input import input_str
from constants import WIDTH, SUB_FILL, FILL_COLOR, HEADING_COLOR, ACCOUNT_LENGTH, SUCCESS_COLOR
from .check_accounts import _check_accounts
from account_manager import account_exists, accounts
from errors import ACCOUNT_NOT_EXIST_ERROR


def remove_accounts() -> None:
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
    print(get_heading("REMOVE ACCOUNTS", HEADING_COLOR, WIDTH, " "))
    _check_accounts()
    print()
    while True:
        account_input = input_str("Account Number: ", target_length=ACCOUNT_LENGTH)
        account_index = account_exists(account_input)
        if account_index == -1:
            print_error(ACCOUNT_NOT_EXIST_ERROR)
            continue

        accounts.pop(account_index)
        print(text_with_color(f"\nSuccessfully removed account {account_input}.", color=SUCCESS_COLOR))
        break

    print_break(WIDTH, SUB_FILL, FILL_COLOR)

