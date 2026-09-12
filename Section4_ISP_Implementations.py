from Depositable import Depositable
from Withdrawable import Withdrawable
from Transferable import Transferable
from StatementProvider import StatementProvider
from BankAccount import BankAccount


class ATM(Depositable, Withdrawable):
    def deposit(self, amount):
        print(f"ATM deposit: {amount}")

    def withdraw(self, amount):
        print(f"ATM withdrawal: {amount}")


class SavingsAccountISP(BankAccount, Depositable, Withdrawable, Transferable, StatementProvider):
    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount):
        return super().withdraw(amount)

    def transfer(self, amount):
        print(f"Savings transfer: {amount}")

    def print_statement(self):
        print("Savings account statement")


# ISP confirmation: ATM has only deposit/withdraw capabilities, while SavingsAccount
# supports deposit, withdraw, transfer, and statement capabilities.
