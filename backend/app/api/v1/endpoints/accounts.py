from typing import Any
from decimal import Decimal
from app.schemas.account import AccountCreate, AccountResponse, AmountRequest
from app.services.account import AccountService, get_account_service
from fastapi import APIRouter, Depends, status

from app.core.database import get_db
from sqlalchemy.orm import Session

account_router = APIRouter()


@account_router.post("/create", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
def create_account(account: AccountCreate, db: Session = Depends(get_db), account_service: AccountService = Depends(get_account_service)) -> AccountResponse:
    created_account = account_service.create_account(db=db, account=account)
    return AccountResponse.model_validate(created_account)

@account_router.put("/{account_id}/withdraw", response_model=AccountResponse)
def withdraw(account_id: int, payload: AmountRequest, db: Session = Depends(get_db), account_service: AccountService = Depends(get_account_service)) -> AccountResponse:
    withdrew_account = account_service.withdraw(account_id=account_id, amount=payload.amount, db=db)
    return AccountResponse.model_validate(withdrew_account)

@account_router.put("/{account_id}/deposit", response_model=AccountResponse)
def deposit(account_id: int, payload:AmountRequest, db: Session = Depends(get_db), account_service: AccountService = Depends(get_account_service)) -> AccountResponse:
    deposited_account = account_service.deposit(account_id=account_id, amount=payload.amount, db=db)
    return AccountResponse.model_validate(deposited_account)

@account_router.get("/{account_id}/check")
def check_balance(account_id: int, db: Session = Depends(get_db), account_service: AccountService = Depends(get_account_service)) -> Decimal:
    return account_service.check_balance(account_id=account_id, db=db)
