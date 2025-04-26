from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Health Information System is running"}

def test_create_program():
    response = client.post(
        "/programs/",
        json={"name": "HIV Treatment"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "HIV Treatment"

def test_create_client():
    response = client.post(
        "/clients/",
        json={"name": "John Doe", "email": "john@example.com", "phone": "0712345678"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_clients():
    response = client.get("/clients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_enroll_client_in_program():
    # Assuming client with ID 1 and program with ID 1 exist
    response = client.post("/clients/1/enroll/1")
    assert response.status_code == 200
    assert "programs" in response.json()
