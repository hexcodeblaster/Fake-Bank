from datetime import datetime

from pydantic import SecretStr

from app.schemas.account import AccountResponse
from app.schemas.address import AddressResponse
from app.schemas.user import (UserResponseWithAccounts,
                              UserResponseWithAddress, UserUpdate)
from tests.factories.schemas.user import UserSchemaFactory

UserResponseWithAccounts.model_rebuild()
UserResponseWithAddress.model_rebuild()


class TestUserSchema:
    def test_user_base(self):
        user_base = UserSchemaFactory.get_user_base()
        assert user_base.email == "testemail@mail.com"
        assert user_base.full_name == "user base"
        assert user_base.phone_number == "9876543210"

    def test_user_create(self):
        user_create = UserSchemaFactory.get_user_create(full_name="user create")
        assert user_create.email == "testemail@mail.com"
        assert user_create.full_name == "user create"
        assert user_create.phone_number == "9876543210"
        assert user_create.password == SecretStr("secret")

    def test_user_update(self):
        user_update = UserUpdate(full_name="user update")
        assert user_update.email is None
        assert user_update.full_name == "user update"
        assert user_update.phone_number is None

    def test_user_response(self, get_current_time):
        user_response = UserSchemaFactory.get_user_response(
            full_name="user response", creation_time=get_current_time
        )
        assert user_response.email == "testemail@mail.com"
        assert user_response.full_name == "user response"
        assert user_response.phone_number == "9876543210"
        assert user_response.id == 1
        assert user_response.created_at == get_current_time
        assert user_response.updated_at is None

    def test_user_response_with_accounts(self, get_current_time):
        user_response_with_accounts = UserSchemaFactory.get_user_response_with_accounts(
            full_name="user response with accounts",
            creation_time=get_current_time,
        )
        assert user_response_with_accounts.email == "testemail@mail.com"
        assert user_response_with_accounts.full_name == "user response with accounts"
        assert user_response_with_accounts.phone_number == "9876543210"
        assert user_response_with_accounts.id == 1
        assert user_response_with_accounts.created_at == get_current_time
        assert user_response_with_accounts.updated_at is None
        assert (
            user_response_with_accounts.accounts
            == UserSchemaFactory.default_account_response()
        )

    def test_user_response_with_addresses(self, get_current_time):
        user_response_with_addresses = (
            UserSchemaFactory.get_user_response_with_addresses(
                full_name="user response with address", creation_time=get_current_time
            )
        )
        assert user_response_with_addresses.email == "testemail@mail.com"
        assert user_response_with_addresses.full_name == "user response with address"
        assert user_response_with_addresses.phone_number == "9876543210"
        assert user_response_with_addresses.id == 1
        assert user_response_with_addresses.created_at == get_current_time
        assert user_response_with_addresses.updated_at is None
        assert (
            user_response_with_addresses.addresses
            == UserSchemaFactory.default_address_response()
        )

    def test_user_in_db(self, get_current_time):
        user_in_db = UserSchemaFactory.get_user_in_db(
            full_name="user in db", creation_time=get_current_time
        )
        assert user_in_db.email == "testemail@mail.com"
        assert user_in_db.full_name == "user in db"
        assert user_in_db.phone_number == "9876543210"
        assert user_in_db.id == 1
        assert user_in_db.created_at == get_current_time
        assert user_in_db.updated_at is None
        assert user_in_db.hashed_password == "secret"
