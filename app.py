from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))  # Load trained model

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        humidity = float(request.form['humidity'])
        pressure = float(request.form['pressure'])
        temperature = float(request.form['temperature'])

        input_features = np.array([[humidity, pressure, temperature]])
        prediction = model.predict(input_features)[0]

        result = "Windstorm Expected 🌪️" if prediction == 1 else "No Windstorm 🚫"
        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
