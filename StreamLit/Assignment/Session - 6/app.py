import streamlit as st
import pandas as pd
import requests

st.title("Ultimate Trending Movies Dashboard")
st.write("Here are some trending movies currently topping the charts:")


movies_data = [
    {"Title": "Inception", "Genre": "Sci-Fi", "Rating": 8.8, "Year": 2010},             # Dummy data simulating a JSON response from an API request
    {"Title": "The Dark Knight", "Genre": "Action", "Rating": 9.0, "Year": 2008},
    {"Title": "Interstellar", "Genre": "Sci-Fi", "Rating": 8.6, "Year": 2014},
    {"Title": "Dune: Part Two", "Genre": "Sci-Fi", "Rating": 8.9, "Year": 2024},
    {"Title": "Oppenheimer", "Genre": "Biography", "Rating": 8.4, "Year": 2023}
]

df = pd.DataFrame(movies_data)
st.dataframe(df)