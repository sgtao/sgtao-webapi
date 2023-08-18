from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_index():
    return {"message": "Success"}

@app.get("/api/")
def hello_api():
    return {"message": "Welcome to Deta"}
