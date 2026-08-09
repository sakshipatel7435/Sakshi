### Task 1: Delivery Summary Dashboard

# Build a Streamlit app that reads an uploaded food delivery CSV file and displays interactive business metrics with city-level filtering. (Foundational — single Streamlit data flow: upload › filter › display.)
# Requirement 1 — Add a file uploader widget that accepts a CSV file; if no file is uploaded, display a st.info() placeholder message instructing the user to upload delivery data.
# Requirement 2 — Display total orders, average delivery time (in minutes), and total revenue as three side-by-side metric cards using st.metric() with appropriate labels.
# Requirement 3 — Add a sidebar selectbox listing all unique cities found in the uploaded data; update all three metric cards to reflect only the selected city's records.
# Requirement 4 — Render a bar chart below the metric cards showing order count per restaurant for the selected city using st.bar_chart().



import streamlit as st
import pandas as pd

st.title("Delivery Summary Dashboard")

uploaded_file = st.file_uploader("Upload Delivery CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    city = st.sidebar.selectbox("Select City", df['city'].unique())
    filtered_df = df[df['city'] == city]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Orders", len(filtered_df))
    col2.metric("Avg Delivery Time (min)", round(filtered_df['delivery_time'].mean(), 1))
    col3.metric("Total Revenue (₹)", round(filtered_df['revenue'].sum(), 2))
    
    st.subheader(f"Orders per Restaurant in {city}")
    
    chart_data = filtered_df['restaurant'].value_counts()
    st.bar_chart(chart_data)
else:
    st.info("Please upload a CSV file to view dashboard metrics.")
