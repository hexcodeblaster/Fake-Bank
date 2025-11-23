from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    house_number = Column(String)
    street_address = Column(String)
    city = Column(String)
    county = Column(String)
    postcode = Column(String)
    user = relationship("User", back_populates="addresses")
