from BankAccount import BankAccount


class FixedDepositAccount(BankAccount):
    def withdraw(self, amount, entered_pin=None):
        raise NotImplementedError("UnsupportedOperationException: Fixed deposits cannot be withdrawn early")
