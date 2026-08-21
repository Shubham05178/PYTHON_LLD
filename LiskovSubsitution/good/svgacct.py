from withdrawaccount import WithdrawAccount
class SavingsAccount(WithdrawAccount):
    def __init__(self, balance):
        super().__init__(balance)
    def withdraw(self, amount):
        if amount <= self._BankAccount__balance:
            self._BankAccount__balance -= amount
            print(f"Withdrew {amount}. New balance: {self._BankAccount__balance}")
        else:
            print("Insufficient funds.")
    def deposit(self, amount):
        self._BankAccount__balance += amount
        print(f"Deposited {amount}. New balance: {self._BankAccount__balance}")         