class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account: {self.account_number}, Holder: {self.holder_name}, Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name, balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, holder_name, balance)
            print("Account created successfully.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

bank = Bank()
while True:
    print("\nBank Menu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Balance")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        acc_num = input("Enter account number: ")
        name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.create_account(acc_num, name, initial_balance)
    elif choice == 2:
        acc_num = input("Enter account number: ")
        account = bank.get_account(acc_num)
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print("Account not found.")
    elif choice == 3:
        acc_num = input("Enter account number: ")
        account = bank.get_account(acc_num)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("Account not found.")
    elif choice == 4:
        acc_num = input("Enter account number: ")
        account = bank.get_account(acc_num)
        if account:
            account.display_balance()
        else:
            print("Account not found.")
    elif choice == 5:
        break
    else:
        print("Invalid choice, please try again.")
