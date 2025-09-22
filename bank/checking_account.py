from bank.bank_account import BankAccount


class CheckingAccount(BankAccount):
    __savings_balance: int

    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.__savings_balance = balance

    def withdraw(self, amount: int):
        self.__savings_balance -= amount

    def get_balance(self):
        return self.__savings_balance
