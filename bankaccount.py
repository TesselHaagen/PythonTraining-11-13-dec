class BankAccount:
    """
    A class for bankaccounts

    Attributes:
    - balance (float): 
    - holder (str):

    Methods:
    - deposit
    - withdraw
    - info
    """
    def __init__(self, balance: float, holder: str):
        self.balance = balance
        self.holder = holder
    
    def deposit(self, amount):
        """
        Deposit amount of money to the balance

        Args:
        - amount (float): the amount to deposit
        """
        self.balance += amount
    
    def withdraw(self, amount):
        """
        Withdraws amount of money from the balance

        Args:
        - amount (float): the amount to withdraw
        """
        self.balance -= amount
    
    def info(self):
        """
        Gives information about the bankaccount

        Retunrs:
        - string with info about the bankaccount
        """
        return f'Current Balance: {self.balance} Holder: {self.holder}'



bankaccount1 = BankAccount(1000, 'Tessel')
bankaccount2 = BankAccount(2000, 'Peter')
hoi = 10

print(isinstance(hoi, BankAccount))
# Roep deposit aan van class BankAccount : deposit(bankaccount1, 500)
bankaccount1.deposit(500)
print(bankaccount1.info())