from datetime import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import User
from app.core.security import get_password_hash

class UserRepository:
    def create_user(self,db: Session, email: str, full_name: str, phone_number: str, hashed_password: str):
        user = User(
            email = email,
            hashed_password = hashed_password,
            full_name = full_name,
            phone_number = phone_number
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_id(self, db: Session, user_id: int) -> User | None:
        return db.get(User, user_id)

    def get_user_by_email(self, db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    def get_all_users(self, db: Session) -> Sequence[User]:
        users = db.scalars(select(User)).all()
        return users
