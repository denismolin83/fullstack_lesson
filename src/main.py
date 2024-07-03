from fastapi import FastAPI

app = FastAPI()

@app.get("/cry")
def read_root():
    return {"Hello": "World"}