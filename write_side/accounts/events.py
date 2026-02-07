class AccountCreated:
    def __init__(self, initial_balance: int):
        self.initial_balance = initial_balance

class MoneyDeposited:
    def __init__(self, amount: int):
        self.amount = amount

class MoneyWithdrawn:
    def __init__(self, amount: int):
        self.amount = amount
