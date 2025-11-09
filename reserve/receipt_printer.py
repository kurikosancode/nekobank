from datetime import datetime
from time import sleep
from threading import Thread
from playsound import playsound

WIDTH = 40
HOUR = 12
SECOND_DELAY = 0.01

SEPARATOR_COLOR = "green"
TITLE_COLOR = "orange"
LEFT_COLOR = "orange"
RIGHT_COLOR = "reset"
MAIN_SEPARATOR = "="
SUB_SEPARATOR = "-"

PAD = " "
PAD_COUNT = 2
PADDING = PAD * PAD_COUNT


def text_with_color(string: str, color: str = "reset") -> str:
    color_dict = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "orange": "\033[38;5;208m",
        "reset": "\033[0m",
    }

    color_code = color_dict.get(color.lower(), color_dict["white"])
    reset_code = color_dict["reset"]

    return f"{color_code}{string}{reset_code}"


def get_date() -> str:
    date = datetime.now()
    return f"{date.day:02d}/{date.month:02d}/{date.year}"


def get_time() -> str:
    current_datetime = datetime.now()
    is_pm = current_datetime.hour >= 12
    formatted_hour = 12 if current_datetime.hour == 12 else current_datetime.hour % HOUR
    formatted_current_time = current_datetime.strftime(f"{formatted_hour}:%M:%S {'PM' if is_pm else 'AM'}")
    return formatted_current_time


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


def print_lines(receipt_lines: list[str], delay: float = SECOND_DELAY) -> None:
    for line in receipt_lines:
        print_line(line, delay)


def print_receipt() -> None:
    ...


bank_name = "NekoBank"
bank_branch = "Malolos City Branch"

card_number = "**** **** **** 8423"
account_number = "**** **** 9876"
name = "Kurt Arnoco"
location = "Malolos City"
date = get_date()
time = get_time()
amount = "₱ 1000"
message = "THANK YOU FOR BANKING WITH US"

lines = [
    PADDING + text_with_color(MAIN_SEPARATOR * WIDTH, color=SEPARATOR_COLOR),
    PADDING + text_with_color(bank_name.center(WIDTH, SUB_SEPARATOR), color=TITLE_COLOR),
    PADDING + text_with_color(bank_branch.center(WIDTH, SUB_SEPARATOR), color=TITLE_COLOR),
    PADDING + text_with_color(MAIN_SEPARATOR * WIDTH, color=SEPARATOR_COLOR),

    PADDING + get_line("ACCOUNT NO:", account_number, WIDTH, LEFT_COLOR, RIGHT_COLOR),
    PADDING + text_with_color(SUB_SEPARATOR * WIDTH, color=SEPARATOR_COLOR),

    PADDING + get_line("NAME:", name, WIDTH, LEFT_COLOR, RIGHT_COLOR),
    PADDING + get_line("AMOUNT:", amount, WIDTH, LEFT_COLOR, RIGHT_COLOR),
    PADDING + get_line("DATE:", date, WIDTH, LEFT_COLOR, RIGHT_COLOR),
    PADDING + get_line("TIME:", time, WIDTH, LEFT_COLOR, RIGHT_COLOR),
    PADDING + get_line("LOCATION:", location, WIDTH, LEFT_COLOR, RIGHT_COLOR),

    PADDING + text_with_color(MAIN_SEPARATOR * WIDTH, color=SEPARATOR_COLOR),
    PADDING + text_with_color(message.center(WIDTH), color=TITLE_COLOR),
    PADDING + text_with_color(MAIN_SEPARATOR * WIDTH, color=SEPARATOR_COLOR),
]


sound = "receipt.wav"

print()
# Thread(target=lambda: playsound(sound), daemon=True).start()
print_lines(lines, SECOND_DELAY)
