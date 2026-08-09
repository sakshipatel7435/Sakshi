### Task 4: Streamlit Deep Learning Inference App
# Integrate the trained Keras demand classification model from Task 3 into a Streamlit interface, combining Module 8 UI patterns with Module 9 neural network inference into a single deployable app. (Integrative — Streamlit + Keras + Plotly across both modules.)
# Requirement 1 — Save the trained model from Task 3 using model.save('demand_model.keras') and load it in a new Streamlit app using tf.keras.models.load_model(), wrapped in st.cache_resource.
# Requirement 2 — Add input widgets for hour of day (slider, 0–23), day of week (selectbox, Monday–Sunday encoded as 0–6), and temperature in °C (number input, range 10–45).
# Requirement 3 — On a Predict Demand button click, assemble and reshape the input into a (1, 3) NumPy array, pass it through the loaded model, and display the predicted demand class (Low / Medium / High) with the associated confidence percentage using st.success() or st.warning() depending on the class.
# Requirement 4 — Display a Plotly bar chart showing the raw probability scores for all three demand classes (Low, Medium, High) so dispatchers can visually assess model confidence alongside the final prediction.



import streamlit as st
import tensorflow as tf
import numpy as np
import plotly.express as px

st.title("Demand Prediction App")



@st.cache_resource              # Req 1
def load_keras_model():
    return tf.keras.models.load_model('demand_model1.keras') 

try:
    model = load_keras_model()
    
  
    hour = st.slider("Hour of Day", 0, 23, 12)                                    # Req 2: Inputs
    day_map = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
    day_str = st.selectbox("Day of Week", list(day_map.keys()))
    temp = st.number_input("Temperature (°C)", min_value=10.0, max_value=45.0, value=25.0)

    
    if st.button("Predict Demand"):                           # Req 3
        features = np.array([[hour, day_map[day_str], temp]])
        probs = model.predict(features)[0]
        
        classes = ["Low", "Medium", "High"]
        pred_idx = np.argmax(probs)
        pred_class = classes[pred_idx]
        confidence = probs[pred_idx] * 100
        
        if pred_class == "High":
            st.warning(f"Predicted Demand: {pred_class} ({confidence:.1f}% confidence)")
        else:
            st.success(f"Predicted Demand: {pred_class} ({confidence:.1f}% confidence)")
            
        
        fig = px.bar(x=classes, y=probs, labels={'x':'Demand Tier', 'y':'Probability'},       # Req 4: Plotly Probability Chart
                     title="Model Class Probabilities", range_y=[0, 1])
        st.plotly_chart(fig)

except Exception as e:
    st.error(f"Failed to load model: {e}")