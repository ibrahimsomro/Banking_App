"""
Main CLI for the banking_app mini project.

Run it with:
    python -m banking_app.main
"""
from typing import Optional
from banking_app import bankcore, accounts


def prompt_menu() -> str:
    print("\nWelcome to ABC Bank")
    print("Select an option:")
    print("1. Login to the account")
    print("2. Create an account")
    print("3. Exit")
    return input("Enter 1/2/3: ").strip()


def prompt_actions() -> str:
    print("\nSelect an action:")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Logout")
    return input("Enter 1/2/3/4: ").strip()


def do_login() -> Optional[str]:
    customer_id = input("Enter customer ID (e.g., 2057-1): ").strip()
    password = input("Enter password: ").strip()
    if bankcore.login(customer_id, password):
        print("Login successful.")
        return customer_id
    # bankcore.login already prints "Invalid login" on failure
    return None


def do_create_account() -> str:
    name = input("Enter your name: ").strip()
    password = input("Create a password: ").strip()
    # Auto-generate ID as per requirement <branch_id>-<user number>
    new_id = bankcore.generate_customer_id()
    try:
        bankcore.create_account(name=name, customer_id=new_id, password=password)
    except ValueError as e:
        print(f"Could not create account: {e}")
        return ""
    print(f"Account created successfully! Your customer ID is: {new_id}")
    # Initialize a zero balance for the new user (optional, accounts module will lazy-init too)
    accounts.check_balance(new_id)
    return new_id


def session_loop(customer_id: str) -> None:
    username = bankcore.get_user_name(customer_id) or customer_id
    print(f"\nWelcome, {username}! (Customer ID: {customer_id})")
    while True:
        choice = prompt_actions()
        if choice == "1":
            # Deposit
            try:
                amount = float(input("Enter deposit amount: "))
                new_bal = accounts.deposit(customer_id, amount)
                print(f"Deposit successful. New balance: {new_bal:.2f}")
            except ValueError as e:
                print(f"Deposit failed: {e}")
        elif choice == "2":
            # Withdraw
            try:
                amount = float(input("Enter withdrawal amount: "))
                new_bal = accounts.withdraw(customer_id, amount)
                print(f"Current balance: {new_bal:.2f}")
            except ValueError as e:
                print(f"Withdrawal failed: {e}")
        elif choice == "3":
            # Check balance
            bal = accounts.check_balance(customer_id)
            print(f"Your current balance is: {bal:.2f}")
        elif choice == "4":
            print("Logged out. Have a great day!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")


def main() -> None:
    while True:
        choice = prompt_menu()
        if choice == "1":
            cid = do_login()
            if cid:
                session_loop(cid)
        elif choice == "2":
            cid = do_create_account()
            if cid:
                session_loop(cid)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
