# main.py
import yaml

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from webapi.routers import allinone
from webapi.routers import gpttemplate

app = FastAPI()

with open("./config.yaml", "r") as config_file:
    """
    config.yamlからoriginsを読み込む
    ## config.yamlのサンプル
    origins:
    - "http://localhost"
    - "http://localhost:3000"
    - "https://react-aio-typing-27586.web.app"
    ...
    """
    config = yaml.full_load(config_file)
    origins = config["origins"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_index():
    """_for access check_

    Returns:
        dict: { "message": "Success" }
    """
    return {"message": "Success"}

@app.get("/api/")
def hello_api():
    """_for access check_

    Returns:
        dict: { "message": "<hello message>" }
    """
    return {"message": "Welcome to Deta"}

# append apis
app.include_router(allinone.router)
app.include_router(gpttemplate.router)

