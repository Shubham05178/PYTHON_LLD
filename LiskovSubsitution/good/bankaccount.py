from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
     self.__balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    def get_balance(self):
        return self.__balance

