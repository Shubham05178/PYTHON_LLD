from bankaccount import BankAccount
from abc import abstractmethod
class WithdrawAccount(BankAccount):
    @abstractmethod
    def withdraw(self, amount):
        pass
       