from BankAccount import BankAccount
from Withdrawable import Withdrawable


class SavingsAccount(BankAccount, Withdrawable):
    def withdraw(self, amount):
        return super().withdraw(amount)
