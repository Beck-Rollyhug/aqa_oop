class BankAccount:
    owner: str
    __balance: int

    def __init__(self, owner: str, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount: int):
        if self.__balance + amount > 0:
            self.__balance += amount
        else:
            raise ValueError

    def withdraw(self, amount: int):
        if self.__balance - amount > 0:
            self.__balance -= amount
        else:
            raise ValueError

    def get_balance(self):
        return self.__balance
