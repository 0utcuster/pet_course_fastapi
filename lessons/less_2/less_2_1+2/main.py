from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/calculate")
def plus_numbers(a: int, b: int):
    return {"result":a+b}

class Product(BaseModel):
    title: str
    price: float

@app.post("/product")
def create_product(product: Product):
    return {
        "ok": True,
        "product": product
    }

@app.get("/")
def say_hello():
    return {"message": "hello"}



@app.get("/file2")
async def root():
    return FileResponse('public/index.html')