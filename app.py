from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

try:
    model = pickle.load(open('model/log_model.pkl', 'rb'))
    scaler = pickle.load(open('model/Std_scalar.pkl', 'rb'))
except Exception as e:
    print(f"Error loading model or scaler: {e}")

def make_prediction(input_values):
    try:
        scaled_input = scaler.transform([[
            input_values['Pregnancies'],
            input_values['Glucose'],
            input_values['blood_pressure'],
            input_values['skin_thickness'],
            input_values['insulin'],
            input_values['bmi'],
            input_values['diabetes_pedigree_function'],
            float(input_values['age']),
        ]])
        prediction = model.predict(scaled_input)
        return True, prediction[0]
    except Exception as e:
        return False, str(e)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    print(input_data)
    prediction_result, prediction = make_prediction(input_data)
    if prediction_result:
        print({'Model Predicted' :prediction})
        prediction_result = 'Diabetes' if prediction == 1 else 'no Diabetes'
        return jsonify({'result': prediction_result}), 200
    else:
        return jsonify({'error': prediction}), 400

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)