<div align="center">

# 🤖 Transformer Architecture & LLMs

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Transformers](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-FFFFFF?style=for-the-badge&logo=ollama&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)

*A hands-on exploration of Large Language Models (LLMs), covering theoretical frameworks, HuggingFace model implementation, local execution with Ollama, advanced prompt engineering, and real-world API integrations with Groq and Streamlit.*

---

</div>

## 📑 Repository Structure

This repository is divided into six distinct sessions, progressing from high-level LLM concepts to practical, code-based web app integrations.

### 📖 SESSION 1 - Overview of LLMs
- Explores massive foundational models (GPT-4, Claude 3.5, Gemini) and their enterprise-level use cases.
- Breaks down the core mechanics of LLM text generation (Tokenization and Next-Word Prediction).
- Provides a comprehensive comparison between legacy Rule-Based chatbots and dynamic LLM agents.
- Analyzes the limitations and critical risks of LLMs in business (specifically Data Privacy and AI Hallucinations).

### ⚙️ SESSION 2 - GPT vs BERT vs T5
*(Note: Python code uses pure TensorFlow pipelines via HuggingFace Transformers, strictly avoiding PyTorch dependencies).*
- **GPT-2 (Decoder-Only):** Instantiated a local text-generation pipeline to successfully synthesize a catchy Instagram caption from scratch.
- **DistilBERT (Encoder-Only):** Loaded a sequence classification model to analyze a Zomato review, identifying positive intent with 99.9% confidence.
- **T5 (Encoder-Decoder):** Implemented a Text-to-Text model natively using AutoModelForSeq2SeqLM to paraphrase complex sentences.
- **Architecture Breakdown:** Detailed markdown comparisons explaining exactly when to use Generator, Bidirectional Encoder, and Transformer models.

### 🔓 SESSION 3 - Open vs Closed Source Models + Ollama
- Deep-dive into Open-Source (Llama 3, Mistral, Falcon) vs Closed-Source (GPT-4, Claude) paradigms.
- Highlights a 5-point comparison across Cost, Customization, Community Support, Data Privacy, and Update Frequency.
- **Local AI Execution:** Documents the exact terminal commands required to pull and boot a 3.8GB Llama 2 model entirely offline using **Ollama**.
- **Product Ideation:** Features a locally-generated AI proposal for a Zomato "Dietary Guardian" feature that proactively scans menus for hidden allergens.

### 🗣️ SESSION 4 - Prompt Engineering Basics
- **Zero-Shot Prompting:** Demonstrates unguided AI summation of trending IPL topics without examples.
- **Few-Shot Prompting:** Crafts a heavily structured prompt supplying two comedic examples to force the AI to generate a hilarious one-line review.
- **Prompt Optimization:** Explores how injecting strict Roles, Tones, and Formatting Constraints drastically improves AI output compared to vague requests.
- **Common Mistakes:** Identifies the three largest mistakes beginners make (Vagueness, Missing Context, Open-Ended Formatting) and provides "Bad vs Better" rewrite examples.

### 🚀 SESSION 5 - Build Streamlit LLM App
- **Interactive UI:** Built a complete, interactive web application from scratch using Python's streamlit framework (insta_caption_generator.py).
- **REST APIs (Groq):** Utilized the 
equests library to establish a live HTTP connection to the Groq API (using Llama 3 models) for incredibly fast text generation.
- **State Management:** Implemented Streamlit's st.session_state to actively remember the user's last 3 interactions and display them dynamically as chat bubbles.

### 🏢 SESSION 6 - Real Projects & Use Cases
- **PDF Extraction Bot:** Developed a Python script utilizing PyPDF2 to read, parse, and extract text data from uploaded PDF documents.
- **Support Chatbot Logic:** Programmed a Python-based intent routing engine utilizing conditional if-else logic to automatically resolve food delivery queries (refunds, order status, delays).
- **Groq API Integration:** Designed a Python function explicitly utilizing Groq's API to dynamically generate short-form blog posts, safely wrapping it in try/except blocks to simulate outputs if API keys are missing.
- **Enterprise Integrations:** Analyzed how massive Indian corporations (MakeMyTrip, Zomato, TCS) leverage GenAI for localized voice agents and automated legacy code migration.
- **Prompt Upgrades:** Enhanced the Groq content generator by dynamically injecting target 	one parameters (e.g., 'Gen-Z enthusiastic') and cranking the model 	emperature up to 0.8 for maximum creativity.

---

## 🚀 Getting Started

The code and theoretical answers are provided as beautifully formatted Jupyter Notebooks (.ipynb). You can view the embedded outputs directly on GitHub!

To run the Streamlit app locally:
`ash
pip install streamlit requests
streamlit run "SESSION 5 - Build Streamlit LLM App/insta_caption_generator.py"
`

To run the HuggingFace models locally (Session 2), install the required dependencies:
`ash
pip install transformers tensorflow
`

> **Note:** API Keys for Groq have been securely removed from the source code for safety. To execute the API cells, simply replace "YOUR_GROQ_API_KEY_HERE" with your actual API key!