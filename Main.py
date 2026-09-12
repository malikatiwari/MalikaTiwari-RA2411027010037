from BankAccount import BankAccount
from AccountRepository import AccountRepository
from NotificationService import NotificationService
from StatementGenerator import StatementGenerator
from SavingsInterestPolicy import SavingsInterestPolicy
from CurrentInterestPolicy import CurrentInterestPolicy


def main():
    account = BankAccount(101, "Ravi", 20, 2000, "Savings")

    account.deposit(1000)
    account.withdraw(500)
    account.deposit(250)

    repository = AccountRepository()
    notification_service = NotificationService()
    statement_generator = StatementGenerator()

    repository.save(account)
    notification_service.send("Account transactions completed successfully.")

    print(statement_generator.generate(account))

    savings_policy = SavingsInterestPolicy()
    current_policy = CurrentInterestPolicy()

    print(f"Savings interest: Rs. {savings_policy.calculate(account.get_balance())}")
    print(f"Current interest: Rs. {current_policy.calculate(account.get_balance())}")


if __name__ == "__main__":
    main()
