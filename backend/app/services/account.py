from app.repositories.account import AccountRepo
from sqlalchemy.orm import Session

from app.schemas.account import AccountCreate, AccountResponse


class AccountService:
    def __init__(self):
        self.account_repo = AccountRepo()

    def create_account(self, db: Session, account: AccountCreate) -> AccountResponse:
        created_account = self.account_repo.create_account(
            db=db,
            account_type=account.type,
            balance=account.balance,
            currency=account.currency,
            user_id=account.user_id
        )
        return AccountResponse(
            type=created_account.type,
            balance=created_account.balance,
            currency=created_account.currency,
            id=created_account.id,
            user_id=created_account.user_id
        )
