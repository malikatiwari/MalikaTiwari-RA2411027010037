from abc import ABC, abstractmethod


class StatementProvider(ABC):
    @abstractmethod
    def print_statement(self):
        pass
