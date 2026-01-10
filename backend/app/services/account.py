from fastapi import Depends

from app.repositories.account import AccountRepo, get_account_repo
from sqlalchemy.orm import Session
from decimal import Decimal
from app.schemas.account import AccountCreate
from app.models.account import Account

class AccountService:
    def __init__(self, account_repo: AccountRepo):
        self.account_repo = account_repo

    def create_account(self, db: Session, account: AccountCreate) -> Account:
        created_account = self.account_repo.create_account(
            db=db,
            account_type=account.type,
            balance=account.balance,
            currency=account.currency,
            user_id=account.user_id
        )
        return created_account

    def get_accounts(self, user_id:int, db: Session) -> list[Account]:
        accounts= self.account_repo.get_accounts_by_user_id(db=db, user_id=user_id)
        return accounts

    def withdraw(self, account_id: int, amount:Decimal, db: Session) -> Account:
        return self.account_repo.withdraw(db=db, account_id=account_id, amount=amount)

    def deposit(self, account_id: int, amount:Decimal, db: Session) -> Account:
        return self.account_repo.deposit(db=db, account_id=account_id, amount=amount)

    def check_balance(self, account_id: int, db: Session) -> Decimal:
        return self.account_repo.check_balance(db=db, account_id=account_id)

def get_account_service(account_repo: AccountRepo = Depends(get_account_repo)) -> AccountService:
    return AccountService(account_repo)
