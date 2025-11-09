from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float, nullable=False)
    currency = Column(Enum("GBP", "EUR", "USD", "JPY", name="currency"), nullable=False)
    type = Column(Enum("savings", "checking", name="account_type"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="accounts")
