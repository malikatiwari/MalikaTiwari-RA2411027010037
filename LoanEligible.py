from abc import ABC, abstractmethod


class LoanEligible(ABC):
    @abstractmethod
    def apply_for_loan(self):
        pass
