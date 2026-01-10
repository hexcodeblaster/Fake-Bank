from enum import Enum
from typing import TYPE_CHECKING
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

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

class AmountRequest(BaseModel):
    amount: Decimal = Field(..., ge=0, decimal_places=2)

class AccountBase(BaseModel):
    type: AccountType
    balance: Decimal = Field(... , ge=0)
    currency: CurrencyType

class AccountCreate(AccountBase):
    user_id: int


class AccountResponse(AccountBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)


class AccountWithUserResponse(AccountResponse):
    user: "UserResponse"

class AccountInDB(AccountResponse):
    pass
