import os
import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import tensorflow as tf

st.set_page_config(
    page_title="Food Delivery Intelligence Platform",
    layout="wide",
)

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to", ["Home", "Data Explorer", "Demand Predictor", "Model Info"]
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "demand_model.keras")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# 1. Home Page
if page == "Home":
  st.title("Food Delivery Intelligence Platform")
  st.markdown("""
    Welcome to the operational intelligence platform. Use the sidebar to:
    - **Data Explorer**: Explore delivery logistics data and view interactive distributions.
    - **Demand Predictor**: Run real-time ANN demand predictions for order volume.
    - **Model Info**: Inspect artificial neural network model architecture and layer metadata.
    """)

  

# 2. Data Explorer Page
elif page == "Data Explorer":
  st.title("Data Explorer")
  uploaded_file = st.file_uploader("Upload Delivery CSV", type=["csv"])

  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip().str.lower()

    # Metric Cards
    col1, col2, col3 = st.columns(3)

    total_orders = len(df)
    col1.metric("Total Orders", f"{total_orders:,}")

    if "delivery_time" in df.columns:
      avg_del_time = df["delivery_time"].mean()
      col2.metric("Avg Delivery Time", f"{avg_del_time:.1f} min")
    else:
      col2.metric("Avg Delivery Time", "N/A")

    if "revenue" in df.columns:
      total_rev = df["revenue"].sum()
      col3.metric("Total Revenue", f"₹{total_rev:,.2f}")
    else:
      col3.metric("Total Revenue", "N/A")

    st.markdown("---")

    if "delivery_time" in df.columns:
      fig1 = px.histogram(
          df,
          x="delivery_time",
          title="Delivery Time Distribution",
          labels={"delivery_time": "Delivery Time (minutes)"},
      )
      st.plotly_chart(fig1, use_container_width=True)

    if "restaurant" in df.columns and "delivery_time" in df.columns:
      fig2 = px.box(
          df,
          x="restaurant",
          y="delivery_time",
          title="Delivery Time Distribution by Restaurant",
          labels={
              "restaurant": "Restaurant",
              "delivery_time": "Delivery Time (min)",
          },
      )
      st.plotly_chart(fig2, use_container_width=True)

  else:
    st.warning("Please upload a CSV file to proceed.")



# 3. Demand Predictor Page
elif page == "Demand Predictor":
  st.title("Real-Time Demand Predictor")

  @st.cache_resource
  def load_prediction_assets():
    if not os.path.exists(MODEL_PATH):
      raise FileNotFoundError(
          f"Model file 'demand_model.keras' not found at path: {MODEL_PATH}"
      )

    model = tf.keras.models.load_model(MODEL_PATH)

    scaler = None
    if os.path.exists(SCALER_PATH):
      scaler = joblib.load(SCALER_PATH)

    return model, scaler

  try:
    model, scaler = load_prediction_assets()

    hour = st.slider("Hour of Day", 0, 23, 12)
    day = st.selectbox(
        "Day of Week",
        range(7),
        format_func=lambda x: [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun",
        ][x],
    )
    temp = st.number_input("Temperature (°C)", 10.0, 45.0, 25.0, step=0.5)

    if st.button("Predict Demand", type="primary"):
      raw_inputs = np.array([[hour, day, temp]])

      # Scale inputs if a fitted scaler is available
      if scaler is not None:
        model_inputs = scaler.transform(raw_inputs)
      else:
        model_inputs = raw_inputs

      probs = model.predict(model_inputs)[0]
      classes = ["Low", "Medium", "High"]
      pred_index = np.argmax(probs)
      pred_label = classes[pred_index]

      st.success(
          f"Predicted Demand: **{pred_label}** ({probs[pred_index]*100:.1f}%"
          " confidence)"
      )

      fig = px.bar(
          x=classes,
          y=probs,
          labels={"x": "Demand Category", "y": "Probability"},
          title="Model Class Confidence Scores",
          range_y=[0, 1],
      )
      st.plotly_chart(fig, use_container_width=True)

  except Exception as e:
    st.error(
        f"Model Error: {e}\n\nPlease run your model training script"
        " ('python task3_train.py') to save 'demand_model.keras' and"
        " 'scaler.pkl'."
    )



# 4. Model Info Page
elif page == "Model Info":
  st.title("Model Architecture & History")

  try:
    if not os.path.exists(MODEL_PATH):
      st.error(
          "File not found: `demand_model.keras`. Please run 'python"
          " task3_train.py' first!"
      )
    else:
      model = tf.keras.models.load_model(MODEL_PATH)

      summary_data = []
      model.summary(print_fn=lambda x: summary_data.append(x))

      st.subheader("Model Summary")
      st.code("\n".join(summary_data), language="text")

  except Exception as e:
    st.error(f"Error loading model metadata: {e}")