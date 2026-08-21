from bankaccount import BankAccount
class FixedDepositAccount(BankAccount):
    def __init__(self,balance):
        super().__init__(balance)
    def deposit(self, amount):
        self._BankAccount__balance += amount
        print(f"Deposited {amount}. New balance: {self._BankAccount__balance}") 