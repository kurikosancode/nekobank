from .print import print_error
from errors import DIGIT_INPUT_ERROR, INVALID_OPTION_ERROR


def input_int(input_message: str) -> int:
    while True:
        user_input = input(input_message)
        if user_input.isdigit():
            break

        print_error(DIGIT_INPUT_ERROR)

    return int(user_input)


def input_str(input_message: str, target_length: int, only_digits: bool = True) -> str:
    while True:
        user_input = input(input_message)
        if only_digits and not all(c.isdigit() for c in user_input):
            print_error("Only digits are allowed. ")
            continue

        if len(user_input) == target_length:
            break

        print_error(f"Input must be of length {target_length}.")

    return user_input


def get_option(minimum: int, maximum: int, message: str = "Please input a valid option: ") -> int:
    while True:
        code = input_int(input_message=message)
        if minimum <= code <= maximum:
            break

        print_error(INVALID_OPTION_ERROR)

    return code

