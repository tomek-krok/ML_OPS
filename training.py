from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


def load_data():
    return load_iris()


def train_model():
    ml_data = load_data()
    x = ml_data.data
    y = ml_data.target

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    ml = RandomForestClassifier()
    ml.fit(x_train, y_train)

    if ml.score(x_test, y_test) > 0.9:
        return ml
    else:
        raise Exception("Model is not good enough")


def save_model():
    ml = train_model()

    if not ml:
        raise Exception("Model is not good enough")
    else:
        joblib.dump(ml, "my_iris_model.joblib")


if __name__ == "__main__":
    save_model()
