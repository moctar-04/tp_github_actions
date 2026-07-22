import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from app import app
 
@pytest.fixture
def client():
    return app.test_client()
 
def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok c'est bien"}
 
def test_add(client):
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 5}