``` 
pip install fastapi
``` 
``` 
pip install "uvicorn[standard]"
``` 
Create a file main.py with:
``` 
from typing import Union
 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
 
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

``` 

### Run the server with:
``` 
uvicorn main:app --reload
``` 

### Check it
Open your browser at http://127.0.0.1:8000/items/5?q=somequery.

### You will see the JSON response as:
``` 
{"item_id": 5, "q": "somequery"}
``` 
### Interactive API docs
Now go to http://127.0.0.1:8000/docs