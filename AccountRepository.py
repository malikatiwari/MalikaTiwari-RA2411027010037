from abc import ABC, abstractmethod


class AccountRepository(ABC):
    @abstractmethod
    def save(self, account):
        pass

    @abstractmethod
    def read_all(self):
        pass
