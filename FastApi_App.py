from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app=FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "message": f"Fetching user with ID {user_id} with thier name !"}

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

    
class Item(BaseModel):
        name: str
        description: str | None = None
        price: float
        tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
        return item
    
if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)
