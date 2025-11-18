from typing import TYPE_CHECKING
from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from app.schemas.user import UserResponse

class AddressBase(BaseModel):
    house_number: str
    street_address: str
    city: str
    county: str
    postcode: str

class AddressCreate(AddressBase):
    user_id: int

class AddressResponse(AddressBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)

class AddressResponseWithUser(AddressResponse):
    user: "UserResponse"

class AddressInDB(AddressResponse):
    pass
