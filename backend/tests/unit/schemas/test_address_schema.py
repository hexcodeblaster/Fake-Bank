from tests.factories.schemas.address import AddressSchemaFactory


class TestAddressSchema:
    def test_address_base(self):
        address_base = AddressSchemaFactory.get_address_base()
        assert address_base.house_number == "1/62A"
        assert address_base.street_address == "Brighton Road"
        assert address_base.city == "London"
        assert address_base.county == "London"
        assert address_base.postcode == "ECR 1YN"

    def test_address_create(self):
        address_create = AddressSchemaFactory.get_address_create(user_id = 1)
        assert address_create.house_number == "1/62A"
        assert address_create.street_address == "Brighton Road"
        assert address_create.city == "London"
        assert address_create.county == "London"
        assert address_create.postcode == "ECR 1YN"
        assert address_create.user_id == 1

    def test_address_response(self):
        address_response = AddressSchemaFactory.get_address_response