from fastapi import APIRouter, FastAPI

from app.schemas.users import User

router = APIRouter()


@router.get("/{user_id}")
def landing_page(user_id: str) -> User:
    print("Got user id :", user_id)
    return "Hello world"


@router.get("/index")
def index_page():
    return "Hello from index"
