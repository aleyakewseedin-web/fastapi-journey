from fastapi import FastAPI
from database.connection import initialize_database, settings 
from routes.users import user_router
from routes.events import Event_router
app = FastAPI(
 title="Event Management API",
 description="An API for managing events and users built with FastAPI and Beanie.",
 version="1.0.0"
)
app.include_router(Event_router)
app.include_router(user_router)

@app.on_event("startup")
async def startup_event():
    await initialize_database(settings) 





