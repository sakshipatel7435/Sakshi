
# Testing the Flask API

To satisfy Task 5, here are the exact instructions to run and test your new Flask Prediction API locally.

### Step 1: Run the Server
Open your terminal inside the `Session_3` folder and start the app:
```powershell
python app.py
```
*(The server will start running at `http://127.0.0.1:5000`)*

### Step 2: Test the Root Endpoint (Task 1)
Open a new, separate terminal and run this curl command to see the welcome message:
```powershell
curl http://127.0.0.1:5000/
```

### Step 3: Test the Price Predictor (Task 2)
Send a POST request with JSON to calculate a discounted price:
```powershell
curl -X POST http://127.0.0.1:5000/predict-price -H "Content-Type: application/json" -d '{"base_price": 500, "discount": 20}'
```

### Step 4: Test the Delivery Predictor (Tasks 3 & 4)
Send a POST request with distance (km) and order size (items) to get the machine-learning predicted delivery time and the custom Swiggy-style message:
```powershell
curl -X POST http://127.0.0.1:5000/predict-delivery -H "Content-Type: application/json" -d '{"distance": 4.5, "order_size": 2}'
```