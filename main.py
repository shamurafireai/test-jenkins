from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/time")
def get_server_time():
    """
    Returns the current server time in ISO format.
    """
    now = datetime.utcnow()
    return {"server_time": now.isoformat() + "Z"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

@app.get("/mul")
def add_numbers(a: int, b: int):
    return {"result": a * b}

@app.get("/div")
def add_numbers(a: int, b: int):
    return {"result": a / b}
    
@app.get("/mula")
def show_message():
    return {"message": "welcome to deshimula"}
