<div align="center">

# 🧠 Natural Language Processing (NLP) Assessment

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-154f5b?style=for-the-badge&logo=python&logoColor=white)

*A comprehensive assessment covering foundational NLP concepts, text preprocessing pipelines, TF-IDF vectorization, and building Naive Bayes & Logistic Regression classifiers for sentiment analysis and issue categorization.*

---

</div>

## 📑 Repository Structure

This repository is organized into four distinct sections, separating theoretical concepts from practical Python implementations.

### 📖 Section A: Concept Application
**File:** [Section_A_Concept_Application.ipynb](./Section_A_Concept_Application.ipynb)
- Theoretical application of NLP concepts to real-world business scenarios.
- Covers Intent Classification, Named Entity Recognition, the importance of Stopword Removal in pipelines, and comparisons between Bag-of-Words and TF-IDF.
- Analyzes model evaluation metrics for imbalanced datasets and the advantages of Transformer Attention mechanisms over traditional RNNs.

### 💻 Section B: Practical Coding Tasks
**File:** [Section_B_Practical_Coding_Tasks.ipynb](./Section_B_Practical_Coding_Tasks.ipynb)
- **Task 1:** Built a robust text preprocessing function utilizing NLTK (lowercase, punctuation removal, stopword removal, and Porter Stemming).
- **Task 2:** Transformed food delivery reviews into a TF-IDF matrix using sklearn.feature_extraction.text.TfidfVectorizer.
- **Task 3:** Trained a Multinomial Naive Bayes classifier on complaint strings and outputted precision/recall classification reports.
- **Task 4:** Built end-to-end sklearn.pipeline objects comparing Naive Bayes vs. Logistic Regression for binary sentiment analysis.

### 🚀 Section C: Mini Capstone Project
**File:** [Section_C_Mini_Capstone.py](./Section_C_Mini_Capstone.py)
- A fully interactive, menu-driven **Review Intelligence System** built as a standard Python script.
- Allows the user to input live reviews, pass them through the preprocessing pipeline, and predict both Sentiment and Issue Category in real-time.
- Tracks and generates cumulative analytics and summary reports.

### 🤖 Section D: AI-Augmented Learning
**File:** [Section_D_AI_Augmented_Learning.ipynb](./Section_D_AI_Augmented_Learning.ipynb)
- Demonstrates the use of AI to generate an initial NLP classification pipeline.
- Includes a debugging segment identifying and manually fixing an AI hallucination (using it_transform instead of 	ransform on inference data causing shape-mismatch errors).

---

## ⚙️ How to Run the Capstone Project

The Mini Capstone Project (Section C) is an interactive console application. Run it directly from your terminal:

`ash
python Section_C_Mini_Capstone.py
`