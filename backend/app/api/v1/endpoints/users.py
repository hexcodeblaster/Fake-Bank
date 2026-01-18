from app.schemas.user import UserCreate
from app.schemas.account import AccountResponse
from app.services.user import UserService
from app.services.account import AccountService
from fastapi import APIRouter, Depends

from app.core.database import get_db
from sqlalchemy.orm import Session


user_router = APIRouter()


@user_router.put("/create")
async def index_page(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService()
    created_user = user_service.create_user(db=db, user=user)
    return created_user

@user_router.get("/email/")
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user_service = UserService()
    return user_service.get_user_by_email(db= db, email=email)

@user_router.get("/all")
async def get_all_users(db: Session = Depends(get_db)):
    user_service = UserService()
    return user_service.get_all_users(db = db)

@user_router.get("/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService()
    return user_service.get_user_by_id(db=db, user_id=user_id)

@user_router.get("/{user_id}/accounts", response_model=list[AccountResponse])
async def get_user_accounts(user_id: int, db:Session = Depends(get_db)):
    accounts_service = AccountService()
    return accounts_service.get_accounts(user_id=user_id, db=db)
