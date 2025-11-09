from math import ceil


def text_with_color(string: str, color: str = "reset") -> str:
    color_dict = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "dark_green": "\033[38;5;34m",
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


def get_heading(text: str, color: str, width: int, fill: str = " ") -> str:
    n = len(text)
    colored_text = text_with_color(text, color)
    fill_width = width - n
    left_width = fill_width // 2
    right_width = ceil(fill_width / 2)
    heading = f"{left_width * fill}{colored_text}{right_width * fill}"
    return heading


def print_heading(text: str, color: str, width: int, fill: str = " ") -> None:
    heading = get_heading(text, color, width, fill)
    print(f"\n{heading}\n")


def print_error(error: str, error_color: str = "red") -> None:
    print(text_with_color(error, error_color) + "\n")


def print_break(width: int, fill: str, color: str = "reset") -> None:
    print("\n" + text_with_color(fill * width, color))