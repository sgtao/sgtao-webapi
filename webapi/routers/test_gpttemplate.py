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

def test_create_prompt_invalid_item():
    invalid_item = {
        "type": "invalid_type",
        "data01": "This is some data."
    }
    response = client.post("/api/gpttemplate/prompt/", json=invalid_item)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "not supported" in response.json()["message"]

def test_create_prompt_undefined_item_type():
    valid_item = {
        "type": "999_undefined",
        "data01": "This is some data."
    }
    response = client.post("/api/gpttemplate/prompt/", json=valid_item)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "not supported" in response.json()["message"]


def test_create_prompt_valid_item011():
    valid_item = {
        "type": "011_summarise",
        "data01": "This is some data."
    }
    response = client.post("/api/gpttemplate/prompt/", json=valid_item)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "prompt" in response.json()


def test_create_prompt_valid_item012():
    valid_item = {
        "type": "012_questionanswering",
        "data01": "This is 1st data.",
        "data02": "This is 2nd data."
    }
    response = client.post("/api/gpttemplate/prompt/", json=valid_item)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "prompt" in response.json()

