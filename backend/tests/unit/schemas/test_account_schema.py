from tests.factories.schemas.account import (
    AccountSchemaFactory,
    AccountType,
    CurrencyType,
    AccountWithUserResponse,
)
from tests.factories.schemas.user import UserResponse, UserSchemaFactory

AccountWithUserResponse.model_rebuild()


class TestAccountSchema:
    def test_account_base(self):
        account_base = AccountSchemaFactory.get_account_base(type=AccountType.CHECKING)
        assert account_base.type == AccountType.CHECKING
        assert account_base.balance == 100
        assert account_base.currency == CurrencyType.GBP

    def test_account_create(self):
        account_create = AccountSchemaFactory.get_account_create(user_id=10)
        assert account_create.type == AccountType.SAVINGS
        assert account_create.balance == 100
        assert account_create.currency == CurrencyType.GBP
        assert account_create.user_id == 10

    def test_account_response(self):
        account_response = AccountSchemaFactory.get_account_response(id=5)
        assert account_response.type == AccountType.SAVINGS
        assert account_response.balance == 100
        assert account_response.currency == CurrencyType.GBP
        assert account_response.id == 5
        assert account_response.user_id == 1

    def test_account_response_with_user_response(self):
        account_response_with_response = (
            AccountSchemaFactory.get_account_with_user_response(id=5)
        )
        assert account_response_with_response.type == AccountType.SAVINGS
        assert account_response_with_response.balance == 100
        assert account_response_with_response.currency == CurrencyType.GBP
        assert account_response_with_response.id == 5
        assert account_response_with_response.user_id == 1
        assert (
            account_response_with_response.user
            == UserSchemaFactory.get_user_response(
                creation_time=UserSchemaFactory.creation_time
            )
        )
