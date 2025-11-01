from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def landing_page():
    print("Hello world")
    return "Hello world"

@app.get('/index')
def index_page():
    print("Hello from index")
    return "Hello from index"
