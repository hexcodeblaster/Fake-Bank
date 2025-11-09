import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Account


class TestAccountsModel:
    def test_account_creation(self, session):
        account = Account(balance=244, type="savings", currency="GBP")
        session.add(account)
        session.commit()
        db_account = session.get(Account, account.id)
        assert db_account.id == account.id
        assert db_account.balance == account.balance
        assert db_account.type == account.type
        assert db_account.currency == "GBP"

    def test_nonempty_account_balance(self, session):
        account = Account(balance=None, currency="USD")
        session.add(account)
        with pytest.raises(IntegrityError) as integrity_error:
            session.commit()
        assert (
            "not null constraint failed: accounts.balance"
            in str(integrity_error.value).lower()
        )

    def test_nonempty_account_type(self, session):
        account = Account(balance=244, currency=None)
        session.add(account)
        with pytest.raises(IntegrityError) as integrity_error:
            session.commit()
        assert (
            "not null constraint failed: accounts.currency"
            in str(integrity_error.value).lower()
        )
