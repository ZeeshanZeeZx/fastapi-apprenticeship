# Route Ordering Analysis (FastAPI)

## 1. Error message

When accessing `/users/me`, the response was:

```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["path", "user_id"],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "me"
    }
  ]
}

2. Why /users/me was routed incorrectly
FastAPI matches routes in the order they are defined.

Since /users/{user_id} was defined before /users/me, the request /users/me was matched against:
/users/{user_id}

So FastAPI treated "me" as the value of user_id and tried to convert it to an integer, which caused a validation error.

3. Why Swagger UI did not show an error
Swagger UI only reflects the OpenAPI schema, not runtime routing behavior.

It:
- Shows available endpoints
- Shows parameter types
- Marks required fields

But it does NOT:
- Simulate route matching order
- Detect conflicts between static and dynamic routes
- Validate actual request routing behavior

So everything looks correct in Swagger even though runtime routing can fail.

4. Fix applied
The fix is to define static routes before dynamic routes.

After fixing, the order is:
@app.get("/users/me")
def read_current_user():
    return {"user": "current user"}


@app.get("/users/me/items")
def read_user_items():
    return {"items": []}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

5. Final behavior after fix
/users/me → handled correctly by read_current_user
/users/me/items → handled correctly by read_user_items
/users/123 → handled by read_user

No routing conflicts occur.

Key takeaway
Static routes must always be defined before dynamic path parameters to avoid greedy matching issues.

