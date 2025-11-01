from fastapi import FastAPI

app = FastAPI()

app.get('/')
def landing_page():
    print("Hello world")
