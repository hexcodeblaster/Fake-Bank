from app.schemas.user import UserCreate
from app.services.user import UserService
from fastapi import APIRouter, Depends

from app.core.database import get_db
from sqlalchemy.orm import Session

user_router = APIRouter()


@user_router.put("/create")
def index_page(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService()
    created_user = user_service.create_user(db=db, user=user)
    return created_user

@user_router.get("/id/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService()
    return user_service.get_user_by_id(db=db, user_id=user_id)

@user_router.get("/email/{email}")
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user_service = UserService()
    return user_service.get_user_by_email(db= db, email=email)

@user_router.get("/all")
def get_all_users(db: Session = Depends(get_db)):
    user_service = UserService()
    return user_service.get_all_users(db = db)
