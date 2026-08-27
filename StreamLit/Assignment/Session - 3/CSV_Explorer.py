import streamlit as st
import pandas as pd


# Task 1
st.title("CSV Data Viewer & Analyzer")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.divider()
    st.header("1. Complete Dataset")
    st.dataframe(df)
    st.divider()

### Task 2
    st.header("2. Top 10 Rows & Dimensions")
    st.dataframe(df.head(10))
    rows, cols = df.shape
    st.write(f"**Total Rows:** {rows} | **Total Columns:** {cols}")
    st.divider()

### Task 3
    st.header("3. View Single Column")
    selected_column = st.selectbox("Select a column to display:", options=df.columns)
    st.dataframe(df[[selected_column]])
    st.divider()

### Task 4
    st.header("4. Search Dataset")
    search_term = st.text_input("Enter a search term:")
        
    if search_term:
        mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)
        filtered_df = df[mask]
        st.subheader(f"Search Results for '{search_term}' ({len(filtered_df)} rows found)")
        st.dataframe(filtered_df)
    else:
        st.dataframe(df)

else:
    st.info("Please upload a CSV file above to start analyzing your data.")