##In `database/connection.py`:

##Use **Pydantic's `BaseSettings`** to read `DATABASE_URL` from a `.env` file
 ##Implement an `initialize_database()` async method using `init_beanie`
## Implement a `Database` class that wraps CRUD operations for any document model
##The `Database` class must implement these methods:

## Method | Description |
##-------|-------------|
##`save(document)` | Insert a new document |
##`get(id)` | Retrieve one document by ID |
##`get_all()` | Retrieve all documents |
##`update(id, body)` | Update a document by ID |
##`delete(id)` | Delete a document by ID |



 
# database/connection.py
from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any, Optional
from pydantic_settings import BaseSettings
from pydantic import  BaseModel
from models.users import User
from models.events import Event

class Settings(BaseSettings):
    DATABASE_URL: Optional[str]
    
    class Config:
        env_file = ".env"
client: Optional[AsyncIOMotorClient] = None
db: Optional[Any] = None
# Define the async function separately
async def initialize_database(self):
        
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(),
            document_models=[Event, User]
        )
        print("✅ MongoDB connected and Beanie initialized!")

settings=Settings()

class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document: BaseModel):
        await document.create()

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> list[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        des_body = body.dict()
        des_body = {k: v for k, v in des_body.items() if v is not None}

        update_query = {
            "$set": {field: value for field, value in des_body.items()}
        }

        doc = await self.get(id)
        if not doc:
            return False

        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
    

