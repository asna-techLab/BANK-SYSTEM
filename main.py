from database import (
    get_customer,
    get_account,
    get_account_by_id,
    update_balance,
    transfer_money,
    change_password
)

from customer import Customer
from account import BankAccount


def login():

    print("\n==============================")
    print("       BANK SYSTEM LOGIN")
    print("==============================")

    name = input("Enter your name: ")
    password = input("Enter your password: ")

    customer_data = get_customer(name, password)

    if customer_data is None:
        print("\nInvalid name or password.")
        return None, None

    print("\nLogin successful!")
    print("Welcome,", customer_data[1])

    # Create Customer object
    customer = Customer(
        customer_data[0],
        customer_data[1],
        customer_data[2]
    )

    # Get customer's account
    account_data = get_account(customer.customer_id)

    if account_data is None:
        print("No bank account found.")
        return None, None

    # Create BankAccount object
    account = BankAccount(
        account_data[0],
        account_data[1],
        account_data[2],
        account_data[3]
    )

    return customer, account


def bank_menu(customer, account):

    while True:

        print("\n================================")
        print("          BANK SYSTEM")
        print("================================")

        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Account Type")
        print("6. Customer Details")
        print("7. Compare Accounts")
        print("8. Change Password")
        print("9. Exit")

        print("================================")

        choice = input("Enter your choice: ")

        # --------------------------------
        # 1. CHECK BALANCE
        # --------------------------------

        if choice == "1":

            account.check_balance()


        # --------------------------------
        # 2. DEPOSIT
        # --------------------------------

        elif choice == "2":

            try:

                amount = float(
                    input("Enter amount to deposit: ")
                )

                success = account.deposit(amount)

                if success:
                    update_balance(
                        account.account_id,
                        account.balance
                    )

            except ValueError:

                print("Please enter a valid number.")


        # --------------------------------
        # 3. WITHDRAW
        # --------------------------------

        elif choice == "3":

            try:

                amount = float(
                    input("Enter amount to withdraw: ")
                )

                success = account.withdraw(amount)

                if success:
                    update_balance(
                        account.account_id,
                        account.balance
                    )

            except ValueError:

                print("Please enter a valid number.")


        # --------------------------------
        # 4. TRANSFER
        # --------------------------------

        elif choice == "4":

            try:

                receiver_id = int(
                    input("Enter receiver account ID: ")
                )

                amount = float(
                    input("Enter amount to transfer: ")
                )

                if amount <= 0:

                    print("Amount must be greater than 0.")

                    continue

                if amount > account.balance:

                    print("Insufficient balance.")

                    continue

                if receiver_id == account.account_id:

                    print(
                        "You cannot transfer money "
                        "to your own account."
                    )

                    continue

                # Check whether receiver exists
                receiver_data = get_account_by_id(
                    receiver_id
                )

                if receiver_data is None:

                    print("Receiver account not found.")

                    continue

                # Perform transfer
                transfer_money(
                    account.account_id,
                    receiver_id,
                    amount
                )

                # Update current object's balance
                account.balance -= amount

                print("\nTransfer successful!")

                print(
                    "Amount transferred:",
                    amount
                )

                print(
                    "Your new balance:",
                    account.balance
                )

            except ValueError:

                print("Please enter valid numbers.")


        # --------------------------------
        # 5. ACCOUNT TYPE
        # --------------------------------

        elif choice == "5":

            account.show_account_type()


        # --------------------------------
        # 6. CUSTOMER DETAILS
        # --------------------------------

        elif choice == "6":

            customer.print_details()

            print(
                "Account ID:",
                account.account_id
            )

            print(
                "Account Type:",
                account.account_type
            )


        # --------------------------------
        # 7. COMPARE ACCOUNTS
        # --------------------------------

        elif choice == "7":

            try:

                other_account_id = int(
                    input(
                        "Enter account ID to compare: "
                    )
                )

                other_data = get_account_by_id(
                    other_account_id
                )

                if other_data is None:

                    print("Account not found.")

                    continue

                other_account = BankAccount(
                    other_data[0],
                    other_data[1],
                    other_data[2],
                    other_data[3]
                )

                if account > other_account:

                    print(
                        "Your account has a larger balance."
                    )

                elif account < other_account:

                    print(
                        "Your account has a smaller balance."
                    )

                else:

                    print(
                        "Both accounts have equal balance."
                    )

            except ValueError:

                print("Please enter a valid account ID.")


        # --------------------------------
        # 8. CHANGE PASSWORD
        # --------------------------------

        elif choice == "8":

            new_password = input(
                "Enter your new password: "
            )

            if new_password == "":

                print("Password cannot be empty.")

            else:

                change_password(
                    customer.customer_id,
                    new_password
                )

                # Update object as well
                customer.password = new_password

                print(
                    "Password changed successfully!"
                )


        # --------------------------------
        # 9. EXIT
        # --------------------------------

        elif choice == "9":

            print("\nThank you for using Bank System!")

            break


        # --------------------------------
        # INVALID OPTION
        # --------------------------------

        else:

            print(
                "Invalid choice. "
                "Please select 1-9."
            )


# ==========================================
# PROGRAM STARTS HERE
# ==========================================

customer, account = login()

if customer is not None and account is not None:

    bank_menu(customer, account)

else:

    print("\nProgram ended.")
    
