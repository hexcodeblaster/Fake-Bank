from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, EmailStr, SecretStr

if TYPE_CHECKING:
    from app.schemas.account import AccountResponse
    from app.schemas.address import AddressResponse


class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone_number: str


class UserCreate(UserBase):
    password: SecretStr


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    full_name: str | None = None
    phone_number: str | None = None


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    model_config = ConfigDict(from_attributes=True)


class UserResponseWithAccounts(UserResponse):
    accounts: list["AccountResponse"]


class UserResponseWithAddress(UserResponse):
    addresses: list["AddressResponse"]


class UserInDB(UserResponse):
    hashed_password: str
