If you write:

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q}

FastAPI treats q as a required query parameter, so it must be passed in the URL query string:

/items/1?q=value


How Swagger UI shows it
In FastAPI Swagger UI:
q appears under Query Parameters
It is marked with a red asterisk (*)
It is labeled as required
The input box is empty and mandatory

So Swagger clearly indicates:

“You must provide this field before executing the request”

3. Curl request example
curl "http://127.0.0.1:8000/items/1?q=hello"

4. What happens if q is missing
Request:
curl "http://127.0.0.1:8000/items/1"
Response:
{
  "detail": [
    {
      "type": "missing",
      "loc": ["query", "q"],
      "msg": "Field required",
      "input": null
    }
  ]
}
HTTP status code:
422 Unprocessable Entity
One-line interview answer

If a parameter is not in the path and has no default value, FastAPI treats it as a required query parameter, shows it as mandatory in Swagger UI, requires it in the URL query string, and returns a 422 validation error if it is missing.