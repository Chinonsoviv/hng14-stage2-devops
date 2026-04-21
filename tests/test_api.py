from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_basic():
    assert 2 + 2 == 4
    