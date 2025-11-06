import uuid

from pydantic import BaseModel

class User(BaseModel):
    id : uuid.UUID
    email: str
    firstname: str
    lastname: str
    phone_no: str
    residence: str
