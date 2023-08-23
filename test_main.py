from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

def test_get_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Success"}

def test_hello_api():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Deta"}
