from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

app = FastAPI()

class Numbers(BaseModel):
    num1: int
    num2: int

@app.get("/")
async def root():
    return FileResponse('templates/index.html')

@app.post("/api/calculate")
async def plus_numbers(data: Numbers):
    return {"result": data.num1 + data.num2}

# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


# @app.post("/api/calculate")
# async def calculate(num1: float, num2: float):
#     return {"result": num1 + num2}



