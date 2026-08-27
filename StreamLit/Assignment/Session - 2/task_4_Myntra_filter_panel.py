# 4. Design a two-column Streamlit layout that mimics a Myntra filter panel: in the left column, add a dropdown to select a 
# clothing category (e.g., 'T-Shirts', 'Jeans', 'Shoes'), and in the right column, add a number input for price range. Display 
# a summary of the selected filters below the columns.


import streamlit as st

st.title("Myntra Product Panel")
col1, col2 = st.columns(2)
with col1:
    category = st.selectbox("Category", ["T-Shirts", "Jeans", "Shoes"])
with col2:
    price = st.number_input("Max Price (₹)", min_value=100, value=2000)

st.write('---')
st.subheader("Active Filters")
st.write(f'**Category:** {category}')
st.write(f'**Max Price:** ₹{price}')
