from fastapi import APIRouter

from app.api.v1.endpoints.users import user_router
from app.api.v1.endpoints.accounts import account_router

api_router = APIRouter()
api_router.include_router(router=user_router, prefix="/user", tags=["user"])
api_router.include_router(router=account_router, prefix="/accounts", tags=["accounts"])
