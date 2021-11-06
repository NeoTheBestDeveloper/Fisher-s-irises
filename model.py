import numpy as np
from tensorflow.keras.models import load_model

IRIS_SORTS = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

model = load_model("my_model")


def to_iris_sort(iris_class):
    """Transform model output to iris sort name."""
    if iris_class not in IRIS_SORTS:
        return False
    return IRIS_SORTS[iris_class]


def predict_iris_sort(iris_props):
    """Predict iris sort."""
    iris_props = np.expand_dims(np.array(iris_props), axis=0)
    predict = model.predict(iris_props)
    iris_class = np.argmax(predict)
    iris_sort = to_iris_sort(iris_class)
    return iris_sort
