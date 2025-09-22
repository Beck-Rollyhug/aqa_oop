from math import floor

from bank.bank_account import BankAccount


class SavingsAccount(BankAccount):
    interest_rate: float

    def __init__(self, owner: str, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        balance = self.get_balance()
        interest = floor(balance * self.interest_rate)
        self.deposit(interest)
