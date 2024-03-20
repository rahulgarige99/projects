class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.balance)

    def modify_account(self, new_account_number, new_customer_name):
        self.account_number = new_account_number
        self.customer_name = new_customer_name


def main():
    # Create two initial accounts
    accounts = []
    accounts.append(BankAccount("123", "rahul"))
    accounts.append(BankAccount("456", "rohith"))

    while True:
        print(" ")
        print("--------------------Welcome To Bank Management System--------------------")
        print(" ")
        print("1. Open New Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Check Balance")
        print("5. Close Account")
        print("6. Modify Account Details")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            customer_name = input("Enter customer name: ")
            accounts.append(BankAccount(account_number, customer_name))
            print("Account created successfully!")

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))

            for account in accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    print("Amount deposited successfully!")
                    break
            else:
                print("Account not found.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))

            for account in accounts:
                if account.account_number == account_number:
                    account.withdraw(amount)
                    print("Amount withdrawn successfully!")
                    break
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")

            for account in accounts:
                if account.account_number == account_number:
                    account.display_balance()
                    break
            else:
                print("Account not found.")

        elif choice == "5":
            account_number = input("Enter account number: ")

            for account in accounts:
                if account.account_number == account_number:
                    accounts.remove(account)
                    print("Account closed successfully!")
                    break
            else:
                print("Account not found.")

        elif choice == "6":
            account_number = input("Enter account number: ")

            for account in accounts:
                if account.account_number == account_number:
                    new_account_number = input("Enter new account number: ")
                    new_customer_name = input("Enter new customer name: ")
                    account.modify_account(new_account_number, new_customer_name)
                    print("Account details modified successfully!")
                    break
            else:
                print("Account not found.")

        elif choice == "0":
            print("---------------------Thank You" ,"Visit Again----------------------------")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

