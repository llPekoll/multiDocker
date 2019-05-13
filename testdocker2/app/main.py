from fastapi import FastAPI

app = FastAPI()

print("ils didannent comme de la police")
@app.get("/")
def read_root():
    return {"Hello": "World fom dock2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}