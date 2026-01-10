from typing import Sequence
from decimal import Decimal
from fastapi import HTTPException

from app.schemas.account import AccountType, CurrencyType
from app.models import Account
from sqlalchemy.orm import Session
from sqlalchemy import select


class AccountRepo:
    def create_account(
        self,
        db: Session,
        account_type: AccountType,
        balance: Decimal,
        currency: CurrencyType,
        user_id: int,
    ) -> Account:
        try:
            account: Account = Account(
                balance=balance, currency=currency, type=account_type, user_id=user_id
            )
            db.add(account)
            db.commit()
            db.refresh(account)
            return account
        except Exception:
            db.rollback()
            raise

    def get_accounts_by_user_id(self, db: Session, user_id: int) -> list[Account]:
        account_query = select(Account).where(Account.user_id == user_id)  # type: ignore
        accounts = list(db.scalars(account_query).all())
        return accounts

    def withdraw(self, db: Session, account_id: int, amount: Decimal) -> Account:
        try:
            account: Account |None = db.get(Account, account_id)
            if account is None:
                raise HTTPException(status_code=404, detail="Account not found")
            if account.balance < amount:
                raise HTTPException(status_code=404, detail="Not enough balance to withdraw")
            account.balance -= amount
            db.commit()
            db.refresh(account)
            return account
        except Exception:
            db.rollback()
            raise

    def deposit(self, db: Session, account_id: int, amount: Decimal) -> Account:
        try:
            account: Account|None = db.get(Account, account_id)
            if account is None:
                raise HTTPException(status_code=404, detail="Account not found")
            account.balance += amount
            db.commit()
            db.refresh(account)
            return account
        except Exception:
            db.rollback()
            raise

    def check_balance(self, db: Session, account_id: int) -> Decimal:
        account: Account|None = db.get(Account, account_id)
        if account is None:
            raise HTTPException(status_code=404, detail="Account not found")
        return account.balance

def get_account_repo() -> AccountRepo:
    return AccountRepo()
