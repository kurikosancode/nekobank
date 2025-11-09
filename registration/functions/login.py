from constants import SUB_FILL, WIDTH, HEADING_COLOR, \
     SUCCESS_COLOR, FILL_COLOR, ACCOUNT_LENGTH, PIN_LENGTH
from utils.print import text_with_color, get_heading, print_error, print_break
from utils.input import input_str
from errors import ACCOUNT_NOT_EXIST_ERROR, PIN_NUMBER_MISMATCH_ERROR
from account_manager import account_exists, accounts, ACCOUNT_PIN


def login() -> int:
    """returns the index of the account."""
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
    print(get_heading("LOGIN", HEADING_COLOR, WIDTH, " "))
    while True:
        account_input = input_str("Account Number: ", target_length=ACCOUNT_LENGTH)
        account_index = account_exists(account_input)
        if account_index == -1:
            print_error(ACCOUNT_NOT_EXIST_ERROR)
            continue

        pin_number = input_str("Account PIN: ", target_length=PIN_LENGTH)
        if pin_number != accounts[account_index][ACCOUNT_PIN]:
            print_error(PIN_NUMBER_MISMATCH_ERROR)
            continue

        print(text_with_color(f"\nSuccessfully logged in to account {account_input}.", color=SUCCESS_COLOR))
        print_break(WIDTH, SUB_FILL, FILL_COLOR)
        return account_index

