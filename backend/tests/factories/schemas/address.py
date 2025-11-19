from app.schemas.address import (
    AddressBase,
    AddressCreate,
    AddressResponse,
    AddressResponseWithUser,
    AddressInDB,
)
from tests.factories.schemas.user import UserSchemaFactory


class AddressSchemaFactory:
    @staticmethod
    def base_data(**overrides) -> dict:
        base_data_dict = {
            "house_number": "1/62A",
            "street_address": "Brighton Road",
            "city": "London",
            "county": "London",
            "postcode": "ECR 1YN",
        }
        return {**base_data_dict, **overrides}

    @staticmethod
    def response_data(**overrides) -> dict:
        base_response_dict = {"id": 1, "user_id": 1}
        return {**AddressSchemaFactory.base_data(), **base_response_dict, **overrides}

    @classmethod
    def get_address_base(cls, **overrides) -> AddressBase:
        return AddressBase(**cls.base_data(), **overrides)

    @classmethod
    def get_address_create(cls, **overrides) -> AddressCreate:
        return AddressCreate(**cls.base_data(), user_id=1, **overrides)

    @classmethod
    def get_address_response(cls, **overrides) -> AddressResponse:
        return AddressResponse(**cls.response_data(), **overrides)

    @classmethod
    def get_address_response_with_user(cls, **overrides) -> AddressResponseWithUser:
        return AddressResponseWithUser(
            **cls.response_data(),
            user=UserSchemaFactory.get_user_response(
                creation_time=UserSchemaFactory.creation_time
            ),
            **overrides
        )

    @classmethod
    def get_address_in_db(cls, **overrides) -> AddressInDB:
        return AddressInDB(**cls.response_data(), **overrides)
