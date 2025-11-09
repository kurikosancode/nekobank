from utils.print import print_break, get_heading
from account_manager import ACCOUNT_HISTORY
from constants import WIDTH, SUB_FILL, FILL_COLOR, HEADING_COLOR


def transaction_history(account_info: list) -> None:
    history = account_info[ACCOUNT_HISTORY]
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
    print(get_heading("TRANSACTION HISTORY", HEADING_COLOR, WIDTH, " "))
    for event, time, date in history:
        n = len(event)
        pad_left = 3
        right_width = 17
        left_width = WIDTH - (right_width * 2) - (2 + pad_left)
        line = f"{pad_left * ' '}{event}{' ' * (left_width - n)}|{time.center(right_width)}|{date.center(right_width)}"
        print(get_heading(line, "reset", WIDTH, " "))
    print_break(WIDTH, SUB_FILL, FILL_COLOR)

