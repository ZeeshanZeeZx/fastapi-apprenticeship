from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

@app.get("/sync")
def sync_endpoint():
    """This endpoint is inefficient because it uses a blocking call (time.sleep) in a synchronous function. When this endpoint is called, it will block the entire server for 2 seconds, preventing it from handling any other requests during that time."""
    time.sleep(2)
    return {"msg": "sync done"}

@app.get("/async_good")
async def async_good():
    """This endpoint is efficient because it is fully asynchronous. The function uses async def, and the delay is handled using await asyncio.sleep(), which is non-blocking. This allows the event loop to handle other requests while waiting, enabling better concurrency."""
    await asyncio.sleep(2)
    return {"msg": "async good done"}

@app.get("/async_bad")
def async_bad():
    """This endpoint is inefficient because it uses a blocking call (time.sleep) in a synchronous function. When this endpoint is called, it will block the entire server for 2 seconds, preventing it from handling any other requests during that time."""
    time.sleep(2)
    return {"msg": "async bad done"}