from BankAccount import BankAccount
from FixedDepositAccount import FixedDepositAccount


class SavingsAccount(BankAccount):
    def withdraw(self, amount, entered_pin=None):
        return super().withdraw(amount, entered_pin)


# Original LSP problem demonstrated in the previous commit:
# a FixedDepositAccount implementation that overrode withdraw() to throw
# UnsupportedOperationException caused the List[Account] withdrawal loop to crash.
# The final design removes that unsupported override entirely.
accounts = [
    SavingsAccount(1001, "Savings User", 21, 10000, "Savings"),
    FixedDepositAccount(1002, "FD User", 21, 20000),
]

for account in accounts:
    print(f"Trying withdrawal for account #{account.get_account_number()}")
    try:
        account.withdraw(1000)
    except AttributeError as error:
        print(f"Crash observed in the old List[Account] design: {error}")
