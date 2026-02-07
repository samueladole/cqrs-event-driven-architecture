from models import AccountReadModel

def apply_event(db, event):
    if event["event_type"] == "AccountCreated":
        db.add(AccountReadModel(
            account_id=event["aggregate_id"],
            balance=event["event_data"]["initial_balance"]
        ))

    elif event["event_type"] == "MoneyDeposited":
        account = db.get(AccountReadModel, event["aggregate_id"])
        account.balance += event["event_data"]["amount"]

    elif event["event_type"] == "MoneyWithdrawn":
        account = db.get(AccountReadModel, event["aggregate_id"])
        account.balance -= event["event_data"]["amount"]
