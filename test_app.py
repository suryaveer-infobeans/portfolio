import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200

def test_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200

def test_projects_page(client):
    response = client.get("/projects")
    assert response.status_code == 200

def test_contact_page(client):
    response = client.get("/contact")
    assert response.status_code == 200
