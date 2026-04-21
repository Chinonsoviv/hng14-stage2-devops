import os
import sys
from fastapi.testclient import TestClient

# Path fix
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    # We only care that the API responds with 'healthy'
    assert response.json()["status"] == "healthy"

def test_basic_math():
    assert 1 + 1 == 2