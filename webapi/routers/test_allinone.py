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

    data = response.json()

    # 期待値と比較
    expected_number = 20  # 期待されるカテゴリの数
    assert data["number"] == expected_number


def test_get_category_item_valid_id():
    response = client.get("/api/allinone/category/item?id=1")
    assert response.status_code == 200
    assert "categoryNo" in response.json()
    assert "number" in response.json()
    assert "startFrom" in response.json()
    assert "endTo" in response.json()
    assert "category" in response.json()

    data = response.json()

    # 期待値と比較
    assert data["categoryNo"] == 1
    assert data["number"] == 17
    assert data["startFrom"] == 1
    assert data["endTo"] == 17
    assert data["category"] == "01_時制"



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


    data = response.json()

    # 期待値と比較
    assert data["no"] == 1
    assert data["index"] == "[001]" 
    assert data["category"] == "01_時制"
    assert data["category_index"] == "[01]"
    assert data["englishText"] == "He grinned and said, “I make lots of money.  On weekdays I receive an average of 50 orders a day from all over the globe via the Internet.” "
    assert data["translation_slashed"] == "彼はにっこり笑った／そして言った／「私は稼いでいる・たくさんのお金を。平日に／私は受け取っている・平均で50の注文を／一日当たり／地球の至る所から／インターネット経由で」 "
    assert data["translation_natural"] == "彼はにっこり笑って「とても儲かっていますよ。平日はインターネット経由で世界中から１日平均５０件の注文があるんです」と言った。 "

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

