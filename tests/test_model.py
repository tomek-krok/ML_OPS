import sys
import os
from sklearn.ensemble import RandomForestClassifier

import model_classifier


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_model():
    model = model_classifier.load("my_iris_model.joblib")
    assert isinstance(model, RandomForestClassifier)


def test_predict_setosa():
    model = model_classifier.load("my_iris_model.joblib")
    assert model_classifier.predict(model, 5.1, 3.5, 1.4, 0.2) == "Setosa"


def test_predict_versicolor():
    model = model_classifier.load("my_iris_model.joblib")
    assert model_classifier.predict(model, 6.4, 3.5, 4.5, 1.2) == "Versicolor"


def test_predict_virginica():
    model = model_classifier.load("my_iris_model.joblib")
    assert model_classifier.predict(model, 5.9, 3.0, 5.0, 1.8) == "Virginica"
