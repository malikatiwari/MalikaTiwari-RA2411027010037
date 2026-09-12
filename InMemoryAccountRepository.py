class InMemoryAccountRepository:
    def __init__(self):
        self.accounts = []

    def save(self, account):
        self.accounts.append(account)
        print("Saved account in memory")

    def read_all(self):
        return self.accounts
