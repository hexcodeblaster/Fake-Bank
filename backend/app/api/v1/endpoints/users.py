from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get('/', tags=['nothing', 'money'])
def landing_page():
    return "Hello world"

@router.get('/index', tags=['index', 'money'])
def index_page():
    return "Hello from index"
