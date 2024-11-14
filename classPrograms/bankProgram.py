# Create a class called BankAccount with attributes account_number, balance,
# and . Implement methods to deposit, withdraw, and display the account balance.


class BankAccount():
    def __init__(self,account_number,balance,owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        
    def deposit(self,balance):
        self.balance = self.balance+balance
        return self.balance
    def withdraw(self,withdraw):
        if withdraw > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance-withdraw
            return self.balance
        
    def display_balance(self):
        return self.balance
        



obj = BankAccount(account_number=2345,balance=80000,owner_name='akash')
print(f'user name : {obj.owner_name} \naccount number : {obj.account_number} \ncurrent balance : {obj.display_balance()}')
print(f'Amount has been desposited sucessfully - {obj.deposit(20000)}')
print(f'Amount has been withdrawn sucessfully - {obj.withdraw(10000)}')
print(f'Current balance of the account {obj.account_number} - {obj.display_balance()}')