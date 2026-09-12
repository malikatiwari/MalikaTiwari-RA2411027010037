from BankAccount import BankAccount
from FixedDepositAccount import FixedDepositAccount


class SavingsAccount(BankAccount):
    def withdraw(self, amount, entered_pin=None):
        return super().withdraw(amount, entered_pin)


# A List[Account] may contain accounts that cannot honestly support withdrawal.
accounts = [
    SavingsAccount(1001, "Savings User", 21, 10000, "Savings"),
    FixedDepositAccount(1002, "FD User", 21, 20000),
]

for account in accounts:
    print(f"Trying withdrawal for account #{account.get_account_number()}")
    try:
        account.withdraw(1000)
    except NotImplementedError as error:
        print(f"Crash observed: {error}")
