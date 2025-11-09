from utils.clock import get_date, get_time
from constants import ACCOUNT_LENGTH, DEFAULT_PIN, INITIAL_BALANCE, MEMBERS


ACCOUNT_NUMBER, ACCOUNT_PIN, ACCOUNT_INFO = range(3)
ACCOUNT_NAME, ACCOUNT_AGE, ACCOUNT_ADDRESS, BALANCE, ACCOUNT_HISTORY = range(1, 6)

"""
# [[account_number, pin_number, is_admin, [account_number, account_name, account_age, account_address, balance, 
# account_history]]]
# account history -> [event, time, date]
"""

accounts = []


def add_to_history(account_info: list, event: str) -> None:
    time, date = get_time(), get_date()

    new_history = [event, time, date]
    account_info[ACCOUNT_HISTORY].append(new_history)


DEFAULT_AGE, DEFAULT_ADDRESS = 18, "Malolos, Bulacan"

for i, name in enumerate(MEMBERS, start=1):
    account_number = str(i).zfill(ACCOUNT_LENGTH)
    info = [account_number, name, DEFAULT_AGE, DEFAULT_ADDRESS, INITIAL_BALANCE, []]
    add_to_history(info, f"Successfully registered account {account_number}.")
    acc = [account_number, DEFAULT_PIN, info]
    accounts.append(acc)


def account_exists(identifier: str) -> int:
    n = len(accounts)
    for index in range(n):
        curr = accounts[index][ACCOUNT_NUMBER]
        if curr == identifier:
            return index

    return -1


def remove_account(identifier: str) -> None:
    n = len(accounts)
    for i in range(n):
        account = accounts[i]
        if account[ACCOUNT_NUMBER] == identifier:
            accounts.pop(i)
            break
