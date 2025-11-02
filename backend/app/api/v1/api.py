from fastapi import APIRouter

from app.api.v1.endpoints.users import router

api_router = APIRouter()
api_router.include_router(router=router, prefix='/users', tags=['users'])
