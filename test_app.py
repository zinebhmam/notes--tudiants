
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_accueil(client):
    response = client.get("/")
    assert response.status_code == 200

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_notes(client):
    response = client.get("/notes")
    assert response.status_code == 200
    assert len(response.json) == 2

def test_filtre_etudiant(client):
    response = client.get("/notes?etudiant=Amina")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["etudiant"] == "Amina"

def test_version(client):
    response = client.get("/health")
    assert response.json["version"] == "1.0"
