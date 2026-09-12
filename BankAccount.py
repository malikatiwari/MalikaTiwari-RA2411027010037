class BankAccount:

    # Reasons this class can change:
    # 1. Account validation rules change (age or minimum-balance rules).
    # 2. Deposit/withdrawal business rules change.
    # 3. Transaction logging format or storage changes.
    # 4. Database technology or persistence details change.
    # 5. Email provider or notification message format changes.
    # 6. Account closing/reopening rules change.
    # 7. PIN management or verification rules change.
    # 8. Interest calculation rules change.
    # 9. Statement formatting or statement contents change.

    # Job description for the SRP version:
    # BankAccount is responsible only for account operations such as deposit,
    # withdrawal, and reporting the current account information.

    def __init__(self, account_number, name, age, balance, account_type):
        if age < 18:
            print("Age was below 18, correcting to 18")
            age = 18
        minimum_balance = 500.0 if account_type == "Savings" else 1000.0
        if balance < minimum_balance:
            print(f"Initial balance below minimum, correcting to {minimum_balance}")
            balance = minimum_balance
        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = balance
        self.account_type = account_type
        self.status = "Active"
        self.pin = None
        self.transaction_log = []

    def deposit(self, amount):
        if self.status != "Active":
            print("Account is not active")
            return False
        if amount <= 0:
            print("Invalid deposit amount")
            return False
        self.balance += amount
        self.transaction_log.append(f"DEPOSIT: Rs. {amount} | New balance: {self.balance}")
        return True

    def withdraw(self, amount, entered_pin=None):
        if self.status != "Active":
            print("Account is not active")
            return False
        if self.pin is not None and (entered_pin is None or entered_pin != self.pin):
            print("Incorrect PIN")
            return False
        if amount <= 0:
            print("Invalid withdrawal amount")
            return False
        minimum_balance = 500.0 if self.account_type == "Savings" else 1000.0
        if self.balance - amount < minimum_balance:
            print("Withdrawal would breach minimum balance")
            return False
        self.balance -= amount
        self.transaction_log.append(f"WITHDRAW: Rs. {amount} | New balance: {self.balance}")
        return True

    def get_account_number(self):
        return self.account_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def get_account_type(self):
        return self.account_type

    def has_pin(self):
        return self.pin is not None
