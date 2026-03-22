
from fastapi import FastAPI
from enrollment import enrollment
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates") 
app= FastAPI()  
@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to the enrollment API"}

app.include_router(enrollment)
