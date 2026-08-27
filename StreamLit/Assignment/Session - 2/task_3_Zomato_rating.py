# 3. Create a Streamlit app that lets users rate their last Zomato order: use a slider to select a rating from 1 to 5 stars, and radio buttons 
# to choose between 'Veg' or 'Non-Veg'. When submitted, show a message summarizing their feedback.<br><br><em><strong>Hint:</strong> Use st.slider 
# for the rating and st.radio for the food type selection.</em>

import streamlit as st

st.title("Zomato Order Rating")
rating = st.slider("Rate your last order (1 to 5 Stars):", min_value=1, max_value=5, value=5)
food_type = st.radio("Food Type:", options=["Veg", "Non-Veg"])

if st.button("Submit Feedback"):
    st.info(f"Thank you for your feedback! You rated your **{food_type}** meal **{rating}/5 stars**.")