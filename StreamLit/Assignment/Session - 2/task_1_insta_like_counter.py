# 1. Create a Streamlit app called insta_like_counter.py that shows a button labeled 'Like' and a counter displaying how many times the 
# button has been clicked, similar to Instagram's like feature.

import streamlit as st

st.title("Instagram Like Counter")

if "likes" not in st.session_state:
    st.session_state.likes = 0
if st.button("Like"):
    st.session_state.likes += 1
st.write(f"**Total Likes:** {st.session_state.likes}")