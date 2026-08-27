# 5. Enhance any one of your previous Streamlit apps by moving all input components (text input, number input, sliders, dropdowns,
# radio buttons) into the sidebar using st.sidebar, and keep the results or outputs on the main page.<br><br><em><strong>Hint:</strong> 
# Use st.sidebar.[component] instead of st.[component] for all inputs.</em>


import streamlit as st

st.title("Zomato Order Feedback")
st.sidebar.header("Rate Your Order")
rating = st.sidebar.slider("Rating (1 to 5 Stars):", min_value=1, max_value=5, value=5)
food_type = st.sidebar.radio("Food Type:", options=["Veg", "Non-Veg"])
submit = st.sidebar.button("Submit Feedback")

if submit:
    st.success("Feedback Received!")
    st.write(f"**Meal Type:** {food_type}")
    st.write(f"**Rating:** {'⭐' * rating} ({rating}/5)")
else:
    st.write("Please select your order details in the sidebar and click **Submit Feedback**.")