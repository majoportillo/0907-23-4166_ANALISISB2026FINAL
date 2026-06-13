import pytest
from fastapi.testclient import TestClient
from main import app, get_db
from database import Base, engine

# Usamos una base de datos en memoria para pruebas
client = TestClient(app)

def test_crear_incidente():
    payload = {
        "descripcion": "Fallo en antena de Jalapa",
        "severidad": "Critica"
    }
    response = client.post("/incidentes/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["descripcion"] == "Fallo en antena de Jalapa"
    assert "id" in data

def test_listar_incidentes():
    response = client.get("/incidentes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)