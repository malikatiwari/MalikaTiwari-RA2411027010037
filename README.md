# GreenLeaf Bank — SOLID Principles Lab

This repository contains the four-part GreenLeaf Bank refactoring lab implemented in **Python**. The project progressively refactors an initially overloaded banking design using the five SOLID principles: **SRP, OCP, LSP, ISP, and DIP**.

## Project Overview

The goal is to make the banking system easier to maintain, extend, test, and change without repeatedly modifying existing classes.

## Lab 1 — Original Design

The starting design used a large `BankAccount` class with multiple responsibilities. This provided the baseline for the later refactoring work.

Typical responsibilities included:
- Account operations
- Persistence/database handling
- Notifications
- Statement generation
- Other account-related rules

## Section 1 — SRP: Single Responsibility Principle

**Problem:** `BankAccount` was doing too many unrelated jobs.

### Refactoring
- `BankAccount` focuses on account operations such as deposit and withdrawal.
- `AccountRepository` handles persistence.
- `NotificationService` handles notifications.
- `StatementGenerator` handles statement formatting/generation.
- `Main.py` demonstrates collaboration between these classes.

### Key idea
A class should have **one reason to change**. Separating responsibilities makes individual components easier to understand, maintain, and test.

### Main files
- `BankAccount.py`
- `AccountRepository.py`
- `NotificationService.py`
- `StatementGenerator.py`
- `Main.py`
- `Section1_SRP_WrapUp.md`

## Section 2 — OCP: Open/Closed Principle

**Problem:** Adding every new account type would require modifying an `if/else` chain inside the interest calculator.

### Refactoring
An `InterestPolicy` abstraction was introduced so each account type can have its own interest policy.

Current policies:
- `SavingsInterestPolicy` — 4%
- `CurrentInterestPolicy` — 1%
- `SalaryInterestPolicy` — 5%

A new account type can therefore receive a new policy without changing the existing policy classes.

### Additional refactoring
- `SalaryAccount` extends the existing account abstraction.
- `Bank` receives a `NotificationService` through its constructor.
- `SMSNotificationService` demonstrates swapping the notification implementation without changing `Bank`.

### Main files
- `InterestCalculator.py`
- `InterestPolicy.py`
- `SavingsInterestPolicy.py`
- `CurrentInterestPolicy.py`
- `SalaryAccount.py`
- `SalaryInterestPolicy.py`
- `Bank.py`
- `SMSNotificationService.py`
- `Section2_OCP_WrapUp.md`

### Key idea
Software entities should be **open for extension but closed for modification**.

## Section 3 — LSP: Liskov Substitution Principle

**Problem:** A `FixedDepositAccount` cannot honestly support withdrawal, so treating it as an ordinary withdrawable account causes a runtime failure.

### Warm-up
The classic Rectangle/Square example demonstrates that a Square cannot safely substitute for a Rectangle when calling code assumes width and height can be changed independently. Setting width to 10 and height to 20 on the Square results in an area of 400 rather than the Rectangle expectation of 200.

### Initial violation
`FixedDepositAccount` originally inherited/overrode `withdraw()` and rejected the operation. A loop over mixed accounts therefore encountered an unsupported operation.

### Refactoring
A `Withdrawable` capability interface was introduced. Only account types that genuinely support withdrawal implement it.

- `SavingsAccount` → `Withdrawable`
- `CurrentAccount` → `Withdrawable`
- `FixedDepositAccount` → not `Withdrawable`

Withdrawal code now works with `List[Withdrawable]` conceptually rather than assuming every `Account` can be withdrawn from.

### Main files
- `LSP_RectangleSquare.py`
- `Section3_1_LSP_Explanation.md`
- `FixedDepositAccount.py`
- `Section3_3_WithdrawalCrash.py`
- `Withdrawable.py`
- `Section3_4_LSP_Fixed.py`
- `Section3_LSP_WrapUp.md`

### Key idea
A subtype must be safely substitutable wherever its base type is expected. A class should not implement a contract that it cannot fulfill.

## Section 4 — ISP + DIP: Interface Segregation and Dependency Inversion

**Problem 1 — ISP:** The ATM did not need every operation in a large `BankService` interface.

**Problem 2 — DIP:** `Bank` should not be tightly coupled to one concrete storage implementation.

### ISP refactoring
The large interface was split into smaller capability interfaces:
- `Depositable`
- `Withdrawable`
- `Transferable`
- `StatementProvider`
- `LoanEligible`

The ATM only implements the capabilities it actually needs:
- Deposit
- Withdrawal

A `SavingsAccount` can implement the capabilities it genuinely supports.

### DIP refactoring
`AccountRepository` is used as the abstraction for account storage. Concrete repositories can be swapped without changing the bank's business logic.

Example storage implementations:
- `InMemoryAccountRepository`
- `FileAccountRepository`

`FileAccountRepository` stores simple account records in plain text using:

```text
accountNumber,name,balance
```

The repository implementation can be changed in `Main.py` while `Bank.py` remains unchanged.

### Main files
- `BankService.py`
- `Depositable.py`
- `Withdrawable.py`
- `Transferable.py`
- `StatementProvider.py`
- `LoanEligible.py`
- `ATM.py`
- `SavingsAccount.py`
- `CurrentAccount.py`
- `AccountRepository.py`
- `InMemoryAccountRepository.py`
- `FileAccountRepository.py`
- `Bank.py`
- `Main.py`
- `Section4_ISP_DIP_WrapUp.md`

### Key idea
- **ISP:** Clients should not be forced to depend on methods they do not use.
- **DIP:** High-level modules should depend on abstractions, not concrete implementations.

## Final Architecture

```text
                         GreenLeaf Bank
                               |
                 +-------------+-------------+
                 |                           |
          Account operations          External services
                 |                           |
        +--------+---------+          +------+------+
        |        |         |          |             |
     Savings  Current    Salary   Notification  Repository
        |        |         |          |             |
  Withdrawable  ...     Interest   Email/SMS     InMemory/File
  Depositable           Policy
  Transferable
  StatementProvider
```

## SOLID Principles Covered

| Principle | Main improvement |
|---|---|
| **SRP** | Separated account operations, persistence, notifications, and statements |
| **OCP** | Added account/interest policies without modifying existing policy classes |
| **LSP** | Removed unsupported withdrawal behavior from accounts that cannot withdraw |
| **ISP** | Replaced one fat interface with focused capability interfaces |
| **DIP** | Made high-level bank logic depend on repository/notification abstractions |

## How to Run

The project uses Python 3. Run the relevant demonstration file from the repository root, for example:

```bash
python Main.py
```

Individual examples can also be run directly:

```bash
python LSP_RectangleSquare.py
python Section3_3_WithdrawalCrash.py
```

## Learning Outcome

Across the four sections, the original tightly coupled banking design is progressively transformed into a modular design where responsibilities are separated, new behavior is added through extension, invalid substitutions are prevented, interfaces are kept focused, and high-level code depends on abstractions.

## Repository

This is the GreenLeaf Bank SOLID-principles lab repository for the four-section refactoring exercise.
