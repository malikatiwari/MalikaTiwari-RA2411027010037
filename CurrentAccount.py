from BankAccount import BankAccount
from Withdrawable import Withdrawable


class CurrentAccount(BankAccount, Withdrawable):
    def withdraw(self, amount):
        return super().withdraw(amount)
