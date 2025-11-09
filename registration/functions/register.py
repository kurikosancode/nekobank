
from utils.input import input_int, input_str
from constants import SUB_FILL, WIDTH, HEADING_COLOR, ACCOUNT_LENGTH, \
    PIN_LENGTH, INITIAL_BALANCE, MINIMUM_AGE, SUCCESS_COLOR, FILL_COLOR
from utils.print import text_with_color, get_heading, print_error, print_break
from errors import ACCOUNT_EXIST_ERROR, age_error
from account_manager import account_exists, accounts, add_to_history


def get_age() -> int:
    while True:
        age = input_int("Age: ")
        if age >= MINIMUM_AGE:
            break

        print_error(f"{age_error(MINIMUM_AGE)}")

    return age


def register() -> int:
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
    print(get_heading("REGISTER", HEADING_COLOR, WIDTH, " "))

    while True:
        account_number = input_str("Account Number: ", target_length=ACCOUNT_LENGTH)
        if account_exists(account_number) != -1:
            print_error(ACCOUNT_EXIST_ERROR)
            continue

        pin_number = input_str("Account PIN: ", target_length=PIN_LENGTH)

        print_break(WIDTH, SUB_FILL, FILL_COLOR)
        print(get_heading("ACCOUNT INFORMATION", HEADING_COLOR, WIDTH, " "))

        account_name = input("Name: ")
        account_age = get_age()
        account_address = input("Address: ")

        account_info = [account_number, account_name, account_age, account_address, INITIAL_BALANCE, []]
        new_account = [account_number, pin_number, account_info]
        accounts.append(new_account)

        event = f"Successfully registered account {account_number}."
        add_to_history(account_info, event)

        print(text_with_color(f"\n{event}", color=SUCCESS_COLOR))
        print_break(WIDTH, SUB_FILL, FILL_COLOR)

        n = len(accounts)
        return n - 1