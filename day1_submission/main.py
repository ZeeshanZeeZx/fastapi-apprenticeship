from fastapi import FastAPI
from typing import Optional
import time
import asyncio  

app = FastAPI()

@app.get("/")
def get_method():
    time.sleep(1)
    return {"message": "Welcome to My API."}

@app.get("/health")
async def health_check():
    await asyncio.sleep(1)
    return {"status": "OK"}

@app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
def read_item(item_id: int, q: str):
    # data = MyModel.obj.get(id=item_id)
    # return {"item_id":  data[item_id], "description": f"Item {data[item_id]} details"}
    response = {"item_id":  item_id, "description": f"Item {item_id} details"}
    if q:
        response["query"] = q
    return response
