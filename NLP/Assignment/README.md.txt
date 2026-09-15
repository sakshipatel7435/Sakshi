<h1 align="center">
  🧠 Natural Language Processing (NLP) Coursework
</h1>

<p align="center">
  <strong>A comprehensive collection of NLP assignments—from basic text preprocessing to advanced Hugging Face Transformer models.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter Notebook" />
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
</p>

---

## 📖 Overview

This repository contains my end-to-end coursework for the **Natural Language Processing (NLP)** module. It is structured into 5 distinct sessions, steadily progressing from fundamental text manipulation all the way to deep learning architectures like Transformers and Attention Mechanisms. 

All code is written in highly modular and strictly formatted Jupyter Notebooks, ensuring clean logic and immediate output visualizations.

---

## 🚀 Session Breakdown

### [Session 1: Introduction to NLP & Use Cases](./Session_1)
*   **Theory:** Explored real-world NLP applications like WhatsApp predictive text, Swiggy customer support chatbots, and Gmail spam filters.
*   **Practical:** Built a completely rule-based Python spam detector and a basic keyword-driven sentiment analyzer using native Python string methods (`.split()`, `.lower()`).

### [Session 2: Text Cleaning & Preprocessing](./Session_2)
*   **Practical:** Mastered the essential preprocessing pipeline required before feeding text to any machine learning model:
    *   **Punctuation Stripping:** Cleaned Flipkart reviews using `string.punctuation`.
    *   **Stopword Removal:** Used NLTK to filter out useless filler words from WhatsApp chats.
    *   **Stemming:** Implemented NLTK's `PorterStemmer` to strip trending Twitter hashtags down to their root forms.

### [Session 3: Feature Engineering for Text](./Session_3)
*   **Theory:** Analyzed the critical differences between frequency counting (Bag of Words) and semantic importance weighting (TF-IDF) in search recommendation algorithms.
*   **Practical:** 
    *   Used `CountVectorizer` to generate a Bag of Words matrix from Zomato reviews.
    *   Used `TfidfVectorizer` to calculate and extract TF-IDF vectors for specific target words in a dataset of Flipkart product reviews.

### [Session 4: Text Classification Models](./Session_4)
*   **Practical:** Transitioned from manual rules to actual Machine Learning models:
    *   **Naive Bayes:** Trained a `MultinomialNB` classifier on Zomato reviews to predict Positive/Negative sentiment.
    *   **Logistic Regression:** Built a highly accurate WhatsApp spam detector using `LogisticRegression`.
    *   **Model Comparison:** Used `train_test_split` and `accuracy_score` to objectively evaluate and compare the performance of Naive Bayes against Logistic Regression on the same dataset.

### [Session 5: Deep Learning for NLP](./Session_5)
*   **Theory:** Broke down the limitations of traditional BoW/TF-IDF models regarding word-order context, and researched state-of-the-art Transformer architectures like RoBERTa.
*   **Practical:** 
    *   Leveraged the **Hugging Face `transformers`** library to deploy a pre-trained sentiment analysis `pipeline` directly on Zomato/Swiggy reviews.
    *   Demonstrated a mathematical NumPy implementation of the **Attention Mechanism**, clearly explaining how attention weights relate context across a sequence of words.

---

## 💻 Getting Started

To run the notebooks locally, clone this repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/yourusername/nlp-coursework.git
cd nlp-coursework

# Install all required data science and ML packages
pip install pandas numpy scikit-learn nltk transformers torch
```

Open any session folder in Jupyter Notebook or VS Code to run the highly granular, step-by-step cells.

---
<p align="center">
  <i>Developed and structured according to strict clean-code principles. No redundant comments, highly modular cell design.</i>
</p>