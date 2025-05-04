from joblib import load


def load_model():
    return load("my_iris_model.joblib")


def predict(model, f1, f2, f3, f4):
    """
    Predicts the type of iris flower based on four features: sepal width,
    sepal length, petal width, and petal length.

    The function uses a pre-trained RandomForestClassifier model to predict
    the type of iris flower. The model is loaded using the `iris_load_model()`
    function. The prediction is based on the input features provided.

    Parameters:
    f1 (float): Sepal width.
    f2 (float): Sepal length.
    f3 (float): Petal width.
    f4 (float): Petal length.

    Returns:
    str: The name of the predicted iris flower. It can be either "Setosa",
    "Versicolor", or "Virginica".
    """
    flower = model.predict([[f1, f2, f3, f4]])

    flower_name = "Not categorized"

    flower = flower[0]
    if flower == 0:
        flower_name = "Setosa"
    elif flower == 1:
        flower_name = "Versicolor"
    elif flower == 2:
        flower_name = "Virginica"

    return flower_name
