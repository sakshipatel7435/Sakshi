from flask import Flask, request, jsonify
import joblib
import numpy as np
app = Flask(__name__)
delivery_model = joblib.load('delivery_model.joblib')

@app.route('/')
def home():
    return 'Welcome to the Prediction API'

@app.route('/predict-price', methods=['POST'])
def predict_price():
    data = request.get_json()
    base_price = data.get('base_price', 0)
    discount = data.get('discount', 0)
    final_price = base_price - base_price * discount / 100
    return jsonify(
        {
            "base_price": base_price,
            "discount": discount,
            "final_price": final_price,
        }
    )

@app.route('/predict-delivery', methods=['POST'])
def predict_delivery():
    data = request.get_json()
    distance = data.get('distance', 0)
    order_size = data.get('order_size', 0)
    features = np.array([[distance, order_size]])
    prediction = delivery_model.predict(features)[0]
    estimated_time = round(prediction, 1)
    return jsonify({'estimated_time_minutes': estimated_time, 'message': f'Hang tight! Your delicious food will be at your door in approximately {estimated_time} minutes.'})
if __name__ == '__main__':
    app.run(debug=True, port=5000)