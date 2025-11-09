from utils.print import print_break, get_heading
from account_manager import ACCOUNT_HISTORY, ACCOUNT_NAME, ACCOUNT_AGE, ACCOUNT_ADDRESS, ACCOUNT_NUMBER, BALANCE
from constants import WIDTH, SUB_FILL, FILL_COLOR, HEADING_COLOR


def check_account(account_info: list) -> None:
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
    print(get_heading("ACCOUNT", HEADING_COLOR, WIDTH, " "))
    print(f"ACCOUNT NUMBER: {account_info[ACCOUNT_NUMBER]}")
    print(f"NAME: {account_info[ACCOUNT_NAME]}")
    print(f"AGE: {account_info[ACCOUNT_AGE]}")
    print(f"ADDRESS: {account_info[ACCOUNT_ADDRESS]}")
    print(f"BALANCE: ₱{account_info[BALANCE]}")
    print_break(WIDTH, SUB_FILL, FILL_COLOR)

