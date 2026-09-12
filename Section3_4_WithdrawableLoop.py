from CurrentAccount import CurrentAccount
from SavingsAccount import SavingsAccount


# Only accounts that can honestly support withdrawal are included here.
withdrawable_accounts = [
    SavingsAccount(2001, "Savings User", 21, 10000, "Savings"),
    CurrentAccount(2002, "Current User", 21, 10000, "Current"),
]

for account in withdrawable_accounts:
    print(f"Withdrawing from account #{account.get_account_number()}")
    account.withdraw(1000)
    print(f"Balance: Rs. {account.get_balance()}")
