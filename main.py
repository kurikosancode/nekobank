from constants import MAIN_FILL, SUB_FILL, WIDTH, BANK_NAME, END_MESSAGE, HEADING_COLOR, \
     SUCCESS_COLOR, FILL_COLOR, CAT_PAD, CAT_DELAY
from utils.print import text_with_color, get_heading
from utils.cat import print_cat
from registration.registration import registration
from main_menu import main_menu

TITLE = get_heading(BANK_NAME, HEADING_COLOR, WIDTH, SUB_FILL)


def print_title(title: str) -> None:
    print(text_with_color(MAIN_FILL * WIDTH, FILL_COLOR))
    print(title)
    print(text_with_color(MAIN_FILL * WIDTH, FILL_COLOR))


def main() -> None:
    print_title(TITLE)
    running = True
    while running:
        user_index = registration()
        if user_index == -1:
            break

        main_menu(user_index)

    print_cat(CAT_PAD, CAT_DELAY)
    print(f"\n{get_heading(END_MESSAGE, SUCCESS_COLOR, WIDTH, ' ')}\n")


if __name__ == '__main__':
    main()