from bank.savings_account import SavingsAccount


def test_bank():
    account = SavingsAccount('Jon')
    account.deposit(500)
    account.withdraw(100)
    account.apply_interest()

    assert account.get_balance() > 0, 'Сумма не положительная'
