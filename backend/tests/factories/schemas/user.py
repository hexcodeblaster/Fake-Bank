from datetime import datetime

from pydantic import SecretStr

from app.schemas.account import AccountResponse, AccountType, CurrencyType
from app.schemas.address import AddressResponse
from app.schemas.user import (UserBase, UserCreate, UserInDB, UserResponse,
                              UserResponseWithAccounts,
                              UserResponseWithAddress, UserUpdate)


class UserSchemaFactory:
    @staticmethod
    def default_account_response() -> list[AccountResponse]:
        return [
            AccountResponse(
                type=AccountType.SAVINGS,
                balance=200,
                currency=CurrencyType.GBP,
                id=1,
                user_id=1,
            ),
            AccountResponse(
                type=AccountType.CHECKING,
                balance=400,
                currency=CurrencyType.USD,
                id=2,
                user_id=1,
            ),
        ]

    @staticmethod
    def default_address_response() -> list[AddressResponse]:
        return [
            AddressResponse(
                house_number="1/62A",
                street_address="Brighton Road",
                city="London",
                county="London",
                postcode="ECR 1YN",
                id=1,
                user_id=1,
            ),
            AddressResponse(
                house_number="5/21",
                street_address="Liverpool Street",
                city="London",
                county="London",
                postcode="EC5 3CN",
                id=2,
                user_id=1,
            ),
        ]

    @staticmethod
    def base_data(**overrides) -> dict:
        base_data = {
            "email": "testemail@mail.com",
            "full_name": "user base",
            "phone_number": "9876543210",
        }
        return {**base_data, **overrides}

    @staticmethod
    def base_response(*, creation_time: datetime, **overrides) -> dict:
        base_response = {"id": 1, "created_at": creation_time, "updated_at": None}
        return {**UserSchemaFactory.base_data(), **base_response, **overrides}

    @classmethod
    def get_user_base(cls, **overrides) -> UserBase:
        user_base = UserBase(**{**cls.base_data(), **overrides})
        return user_base

    @classmethod
    def get_user_create(cls, **overrides) -> UserCreate:
        user_create = UserCreate(
            **{**cls.base_data(), "password": SecretStr("secret"), **overrides}
        )
        return user_create

    @classmethod
    def get_user_update(cls, **overrides) -> UserUpdate:
        user_update = UserUpdate(**overrides)
        return user_update

    @classmethod
    def get_user_response(cls, *, creation_time: datetime, **overrides) -> UserResponse:
        user_response = UserResponse(
            **{**cls.base_response(creation_time=creation_time), **overrides}
        )
        return user_response

    @classmethod
    def get_user_response_with_accounts(
        cls, *, creation_time: datetime, **overrides
    ) -> UserResponseWithAccounts:
        user_response_with_accounts = UserResponseWithAccounts(
            **{
                **cls.base_response(creation_time=creation_time),
                "accounts": cls.default_account_response(),
                **overrides,
            }
        )
        return user_response_with_accounts

    @classmethod
    def get_user_response_with_addresses(
        cls, *, creation_time: datetime, **overrides
    ) -> UserResponseWithAddress:
        user_response_with_address = UserResponseWithAddress(
            **{
                **cls.base_response(creation_time=creation_time),
                "addresses": cls.default_address_response(),
                **overrides,
            }
        )
        return user_response_with_address

    @classmethod
    def get_user_in_db(cls, *, creation_time: datetime, **overrides):
        user_in_db = UserInDB(
            **{
                **cls.base_response(creation_time=creation_time),
                "hashed_password": "secret",
                **overrides,
            }
        )
        return user_in_db
