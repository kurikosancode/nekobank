from utils.print import print_break, get_heading
from constants import WIDTH, SUB_FILL, FILL_COLOR, HEADING_COLOR, MEMBERS


def credit() -> None:
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
    print(get_heading("MEMBERS", HEADING_COLOR, WIDTH, " "))
    for member in MEMBERS:
        print(member.center(WIDTH))
    print_break(WIDTH, SUB_FILL, FILL_COLOR)

