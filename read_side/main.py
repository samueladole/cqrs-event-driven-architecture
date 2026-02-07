from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database.dependencies import get_db
from .models.account import AccountReadModel
from .service_registration import register

@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Lifespan function to handle startup and shutdown events."""
    # Startup: Register the service
    register()
    yield
    # Shutdown: Unregister the service (if needed)
    # Note: Unregistration logic can be added here if the registry supports it.

app = FastAPI(lifespan=lifespan)

@app.get("/accounts/{account_id}")
def get_account(account_id: str, db: Session = Depends(get_db)):
    account = db.get(AccountReadModel, account_id)

    if not account:
        return {"error": "Account not found"}

    return {
        "account_id": account.account_id,
        "balance": account.balance,
    }
