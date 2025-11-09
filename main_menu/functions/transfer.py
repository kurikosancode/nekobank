from utils.input import input_str, input_int
from utils.print import print_error, text_with_color, print_break, get_heading
from utils.receipt import check_if_print_receipt
from account_manager import BALANCE, ACCOUNT_NUMBER, add_to_history, account_exists, accounts, ACCOUNT_INFO
from constants import SUCCESS_COLOR, WIDTH, SUB_FILL, FILL_COLOR, HEADING_COLOR, ACCOUNT_LENGTH, RECEIPT_DELAY, RECEIPT_WIDTH
from errors import ACCOUNT_NOT_EXIST_ERROR


def transfer(account_info: list) -> None:
    money = 0
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
    print(get_heading("TRANSFER", HEADING_COLOR, WIDTH, " "))
    while True:
        to_account = input_str("Transfer account to account number: ", ACCOUNT_LENGTH)
        account_index = account_exists(to_account)
        if account_exists(to_account) == -1:
            print_error(ACCOUNT_NOT_EXIST_ERROR)
            continue

        money = input_int("Money Transfer: ")
        if money < 0:
            print_error("Money must be positive.")
            continue
        if money > account_info[BALANCE]:
            print_error(f"The input exceeds the current balance (₱{account_info[BALANCE]}).")
            continue

        break

    account_info[BALANCE] -= money
    accounts[account_index][ACCOUNT_INFO][BALANCE] += money
    check_if_print_receipt(account_info, amount=money, seconds_delay=RECEIPT_DELAY, receipt_width=RECEIPT_WIDTH)
    event = f"Successfully transferred ₱{money} from {account_info[ACCOUNT_NUMBER]} to {to_account}."
    add_to_history(account_info, event)
    print(text_with_color(f"\n{event}", color=SUCCESS_COLOR))
    print(text_with_color(f"New Balance: ₱{account_info[BALANCE]}", color=SUCCESS_COLOR))
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
