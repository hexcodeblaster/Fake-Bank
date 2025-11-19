from app.schemas.account import (
    AccountType,
    CurrencyType,
    AccountBase,
    AccountCreate,
    AccountResponse,
    AccountWithUserResponse,
    AccountUpdate,
    AccountInDB,
)
from tests.factories.schemas.user import UserSchemaFactory


class AccountSchemaFactory:
    @staticmethod
    def base_data(**overrides) -> dict:
        base_data_dict = {
            "type": AccountType.SAVINGS,
            "balance": 100,
            "currency": CurrencyType.GBP,
        }
        return {**base_data_dict, **overrides}

    @staticmethod
    def response_data(**overrides) -> dict:
        response_data_dict = {**AccountSchemaFactory.base_data(), "id": 1, "user_id": 1}
        return {**response_data_dict, **overrides}

    @classmethod
    def get_account_base(cls, **overrides) -> AccountBase:
        return AccountBase(**cls.base_data(), **overrides)

    @classmethod
    def get_account_create(cls, **overrides) -> AccountCreate:
        return AccountCreate(**cls.base_data(), user_id=1, **overrides)

    @classmethod
    def get_account_response(cls, **overrides) -> AccountResponse:
        return AccountResponse(**cls.response_data(), **overrides)

    @classmethod
    def get_account_with_user_response(cls, **overrides) -> AccountWithUserResponse:
        return AccountWithUserResponse(
            **cls.response_data(),
            user=UserSchemaFactory.get_user_response(
                creation_time=UserSchemaFactory.creation_time
            ),
            **overrides
        )

    @classmethod
    def get_account_update(cls, **overrides) -> AccountUpdate:
        return AccountUpdate(**overrides)

    @classmethod
    def get_account_in_db(cls, **overrides) -> AccountInDB:
        return AccountInDB(**cls.response_data(), **overrides)
