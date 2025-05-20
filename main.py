from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello {name}!"}
