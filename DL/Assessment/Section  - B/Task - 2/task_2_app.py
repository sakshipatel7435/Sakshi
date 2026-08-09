### Task 2: Delivery Time Prediction UI

# Requirement 1 — Load a saved model file named delivery_model.pkl using joblib, wrapped inside a function decorated with st.cache_resource so the model is loaded only once per session.
# Requirement 2 — Create input widgets for: distance (slider, 1–50 km), order value in Rs (number input), and time of day (selectbox with options: Morning, Afternoon, Evening, Night).
# Requirement 3 — On a Predict Delivery Time button click, encode the time-of-day selection as an integer (0–3), assemble the feature array, pass it to the loaded model, and display the predicted delivery time in minutes using st.success().
# Requirement 4 — Handle any ValueError or model file load failure gracefully using a try-except block, displaying a descriptive st.error() message without crashing the app.



import streamlit as st
import joblib
import numpy as np

st.title("Delivery Time Predictor")


@st.cache_resource                              # Req 1
def load_model():
    return joblib.load('delivery_model.pkl')

try:
    model = load_model()
    
   
    distance = st.slider("Distance (km)", 1, 50, 5)                         # Req 2: Input widgets
    order_value = st.number_input("Order Value (₹)", min_value=0.0, value=250.0)
    time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
    
    
    if st.button("Predict Delivery Time"):                                  # Req 3: Inference
        time_map = {"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3}
        features = np.array([[distance, order_value, time_map[time_of_day]]])
        
        prediction = model.predict(features)[0]
        st.success(f"Estimated Delivery Time: {prediction:.1f} minutes")

except Exception as e: # Req 4
    st.error(f"Error loading model file 'delivery_model.pkl': {e}")