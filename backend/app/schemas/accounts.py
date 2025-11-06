from enum import Enum
import uuid

from pydantic import BaseModel

from app.schemas.users import User


class AccountType(str, Enum):
    SAVINGS = "savings"
    CHECKING = "checking"

class Accounts(BaseModel):
    id: uuid.UUID
    type:AccountType
    user: User
    balance: float
    overdraft_limit: int
