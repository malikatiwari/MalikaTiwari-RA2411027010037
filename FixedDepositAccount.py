from Account import Account


class FixedDepositAccount(Account):
    """Fixed deposits are accounts, but they do not promise withdrawal."""

    def __init__(self, account_number, name, age, balance):
        super().__init__(account_number, name, age, balance, "Fixed Deposit")
