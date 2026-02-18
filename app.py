from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Feature names in correct order
feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

@app.route('/')
def home():
    return render_template('index.html', features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect inputs using loop
        input_features = [float(request.form[feature]) for feature in feature_names]

        final_features = np.array([input_features])
        prediction = model.predict(final_features)

        if prediction[0] == 1:
            result = "Fraud Transaction ❌"
        else:
            result = "Normal Transaction ✅"

        return render_template('index.html',
                               prediction_text=result,
                               features=feature_names)

    except:
        return render_template('index.html',
                               prediction_text="Invalid Input!",
                               features=feature_names)

if __name__ == "__main__":
    app.run(debug=True)
