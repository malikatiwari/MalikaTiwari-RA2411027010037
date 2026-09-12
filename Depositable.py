from abc import ABC, abstractmethod


class Depositable(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
