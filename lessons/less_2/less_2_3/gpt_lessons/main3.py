from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

app = FastAPI()

class Numbers(BaseModel):
    num1: int
    num2: int

@app.get("/")
async def root():
    return FileResponse('index3.html')

@app.post("/api/calculate")
async def plus_numbers(data: Numbers):
    return {"result": data.num1 + data.num2}