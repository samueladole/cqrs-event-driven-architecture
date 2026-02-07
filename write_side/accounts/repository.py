from write_side.accounts.models import Event
from write_side.accounts.aggregates import BankAccount

def load_account(account_id):
    """Load a bank account aggregate by replaying its events."""
    account = BankAccount()
    events = Event.objects.filter(
        aggregate_id=account_id,
        aggregate_type="BankAccount"
    )

    for event in events:
        account.apply({
            "event_type": event.event_type,
            "event_data": event.event_data
        })

    return account
