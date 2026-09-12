# Section 2 — OCP Wrap-up

For the Salary Account requirement, I edited `Main.py` to use the new account and policy and added new files for `SalaryAccount`, `SalaryInterestPolicy`, `Bank`, and `SMSNotificationService`.
No existing interest policy class was changed; `SavingsInterestPolicy` and `CurrentInterestPolicy` remain untouched.
The design is open for adding new account types and interest policies without modifying existing policy classes.
