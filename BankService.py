from abc import ABC, abstractmethod


class BankService(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, amount):
        pass

    @abstractmethod
    def print_statement(self):
        pass

    @abstractmethod
    def apply_for_loan(self):
        pass


# Warm-up: ATM is forced to implement methods it does not really need.
class ATM(BankService):
    def deposit(self, amount):
        print(f"ATM deposit: {amount}")

    def withdraw(self, amount):
        print(f"ATM withdrawal: {amount}")

    # Forced by the fat interface, but ATM does not need transfer here.
    def transfer(self, amount):
        pass

    # Forced by the fat interface, but ATM does not need statement printing.
    def print_statement(self):
        pass

    # Forced by the fat interface, but ATM does not handle loans.
    def apply_for_loan(self):
        pass
