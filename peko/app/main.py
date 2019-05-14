from fastapi import FastAPI

app = FastAPI()

print("i think the server is running!")
@app.get("/")
def read_root():
    return {"Hello": "World fom doc1"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}