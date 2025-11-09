from receipt_printer import print_receipt
from .print import print_error
from .input import input_int
from errors import INVALID_OPTION_ERROR


def check_if_print_receipt(account_info: list, amount: int, seconds_delay: float, receipt_width: int) -> None:
    while True:
        code = input_int("Print receipt? (1 = Yes, 0 = No): ")
        if code == 0:
            break
        elif code == 1:
            print()
            print_receipt(account_info, amount, seconds_delay, receipt_width)
            break

        print_error(INVALID_OPTION_ERROR)

