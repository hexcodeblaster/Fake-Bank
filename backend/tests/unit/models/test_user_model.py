import pytest
from sqlalchemy.exc import IntegrityError

from app.models import User


class TestUserModel:
    def test_user_model_creation(self, session):
        user_1 = User(
            email="user1mail@gmai.com",
            hashed_password="super_secret_hashed_password",
            full_name="User 1",
        )
        session.add(user_1)
        session.commit()

        db_user = session.get(User, user_1.id)
        assert db_user is not None
        assert db_user.id is not None
        assert db_user.email == user_1.email
        assert db_user.full_name == user_1.full_name

    def test_unique_email_storage(self, session):
        user_1 = User(
            email="user1mail@gmai.com",
            hashed_password="super_secret_hashed_password_for_user_1",
            full_name="User 1",
        )
        user_2 = User(
            email="user1mail@gmai.com",
            hashed_password="super_secret_hashed_password_for_user_2",
            full_name="User 2",
        )
        session.add(user_1)
        session.add(user_2)
        with pytest.raises(IntegrityError) as exc_info:
            session.commit()
        assert "unique constraint failed: users.email" in str(exc_info.value).lower()

    def test_nonempty_email_field(self, session):
        user_1 = User(
            email=None,
            hashed_password="super_secret_hashed_password",
            full_name="User 1",
        )
        session.add(user_1)
        with pytest.raises(IntegrityError) as exc_info:
            session.commit()
        assert "not null constraint failed: users.email" in str(exc_info.value).lower()
