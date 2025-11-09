from utils.print import print_break, get_heading
from account_manager import accounts, ACCOUNT_INFO
from constants import WIDTH, SUB_FILL, FILL_COLOR, HEADING_COLOR


def _check_accounts() -> None:
    available_space = WIDTH - 4
    account_number_length = .20
    name_length = .25
    age_length = .10
    address_length = .30
    balance_length = .15

    header = f"{'ACCOUNT NUMBER'.center(int(account_number_length * available_space))} " \
               f"{'NAME'.center(int(name_length * available_space))} " \
               f"{'AGE'.center(int(age_length * available_space))} " \
               f"{'ADDRESS'.center(int(address_length * available_space))} " \
               f"{'BALANCE'.center(int(balance_length * available_space))}"

    print(header)
    for account_info in map(lambda account: account[ACCOUNT_INFO], accounts):
        account_number, name, age, address, balance, _ = account_info
        balance = f"₱{balance}"

        line = f"{account_number.center(int(account_number_length * available_space))}|" \
               f"{name.center(int(name_length * available_space))}|" \
               f"{str(age).center(int(age_length * available_space))}|" \
               f"{address.center(int(address_length * available_space))}|" \
               f"{balance.center(int(balance_length * available_space))}"

        print(line)


def check_accounts() -> None:
    print_break(WIDTH, SUB_FILL, FILL_COLOR)
    print(get_heading("CHECK ACCOUNTS", HEADING_COLOR, WIDTH, " "))
    _check_accounts()
    print_break(WIDTH, SUB_FILL, FILL_COLOR)

