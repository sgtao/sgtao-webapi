# main.py
from fastapi import FastAPI
from webapi.routers import allinone

app = FastAPI()

@app.get("/")
def get_index():
    return {"message": "Success"}

@app.get("/api/")
def hello_api():
    return {"message": "Welcome to Deta"}

# append apis
app.include_router(allinone.router)

