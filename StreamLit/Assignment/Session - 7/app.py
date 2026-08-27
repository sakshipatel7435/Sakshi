import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Session 7 Mini Project", page_icon="🚀", layout="wide"
)

# TASK 1
with st.expander("Task 1: Water Intake Tracker App Plan", expanded=False):
    st.markdown(
        """
    **UI Sections & Input Types:**
    - **Sidebar:** `st.number_input` (Daily Goal in mL), `st.time_input` (Reminder Window).
    - **Main Area:** `st.date_input` (Entry Date), `st.slider` (Water Intake in mL), `st.selectbox` (Beverage Type).
    
    **Charts Included:**
    1. **Bar Chart:** Daily logged intake vs Target Goal over 7 days.
    2. **Pie Chart:** Percentage split by Beverage Type.
    """
    )

st.title("Session 7 - Mini Project Dashboard")
st.divider()

### TASK 2 & TASK 4
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.header("Task 2 & 4: Flipkart Rating Analyzer")

### Task 2
    with st.sidebar:
        st.header("Flipkart Controls")
        uploaded_file = st.file_uploader(
            "Upload Product Reviews CSV", type=["csv"], key="flipkart_csv"
        )
        category = st.selectbox(
            "Select Product Category",
            ["Electronics", "Fashion", "Home & Kitchen", "Books"],
        )

    st.write(f"Active Category: **{category}**")

### Task 5
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if df.empty:
                st.warning("The uploaded CSV file is empty!")
            else:
                st.subheader("Raw Data Preview")
                st.dataframe(df.head(), use_container_width=True)
        except Exception as e:
            st.error(f"Error loading file: {e}")
    else:
        st.info(
            "Please upload a CSV file from the sidebar to view data."
        )

### Task 4
    with st.expander("Advanced Filter Options"):
        st.slider("Minimum Rating Filter", 1.0, 5.0, 3.5)
        st.checkbox("Show Verified Purchases Only")

### TASK 3
with col_right:
    st.header("🎵 Task 3: Top 5 Songs & Artist Frequency")

    artists = []
    with st.form(key="spotify_form"):
        st.write("Enter your Top 5 Favorite Songs and Artists:")
        for i in range(1, 6):
            c1, c2 = st.columns(2)
            with c1:
                st.text_input(f"Song {i}", key=f"s_{i}")
            with c2:
                art = st.text_input(f"Artist {i}", key=f"a_{i}").strip()
                if art:
                    artists.append(art)

        submit_btn = st.form_submit_button(label="Analyze Playlist")

    if submit_btn:
### Task 5
        if not artists:
            st.warning("Please enter at least one artist name!")
        else:
            artist_counts = pd.Series(artists).value_counts().reset_index()
            artist_counts.columns = ["Artist", "Count"]

            st.subheader("Artist Count Chart")
            st.bar_chart(data=artist_counts.set_index("Artist"))