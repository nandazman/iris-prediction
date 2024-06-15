from typing import Union

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/greetings/{name}')
def greetings(name: str, request: Request):
    result = f'Good Morning, {name}'

    return {
        'status': 'success',
        'message': result
    }