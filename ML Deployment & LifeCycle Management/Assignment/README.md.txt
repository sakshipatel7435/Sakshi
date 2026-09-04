# ML Deployment & Lifecycle Management

This repository contains my complete coursework and practical implementations for the **ML Deployment & Lifecycle Management** module. The project is broken down into 6 comprehensive sessions that cover the entire journey of a Machine Learning model—from basic training and serialization, to building backend APIs, all the way to cloud deployment and full-stack integration.

---

## 📁 Repository Structure

### [Session 1: Introduction to ML Deployment](./Session_1)
*   **Theory:** Explores the fundamental differences between model training and deployment in production environments.
*   **Practical:** Implemented a batch prediction script (`batch_prediction.ipynb`) that simulates offline ML inference for bulk restaurant reviews.

### [Session 2: Saving & Loading Models](./Session_2)
*   **Theory:** Designed a folder structure methodology for ML model versioning (e.g., `v1`, `v2`).
*   **Practical:** Trained custom classification models for Spotify genres and Flipkart product categories using `scikit-learn`. Successfully serialized and deserialized the trained models using both `pickle` and `joblib`.

### [Session 3: Flask Prediction API](./Session_3)
*   **Backend:** Built a REST API using the Flask framework.
*   **Endpoints:** Created `/predict-price` and `/predict-delivery` endpoints that accept JSON `POST` requests and utilize a serialized ML model to return dynamic predictions (e.g., estimated food delivery times).

### [Session 4: FastAPI + Postman Testing](./Session_4)
*   **Backend:** Transitioned to the modern, high-performance FastAPI framework powered by Uvicorn.
*   **Validation:** Developed an Instagram Like Predictor API featuring native `Pydantic` data validation to instantly catch missing fields and return custom HTTP 400 Bad Request errors.
*   **Testing:** Fully tested endpoints using Postman.

### [Session 5: Cloud Deployment](./Session_5)
*   **Streamlit Cloud:** Built and deployed an interactive web app (`IPL_Team_App`) highlighting a favorite cricket team.
*   **Hugging Face Spaces:** Built and deployed a secondary Streamlit app (`Bollywood_Movies_App`) featuring trending movie posters and descriptions.
*   **Environment Management:** Configured strict `requirements.txt` files to guarantee identical cross-platform cloud container builds.

### [Session 6: Final End-to-End Project](./Session_6)
*   **Machine Learning:** Trained a Natural Language Processing (NLP) pipeline (CountVectorizer + Multinomial Naive Bayes) to classify Flipkart product reviews as Positive or Negative.
*   **Backend API:** Wrapped the serialized NLP model in a Flask API endpoint equipped with CORS mapping.
*   **Frontend UI:** Designed a sleek HTML/JS frontend (`review_predictor.html`) that uses asynchronous `fetch()` requests to dynamically update the DOM with the model's sentiment prediction in real-time, without reloading the page.
*   **Deployment:** Ready for deployment on cloud hosts like PythonAnywhere.

---

## 🚀 Getting Started

To run any of the API sessions locally, ensure you have the required global dependencies installed:
```bash
pip install scikit-learn flask fastapi uvicorn flask-cors pandas numpy streamlit
```

Navigate to any session folder and boot up the respective server:
*   **Flask (Sessions 3 & 6):** `python predict_review.py`
*   **FastAPI (Session 4):** `uvicorn insta_like_api:app --reload`
*   **Streamlit (Session 5):** `streamlit run app.py`