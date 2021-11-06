from flask import Flask, render_template, request, url_for
from model import predict_iris_sort

app = Flask(__name__)


@app.route('/')
def index():
    """Render main page."""
    return render_template('index.html')


@app.route('/predict', methods=["POST"])
def predict():
    """Predict iris sort with AI model and return response to user."""
    if request.method == 'POST':
        data = request.get_json(force=True)
        iris_props = data["payload"]
        iris_sort = predict_iris_sort(iris_props)

        if iris_sort:
            return dict(payload=iris_sort)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
