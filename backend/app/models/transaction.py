from typing import Any

from sqlalchemy import CheckConstraint, Column, Enum, Float, ForeignKey, Integer
from sqlalchemy.orm import validates

from app.models import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(Enum("credit", "debit", name="transaction_type"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    account_id = Column(Integer, ForeignKey("accounts.id"))

    __table_args__ = (CheckConstraint("amount > 0", name="check_amount_is_positive"),)

    @validates("amount")
    def validate_age(self, _: str, amount: Any) -> float:
        """
        Validates age
        :param _: Is always going to be string 'amount'
        :param amount: the value of parameter 'amount'
        :return: amount if no validation fails
        """
        if amount is None:
            raise ValueError("Amount can't be None")
        if not isinstance(amount, (float, int)):
            raise ValueError("Amount can't be non number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return amount
