from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "World"}


@app.get('/ping')
def get_ping():
    return {"message": "pong"}
