import streamlit as st
import pandas as pd
import plotly.express as px


### Task-1
st.title('Data Visualization in Streamlit')
st.title("1. Daily Step Tracker")
step_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Steps": [6500, 8200, 7800, 10500, 9100, 12300, 5400]
})
st.line_chart(data=step_data, x="Day", y="Steps")

### Task-2
st.title('2. Monthly Food Orders')
orders_data = pd.DataFrame({
    'Orders': [15, 9, 4]}, 
    index=['Zomato', 'Swiggy', "Domino's"])
st.bar_chart(orders_data)

### Task-3
st.title("3. Spotify Weekly Listening Time")
spotify_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Minutes": [45, 60, 30, 90, 120, 150, 80]
})
st.area_chart(data=spotify_data, x="Day", y="Minutes")


### Task-4
st.title("4. Daily Screen Time Breakdown")

app_usage = {
    "App": ["Instagram", "YouTube", "WhatsApp"],
    "Hours": [2.5, 3.0, 1.5]
}
fig = px.pie(
    app_usage, 
    values="Hours", 
    names="App", 
    title="Daily App Usage Share",
    hole=0.3  # Optional donut style
)
st.plotly_chart(fig)

### Task-5
st.title("5. WhatsApp Chat Activity")

whatsapp_df = pd.DataFrame({
    'messages sent': [50, 120, 80, 200, 150, 300, 250], 
    'photos shared': [2, 10, 5, 20, 15, 30, 25], 
    'calls made': [1, 3, 0, 5, 2, 4, 3]}, 
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

selected_columns = st.multiselect('Select activity metrics to visualize:', options=whatsapp_df.columns.tolist(), default=['messages sent'])
if selected_columns:
    st.line_chart(whatsapp_df[selected_columns])
else:
    st.info('Please select at least one metric to display the chart.')


