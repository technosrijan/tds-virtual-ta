## Web Framework: FastAPI

FastAPI is a modern Python web framework for building APIs with automatic interactive documentation. It's fast, easy to use, and designed for building production-ready REST APIs.

Here's a minimal FastAPI app, `app.py`:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
# ]
# ///

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run this with `uv run app.py`.

1. **Handle errors by raising HTTPException**

   ```python
   from fastapi import HTTPException

   async def get_item(item_id: int):
       if not valid_item(item_id):
           raise HTTPException(
               status_code=404,
               detail=f"Item {item_id} not found"
           )
   ```

2. **Use middleware for logging**

   ```python
   from fastapi import Request
   import time

   @app.middleware("http")
   async def add_timing(request: Request, call_next):
       start = time.time()
       response = await call_next(request)
       response.headers["X-Process-Time"] = str(time.time() - start)
       return response
   ```

Tools:

- FastAPI CLI: Project scaffolding
- Pydantic: Data validation
- SQLModel: SQL databases
- FastAPI Users: Authentication

Watch this FastAPI Course for Beginners (64 min):

[](https://youtu.be/tLKKmouUams)