from time import sleep
from constants import SUB_FILL, MAIN_FILL, FILL_COLOR, BANK_NAME, BANK_BRANCH, WIDTH
from account_manager import ACCOUNT_NUMBER, ACCOUNT_NAME, ACCOUNT_ADDRESS
from utils.print import text_with_color
from utils.clock import get_time, get_date

HOUR = 12

TITLE_COLOR = "orange"
LEFT_COLOR = "orange"
RIGHT_COLOR = "reset"

PAD = " "

MESSAGE = "THANK YOU FOR BANKING WITH US"


def print_line(line: str, second_delay: float) -> None:
    for c in line:
        print(c, flush=True, end="")
        sleep(second_delay)
    print("")


def get_line(left: str, right: str, width: int, left_color: str = "reset", right_color: str = "reset") -> str:
    left_length, right_length = len(left), len(right)
    left_colored = text_with_color(left, color=left_color)
    right_colored = text_with_color(right, color=right_color)
    return f"{left_colored}{' ' * (width - (left_length + right_length))}{right_colored}"


def print_lines(receipt_lines: list[str], delay: float) -> None:
    for line in receipt_lines:
        print_line(line, delay)


def print_receipt(account_info: list, amount: int, seconds_delay: float, receipt_width: int) -> None:
    account_number = account_info[ACCOUNT_NUMBER]
    name = account_info[ACCOUNT_NAME]
    address = account_info[ACCOUNT_ADDRESS]
    amount = f"₱{amount}"
    date = get_date()
    time = get_time()
    pad = (WIDTH // 2) - (receipt_width // 2)
    padding = PAD * pad

    lines = [
        padding + text_with_color(MAIN_FILL * receipt_width, color=FILL_COLOR),
        padding + text_with_color(BANK_NAME.center(receipt_width, SUB_FILL), color=TITLE_COLOR),
        padding + text_with_color(BANK_BRANCH.center(receipt_width, SUB_FILL), color=TITLE_COLOR),
        padding + text_with_color(MAIN_FILL * receipt_width, color=FILL_COLOR),

        padding + get_line("ACCOUNT NO:", account_number, receipt_width, LEFT_COLOR, RIGHT_COLOR),
        padding + text_with_color(SUB_FILL * receipt_width, color=FILL_COLOR),

        padding + get_line("NAME:", name, receipt_width, LEFT_COLOR, RIGHT_COLOR),
        padding + get_line("AMOUNT:", amount, receipt_width, LEFT_COLOR, RIGHT_COLOR),
        padding + get_line("DATE:", date, receipt_width, LEFT_COLOR, RIGHT_COLOR),
        padding + get_line("TIME:", time, receipt_width, LEFT_COLOR, RIGHT_COLOR),
        padding + get_line("ADDRESS:", address, receipt_width, LEFT_COLOR, RIGHT_COLOR),

        padding + text_with_color(MAIN_FILL * receipt_width, color=FILL_COLOR),
        padding + text_with_color(MESSAGE.center(receipt_width), color=TITLE_COLOR),
        padding + text_with_color(MAIN_FILL * receipt_width, color=FILL_COLOR),
    ]

    print_lines(lines, seconds_delay)


