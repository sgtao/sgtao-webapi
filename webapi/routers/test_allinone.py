# test_allinone.py
from fastapi.testclient import TestClient
from fastapi import HTTPException
from webapi.routers import allinone
import pytest

client = TestClient(allinone.router)

def test_get_allinone():
    response = client.get("/api/allinone/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello from allinone."}

def test_get_aio_category():
    response = client.get("/api/allinone/category")
    assert response.status_code == 200
    assert "number" in response.json()
    assert "categories" in response.json()

def test_get_category_item_valid_id():
    response = client.get("/api/allinone/category/item?id=1")
    assert response.status_code == 200
    assert "categoryNo" in response.json()
    assert "number" in response.json()
    assert "startFrom" in response.json()
    assert "endTo" in response.json()
    assert "category" in response.json()

def test_get_category_item_negative_id():
    with pytest.raises(HTTPException) as exc_info:
        response = client.get("/api/allinone/category/item?id=-1")
    
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "id is out ob range"


def test_get_num_contents():
    response = client.get("/api/allinone/contents")
    assert response.status_code == 200
    assert "number" in response.json()

def test_get_aio_item_valid_id():
    response = client.get("/api/allinone/contents/item?id=1")
    assert response.status_code == 200
    assert "no" in response.json()
    assert "index" in response.json()
    assert "category" in response.json()
    assert "category_index" in response.json()
    assert "englishText" in response.json()
    assert "translation_slashed" in response.json()
    assert "translation_natural" in response.json()


def test_get_aio_item_invalid_id():
    with pytest.raises(HTTPException) as exc_info:
        response = client.get("/api/allinone/contents/item?id=1000")
    
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "id is out ob range"


def test_get_aio_item_negative_id():
    with pytest.raises(HTTPException) as exc_info:
        response = client.get("/api/allinone/contents/item?id=-1")
    
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "id is out ob range"

