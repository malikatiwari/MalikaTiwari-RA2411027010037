class StatementGenerator:

    def generate(self, account):
        lines = [
            f"---- Statement for Account #{account.get_account_number()} ({account.get_name()}) ----"
        ]
        for entry in account.transaction_log:
            lines.append(entry)
        lines.append(f"Current Balance: Rs. {account.get_balance()}")
        lines.append("-----------------------------------------------------")
        return "\n".join(lines)
