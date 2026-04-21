import sys
import os

# 👇 FORCE project root into Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_basic():
    assert 2 + 2 == 4