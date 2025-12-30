from app.schemas.account import AccountCreate
from app.services.account import AccountService
from fastapi import APIRouter, Depends

from app.core.database import get_db
from sqlalchemy.orm import Session

account_router = APIRouter()


@account_router.put("/create")
def index_page(account: AccountCreate, db: Session = Depends(get_db)):
    account_service = AccountService()
    created_account = account_service.create_account(db=db, account=account)
    return created_account
