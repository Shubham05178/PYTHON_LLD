from fixedaccount import FixedDepositAccount 
from svgacct import SavingsAccount
s1=SavingsAccount(100000)
s1.withdraw(5000)
s1.deposit(10000) 
print(s1.get_balance())

fd1=FixedDepositAccount(50000)
fd1.deposit(10000) 
print(fd1.get_balance())
