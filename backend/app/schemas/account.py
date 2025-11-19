from enum import Enum
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from app.schemas.user import UserResponse


class AccountType(str, Enum):
    SAVINGS = "savings"
    CHECKING = "checking"


class CurrencyType(str, Enum):
    GBP = "GBP"
    EUR = "EUR"
    USD = "USD"
    JPY = "JPY"


class AccountBase(BaseModel):
    type: AccountType
    balance: float
    currency: CurrencyType


class AccountCreate(AccountBase):
    user_id: int


class AccountResponse(AccountBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)


class AccountWithUserResponse(AccountResponse):
    user: "UserResponse"


class AccountUpdate(BaseModel):
    balance: float | None = None
    currency: CurrencyType | None = None
    type: AccountType | None = None


class AccountInDB(AccountResponse):
    pass
