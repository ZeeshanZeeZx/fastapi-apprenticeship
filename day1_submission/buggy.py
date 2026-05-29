from fastapi import FastAPI

app = FastAPI()

# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     return {"user_id": user_id}

# @app.get("/users/me")
# async def read_current_user():
#     return {"username": "the current user"}


## wrong dynamic path is writter before the static path, so the static path will never be reached
@app.get("/users/me")
async def read_current_user():
    return {"username": "the current user"}

@app.get("/users/me/items")
def read_user_items():
    return [{"item_id": "Foo"}, {"item_id": "Bar"}]

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}


