from datetime import datetime

from pydantic import SecretStr

from app.schemas.account import AccountResponse, AccountType, CurrencyType
from app.schemas.address import AddressResponse
from app.schemas.user import (
    UserBase,
    UserCreate,
    UserInDB,
    UserResponse,
    UserResponseWithAccounts,
    UserResponseWithAddress,
    UserUpdate,
)


class classproperty:
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, owner):
        return self.fget(owner)


class UserSchemaFactory:
    _creation_time = datetime.now()

    @classproperty
    def creation_time(cls):
        return cls._creation_time

    @staticmethod
    def default_accounts_response_list() -> list[AccountResponse]:
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
        base_data_dict = {
            "email": "testemail@mail.com",
            "full_name": "user base",
            "phone_number": "9876543210",
        }
        return {**base_data_dict, **overrides}

    @staticmethod
    def base_response(*, creation_time: datetime, **overrides) -> dict:
        base_response_dict = {"id": 1, "created_at": creation_time, "updated_at": None}
        return {**UserSchemaFactory.base_data(), **base_response_dict, **overrides}

    @classmethod
    def get_user_base(cls, **overrides) -> UserBase:
        return UserBase(**cls.base_data(), **overrides)

    @classmethod
    def get_user_create(cls, **overrides) -> UserCreate:
        return UserCreate(**cls.base_data(), password=SecretStr("secret"), **overrides)

    @classmethod
    def get_user_update(cls, **overrides) -> UserUpdate:
        return UserUpdate(**overrides)

    @classmethod
    def get_user_response(cls, *, creation_time: datetime, **overrides) -> UserResponse:
        return UserResponse(
            **cls.base_response(creation_time=creation_time), **overrides
        )

    @classmethod
    def get_user_response_with_accounts(
        cls, *, creation_time: datetime, **overrides
    ) -> UserResponseWithAccounts:
        return UserResponseWithAccounts(
            **cls.base_response(creation_time=creation_time),
            accounts=cls.default_accounts_response_list(),
            **overrides
        )

    @classmethod
    def get_user_response_with_addresses(
        cls, *, creation_time: datetime, **overrides
    ) -> UserResponseWithAddress:
        return UserResponseWithAddress(
            **cls.base_response(creation_time=creation_time),
            addresses=cls.default_address_response(),
            **overrides
        )

    @classmethod
    def get_user_in_db(cls, *, creation_time: datetime, **overrides):
        return UserInDB(
            **cls.base_response(creation_time=creation_time),
            hashed_password="secret",
            **overrides
        )
