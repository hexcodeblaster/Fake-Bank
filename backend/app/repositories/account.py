from app.schemas.account import AccountType, CurrencyType
from app.models import Account
from sqlalchemy.orm import Session

class AccountRepo:
    def create_account(self, db: Session, account_type: AccountType, balance: float, currency: CurrencyType, user_id: int) -> Account:
        account = Account(
            balance = balance,
            currency = currency,
            type = account_type,
            user_id = user_id
        )
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

    def get_account_by_user_id(self, db: Session,  user_id: int) -> Account | None:
        account = db.get(Account, user_id)
        return account