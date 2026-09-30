import streamlit as st
import requests

st.set_page_config(page_title="Insta Caption Generator", page_icon="📸")
st.title("Welcome to Insta Caption Generator! 📸")
st.write("Generate trendy, AI-powered Instagram captions in seconds.")

if "history" not in st.session_state:
    st.session_state.history = []

API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer API_KEY_HERE",
    "Content-Type": "application/json"
}

def generate_ai_caption(prompt):
    payload = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {"role": "user", "content": f"Write a short, catchy, and trendy Instagram caption with emojis for the following photo description. Do not include any conversational filler, just the caption.\n\nDescription: {prompt}"}
        ],
        "max_tokens": 100,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=15)
        
        if response.status_code != 200:
            return f"⚠️ API Error: {response.text}"
            
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
        
    except Exception as e:
        return f"⚠️ Error connecting to Groq API: {str(e)}"

st.markdown("---")
user_input = st.text_input("Describe your photo", placeholder="e.g. Sunset vibes at the beach...")
generate_btn = st.button("Generate Caption")

if generate_btn and user_input:
    st.markdown(f"**Your Description:** {user_input}")
    
    with st.spinner("Generating AI Caption via Groq..."):
        ai_caption = generate_ai_caption(user_input)
        
    st.session_state.history.append({"user": user_input, "ai": ai_caption})
    
    if len(st.session_state.history) > 3:
        st.session_state.history = st.session_state.history[-3:]

if st.session_state.history:
    st.markdown("### Recent Generations")
    for chat in st.session_state.history:
        with st.chat_message("user"):
            st.write(chat["user"])
        with st.chat_message("assistant"):
            st.write(chat["ai"])