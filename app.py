from flask import Flask, render_template, request  # type: ignore
import pickle
import numpy as np  # type: ignore

# Load the trained model (placement.pkl)
with open("placement.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/predict_result', methods=['POST'])
def predict_result():
    if request.method == 'POST':
        features = [float(x) for x in request.form.values()]
        print("Received Inputs:", features)  # Debugging

        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)
        print("Model Prediction:", prediction)  # Debugging

        output = "Placed" if prediction[0] == 1 else "Not Placed"
        return render_template('result.html', prediction_text=f'Student Placement Prediction: {output}')

if __name__ == '__main__':
    app.run(debug=True)
