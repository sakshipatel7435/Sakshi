from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
app = Flask(__name__)
CORS(app)
with open('review_sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get('review', '')
    prediction = model.predict([review])[0]
    return jsonify({'prediction': prediction})
if __name__ == '__main__':
    app.run(debug=True, port=5000)