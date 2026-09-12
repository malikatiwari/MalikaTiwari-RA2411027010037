from AccountRepository import AccountRepository


class FileAccountRepository(AccountRepository):
    def __init__(self, file_name="accounts.txt"):
        self.file_name = file_name

    def save(self, account):
        with open(self.file_name, "a", encoding="utf-8") as file:
            file.write(
                f"{account.get_account_number()},{account.get_name()},{account.get_balance()}\n"
            )

    def read_all(self):
        accounts = []
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                for line in file:
                    account_number, name, balance = line.strip().split(",", 2)
                    accounts.append({
                        "accountNumber": account_number,
                        "name": name,
                        "balance": float(balance),
                    })
        except FileNotFoundError:
            pass
        return accounts
