# Section 1 — SRP Wrap-up

I ended up with 4 classes: `BankAccount`, `AccountRepository`, `NotificationService`, and `StatementGenerator`.
`BankAccount` now focuses on account operations, while database persistence, notifications, and statement formatting have separate responsibilities.
This is easier to test because each class can be tested independently without involving unrelated database, email, or formatting behavior.
A change to one responsibility is therefore less likely to break another responsibility.