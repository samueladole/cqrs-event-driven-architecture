import uuid
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from write_side.accounts.models import Event
from write_side.accounts.repository import load_account

@require_POST
def create_account(request):
    account_id = uuid.uuid4()
    initial_balance = int(request.POST["initial_balance"])

    account = load_account(account_id)
    event = account.create(initial_balance)

    Event.objects.create(
        aggregate_id=account_id,
        aggregate_type="BankAccount",
        event_type=event["event_type"],
        event_data=event["event_data"],
    )

    return JsonResponse({"account_id": str(account_id)})
