
from utils.input import input_str
from account_manager import accounts, ACCOUNT_PIN, ACCOUNT_NUMBER, add_to_history, ACCOUNT_INFO
from utils.print import print_break, get_heading, print_error, text_with_color
from constants import WIDTH, SUB_FILL, FILL_COLOR, PIN_LENGTH, HEADING_COLOR, SUCCESS_COLOR


def change_pin(account_index: int) -> None:
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
    print(get_heading("CHANGE PIN", HEADING_COLOR, WIDTH, " "))
    while True:
        current_pin = input_str("Current Account PIN: ", target_length=PIN_LENGTH)
        if current_pin != accounts[account_index][ACCOUNT_PIN]:
            print_error("Account PIN doesn't match the current PIN.")
            continue

        while True:
            new_pin = input_str("Enter new PIN: ", target_length=PIN_LENGTH)
            confirmed_pin = input_str("Re-enter new PIN to confirm: ", target_length=PIN_LENGTH)

            if new_pin == confirmed_pin:
                break

            print_error("PINs do not match. Please try again.")

        accounts[account_index][ACCOUNT_PIN] = new_pin
        event = f"Successfully changed pin number of account {accounts[account_index][ACCOUNT_NUMBER]} to " \
                f"{new_pin}."
        add_to_history(accounts[account_index][ACCOUNT_INFO], event)

        print(text_with_color(f"\n{event}", color=SUCCESS_COLOR))
        print_break(WIDTH, SUB_FILL, FILL_COLOR)

        break
