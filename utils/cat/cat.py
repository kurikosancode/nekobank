from pathlib import Path
from time import sleep

path = "cat_1.txt"
CAT_PATH = Path(__file__).parent / path
CAT_WIDTH = 30

with CAT_PATH.open("r", encoding="utf-8") as f:
    lines = f.readlines()


def print_cat(pad: int, delay: float) -> None:
    print()
    for line in lines:
        line = line.rstrip()
        print(" " * pad, end="")
        for c in line:
            print(c, flush=True, end="")
            sleep(delay)
        print()