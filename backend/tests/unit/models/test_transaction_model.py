from unittest.mock import Mock

import pytest

from app.models import Transaction


class TestTransactionModel:
    def test_transaction_creation(self, session):
        transaction = Transaction(
            type="credit",
            amount=24.91,
        )
        session.add(transaction)
        session.commit()
        db_transaction = session.get(Transaction, transaction.id)
        assert db_transaction.id is not None
        assert db_transaction.type == "credit"
        assert db_transaction.amount == 24.91

    def test_non_positive_amount(self):
        with pytest.raises(ValueError) as value_error:
            Transaction(
                type="debit",
                amount=0,
            )
        assert "Amount must be positive" in str(value_error.value)

    def test_none_amount(self):
        with pytest.raises(ValueError) as value_error:
            Transaction(type="debit", amount=None)
        assert "Amount can't be None" in str(value_error.value)

    def test_non_number_amount(self):
        with pytest.raises(ValueError) as value_error:
            Transaction(type="debit", amount="22")
        assert "Amount can't be non number" in str(value_error.value)
