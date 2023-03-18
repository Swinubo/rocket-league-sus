class Bank:
    interest_rate = 0.03  # class variable


    def __init__(self):
        self.accounts = {}  # dictionary to store the bank account


    def create_account(self, name, account_number, initial_deposit=0):
        self.accounts[account_number] = BankAccount(name, account_number, initial_deposit)
        print("Account created successfully for ", name, "\n")


    def check_balance(self, account_number):
        if account_number in self.accounts:
            self.accounts[account_number].check_balance()
        else:
            print("Invalid account number. \n")


    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Invalid account number. \n")


    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Invalid account number. \n")


    def calculate_interest(self):
        for account in self.accounts.values():
            interest = account.balance * Bank.interest_rate
            account.deposit(interest)
            print("Interest added to account:", account.number, "\n")

    def transfer(self, AccountReceiver, AccountGiver, Amount):
        if AccountReceiver in self.accounts:
            if AccountGiver in self.accounts:
                self.accounts[AccountReceiver].deposit(Amount)
                self.accounts[AccountGiver].withdraw(Amount)
                self.accounts[AccountReceiver].check_balance()
                self.accounts[AccountGiver].check_balance()
                print("Transfer succesful.")
        else:
            print("Invalid account number")

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.holder = account_holder
        self.number = account_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful. Current balance:", self.balance, "\n")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrawal successful. Current balance:", self.balance, "\n")


    def check_balance(self):
        print("Account holder:", self.holder)
        print("Account number:", self.number)
        print("Current balance:", self.balance, "\n")

bank = Bank()
bank.create_account("Alice Smith", "123456789", 10000000)
bank.create_account("Bob Johnson", "987654321", 10000)


bank.transfer('123456789', '987654321', 1200)
