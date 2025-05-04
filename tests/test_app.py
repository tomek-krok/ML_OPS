import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

from fastapi.testclient import TestClient

client = TestClient(app.app)


def test_welcome_root():
    assert app.welcome_root() == {"message": "Welcome to the ML API"}


def test_health_check():
    assert app.health_check() == {"status": "ok"}


def test_predict_setosa():
    data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }

    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json()["prediction"] == "Setosa"


def test_predict_versicolor():
    data = {
        "sepal_length": 6.4,
        "sepal_width": 3.5,
        "petal_length": 4.5,
        "petal_width": 1.2,
    }

    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json()["prediction"] == "Versicolor"


def test_predict_virginica():
    data = {
        "sepal_length": 5.9,
        "sepal_width": 3.0,
        "petal_length": 5.0,
        "petal_width": 1.8,
    }

    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json()["prediction"] == "Virginica"
