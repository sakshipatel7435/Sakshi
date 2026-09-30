import streamlit as st
import PyPDF2

st.set_page_config(page_title="PDF Chatbot", page_icon="📄")
st.title("📄 Simple PDF Text Extractor")
st.write("Upload a PDF document (like a college timetable or IRCTC ticket) and extract its text!")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() + "\n"
            
        st.success("Text Successfully Extracted!")
        
        st.subheader("Extracted Document Text:")
        st.text_area("PDF Content", text, height=300)
        
    except Exception as e:
        st.error(f"Error reading PDF: {e}") 