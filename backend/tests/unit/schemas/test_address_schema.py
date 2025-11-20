from tests.factories.schemas.address import (
    AddressSchemaFactory,
    AddressResponseWithUser,
)
from tests.factories.schemas.user import UserSchemaFactory, UserResponse

AddressResponseWithUser.model_rebuild()


class TestAddressSchema:
    def test_address_base(self):
        address_base = AddressSchemaFactory.get_address_base()
        assert address_base.house_number == "1/62A"
        assert address_base.street_address == "Brighton Road"
        assert address_base.city == "London"
        assert address_base.county == "London"
        assert address_base.postcode == "ECR 1YN"

    def test_address_create(self):
        address_create = AddressSchemaFactory.get_address_create(user_id=10)
        assert address_create.house_number == "1/62A"
        assert address_create.street_address == "Brighton Road"
        assert address_create.city == "London"
        assert address_create.county == "London"
        assert address_create.postcode == "ECR 1YN"
        assert address_create.user_id == 10

    def test_address_response(self):
        address_response = AddressSchemaFactory.get_address_response(user_id=10)
        assert address_response.house_number == "1/62A"
        assert address_response.street_address == "Brighton Road"
        assert address_response.city == "London"
        assert address_response.county == "London"
        assert address_response.postcode == "ECR 1YN"
        assert address_response.user_id == 10

    def test_address_response_with_user(self):
        address_response_with_user = (
            AddressSchemaFactory.get_address_response_with_user(user_id=10)
        )
        assert address_response_with_user.house_number == "1/62A"
        assert address_response_with_user.street_address == "Brighton Road"
        assert address_response_with_user.city == "London"
        assert address_response_with_user.county == "London"
        assert address_response_with_user.postcode == "ECR 1YN"
        assert address_response_with_user.user_id == 10
        assert (
            address_response_with_user.user.created_at
            == UserSchemaFactory.creation_time
        )
        assert isinstance(address_response_with_user.user, UserResponse)

    def test_address_in_db(self):
        address_in_db = AddressSchemaFactory.get_address_in_db(user_id=10)
        assert address_in_db.house_number == "1/62A"
        assert address_in_db.street_address == "Brighton Road"
        assert address_in_db.city == "London"
        assert address_in_db.county == "London"
        assert address_in_db.postcode == "ECR 1YN"
        assert address_in_db.user_id == 10
