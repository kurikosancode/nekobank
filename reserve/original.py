print("Welcome to Group no.1s Atm Machine please create 5 accounts ")

while True:
    Account_names = [input(f"Enter name for the accounts {i}: ") for i in range(5)]

    if all(name.isalpha() for name in Account_names):
        print(Account_names[0:5])
        print("Please proceed with your pin: ")
        break
    else:
        print("Try again")
        continue

while True: 
    Accountpins = [input(f"Enter the pin for the accounts {i}: ") for i in range(5)]

    if all(pin.isdigit() for pin in Accountpins):
        print(Accountpins[0:5])
        print("Shall we proceed to the last step: ")
        break
    else:
        print("Try again")
        continue

while True:
    Accountballance = [input(f"Enter the balance for the accounts {i}: ") for i in range(5)]

    if all(ballance.isdigit() for ballance in Accountballance):
        print(Accountballance[0:5])
        break
    else:
        print("Try again Start back on account names")
        continue

print("\n=== GROUP NO.1 ATM MACHINE ===")
print("1. Create Account")
print("2. Deposit")
print("3. Withdraw")
print("4. Transfer")
print("5. Check Balance")
print("6. Change pin")
print("7. Exit")

options = input("Choose from the given options: ")

match options:
    case "1":
        print("Proceeding please wait patiently....")
    case "2":
        print("Depositing... please wait.")
    case "3":
        print("Withdrawing... please wait.")
    case "4":
        print("Proceeding to transfer... please wait.")
    case "5":
        print("Checking balance...")
    case "6":
        print("Changing pin....")
    case "7":
        print("Exiting program. Thank you!")
    case _:
        print("Unknown command")


def deposit_slot(Account_names, Accountbalance):
    print("\n=== DEPOSIT SLOT ===")
    name = input("Enter your account name (or type 'exit' to cancel): ")

    if name.lower() == "exit":
        print("Exiting deposit... returning to main menu.")
        return

    if name not in Account_names:
        print("Account not found. Please try again.")
        return

    index = Account_names.index(name)

    amount = input("Enter amount to deposit: ")

    if not amount.isdigit():
        print("Invalid input. Please enter numbers only.")
        return

    amount = int(amount)
    new_balance = int(Accountbalance[index]) + amount
    Accountbalance[index] = str(new_balance)

    print(f"Deposit successful! New balance for {name}: ₱{new_balance}")


def bank_transfer():
    print("\n=== BANK TRANSFER ===")
    while True:
        sender = input("Enter the account you want to transfer from: ")
        if sender not in Account_names:
            print("Invalid account. Please try again.")
        else:
            break

    while True:
        receiver = input("Enter the account you want to transfer to: ")
        if receiver not in Account_names:
            print("Invalid account. Please try again.")
        else:
            break

    while True:
        amount = input("Enter the amount you want to transfer: ")
        if not amount.isdigit():
            print("Invalid amount. Please try again.")
        else:
            break

    amount = int(amount)

    sender_index = Account_names.index(sender)
    receiver_index = Account_names.index(receiver)

    sender_balance = int(Accountballance[sender_index])
    receiver_balance = int(Accountballance[receiver_index])

    if sender_balance < amount:
        print("Insufficient funds. Please try again.")
        return

    Accountballance[sender_index] = str(sender_balance - amount)
    Accountballance[receiver_index] = str(receiver_balance + amount)

    print("Transfer complete.")
    print(f"New balance for {sender}: {float(Accountballance[Account_names.index(sender)])}")
    print(f"New balance for {receiver}: {float(Accountballance[Account_names.index(receiver)])}")


bank_transfer()

account = {"5665": "dan", "54665": "jc", "546546": "kurt", "345453": "josh", "3453": "martin"}
while True:
    print("\n--- CHECK ACCOUNT ---")
    print("Soft Keys: [CLEAR] [DELETE] [EXIT]")
    acc_pin = input("Enter Account PIN  : ")

    if acc_pin.upper() == "EXIT":
        print("Returning to main menu...")
        break
    elif acc_pin.upper() == "CLEAR":
        print("Input cleared.")
        continue
    elif acc_pin.upper() == "DELETE":
        print("Last character deleted.")
        continue

    if acc_pin in account:
        print(f"Account found: {account[acc_pin]}")
        print("Proceeding to next step...")

        break
    else:
        print("Account not found. Try again or type EXIT to return to main menu.")

# Balance Inquiry and Change PIN (MARTIN AND RAPHA)
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

accounts = {
    "Martin": {"pin": "1234", "balance": 5000},
    "Rapha": {"pin": "5678", "balance": 3000}
}


def login():
    acc_name = input("\nEnter account name: ")
    if acc_name not in accounts:
        print(RED + "Account not found!" + RESET)
        return None

    pin = input("Enter PIN: ")
    if not pin.isdigit():
        print(RED + "Invalid use of character!" + RESET)
        return None

    if pin != accounts[acc_name]["pin"]:
        print(RED + "PIN doesn’t match!" + RESET)
        return None

    return acc_name


def balance_inquiry():
    acc_name = login()
    if acc_name:
        print(GREEN + f"\nYour balance is: ₱{accounts[acc_name]['balance']}" + RESET)
    back_to_menu()


def change_pin():
    acc_name = login()
    if acc_name:
        new_pin = input("Enter new PIN: ")
        if not new_pin.isdigit():
            print(RED + "Invalid use of character! Please try again." + RESET)
            back_to_menu()
            return
        confirm_pin = input("Re-enter new PIN: ")
        if new_pin != confirm_pin:
            print(RED + "PINs do not match! Try again." + RESET)
            back_to_menu()
            return
        accounts[acc_name]["pin"] = new_pin
        print(GREEN + "PIN successfully changed!" + RESET)
    back_to_menu()


def back_to_menu():
    input("\nPress Enter to return to menu...")


def main_menu():
    while True:
        print("\n=== \033[1mMAIN MENU\033[0m ===" + RESET)
        print("1. Balance Inquiry")
        print("2. Change PIN")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            balance_inquiry()
        elif choice == "2":
            change_pin()
        elif choice == "3":
            print(GREEN + "Thank you, have a nice day!" + RESET)
            break
        else:
            print(RED + "Invalid choice! Try again." + RESET)


main_menu()