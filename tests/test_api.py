import os
import sys
from fastapi.testclient import TestClient

# This adds the root directory to the python path so 'api' can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.main import app

client = TestClient(app)

def test_read_main():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200

def test_health_check():
    """Test the health endpoint (required for Docker points)"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_basic_math():
    """A simple test to ensure pytest is running"""
    assert 1 + 1 == 2