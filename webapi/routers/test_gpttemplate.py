# test_gpttemplate.py
from fastapi.testclient import TestClient
from fastapi import HTTPException
from webapi.routers import gpttemplate
# import pytest

client = TestClient(gpttemplate.router)

def test_get_gpttemplate():
    response = client.get("/api/gpttemplate/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello from gpttemplate."}

