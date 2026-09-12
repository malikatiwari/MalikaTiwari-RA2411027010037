class Account:
    """Common account abstraction that does not promise withdrawal."""

    def __init__(self, account_number, name, age, balance, account_type):
        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = balance
        self.account_type = account_type

    def get_account_number(self):
        return self.account_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_balance(self):
        return self.balance

    def get_account_type(self):
        return self.account_type
