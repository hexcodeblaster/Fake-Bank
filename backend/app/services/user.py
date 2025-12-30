from app.core.security import get_password_hash
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from pydantic import EmailStr, SecretStr

from app.schemas.user import UserResponse


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, db: Session,user: UserCreate) -> UserResponse:
        saved_user = self.user_repo.create_user(
            db=db,
            email=user.email,
            full_name=user.full_name,
            phone_number=user.phone_number,
            hashed_password=get_password_hash(user.password.get_secret_value())
        )
        return UserResponse(
            id = saved_user.id,
            email=saved_user.email,
            full_name=saved_user.full_name,
            phone_number=saved_user.phone_number,
            created_at=saved_user.created_at,
            updated_at=saved_user.updated_at
        )

    def get_user_by_id(self, db: Session, user_id: int) -> UserResponse | None:
        returned_user =  self.user_repo.get_user_by_id(db=db, user_id=user_id)
        return UserResponse(
            id=returned_user.id,
            email=returned_user.email,
            full_name=returned_user.full_name,
            phone_number=returned_user.phone_number,
            created_at=returned_user.created_at,
            updated_at=returned_user.updated_at
        )

    def get_user_by_email(self, db: Session, email: str) -> UserResponse | None:
        returned_user = self.user_repo.get_user_by_email(db=db, email=email)
        return UserResponse(
            id=returned_user.id,
            email=returned_user.email,
            full_name=returned_user.full_name,
            phone_number=returned_user.phone_number,
            created_at=returned_user.created_at,
            updated_at=returned_user.updated_at
        )

    def get_all_users(self, db: Session) -> list[UserResponse]:
        returned_users_list = self.user_repo.get_all_users(db=db)
        return [
            UserResponse(
                id=returned_user.id,
                email=returned_user.email,
                full_name=returned_user.full_name,
                phone_number=returned_user.phone_number,
                created_at=returned_user.created_at,
                updated_at=returned_user.updated_at
            )
            for returned_user in returned_users_list
        ]


