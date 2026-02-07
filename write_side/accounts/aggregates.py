class BankAccount:
    def __init__(self):
        self.balance = 0
        self.exists = False

    def apply(self, event):
        if event["event_type"] == "AccountCreated":
            self.exists = True
            self.balance = event["event_data"]["initial_balance"]

        elif event["event_type"] == "MoneyDeposited":
            self.balance += event["event_data"]["amount"]

        elif event["event_type"] == "MoneyWithdrawn":
            self.balance -= event["event_data"]["amount"]

    def create(self, initial_balance):
        if self.exists:
            raise Exception("Account already exists")
        return {
            "event_type": "AccountCreated",
            "event_data": {"initial_balance": initial_balance},
        }

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount")
        return {
            "event_type": "MoneyDeposited",
            "event_data": {"amount": amount},
        }

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds")
        return {
            "event_type": "MoneyWithdrawn",
            "event_data": {"amount": amount},
        }
