# Final End-to-End Project (Session 6)

## Task 4: Deployment on PythonAnywhere
To deploy this project to PythonAnywhere (or a similar cloud platform):
1. Sign up for a free PythonAnywhere account.
2. Go to the **Files** tab and upload your `predict_review.py` and `review_sentiment_model.pkl` files into a new folder.
3. Go to the **Web** tab, click "Add a new web app", select Flask, and configure the source code path to point to your uploaded `predict_review.py`.
4. Once your API is live (e.g., `https://yourusername.pythonanywhere.com/predict`), open `review_predictor.html` in your favorite code editor and update the Javascript `fetch()` URL to match your new live cloud API URL instead of `127.0.0.1:5000`.
5. Open `review_predictor.html` in your browser.
   * **Test 1:** "Amazing phone, I love it" -> *Predicted Positive*
   * **Test 2:** "Terrible battery life, completely useless" -> *Predicted Negative*
   * **Test 3:** "Very good quality" -> *Predicted Positive*

## Task 5: Project Workflow Explanation
The end-to-end workflow begins when a user types their product feedback into the HTML frontend textarea and clicks the Predict button. This action triggers a JavaScript `fetch()` function that packages the text into a JSON payload and sends an asynchronous POST request to our Flask API server. The Flask application receives this payload, extracts the raw review string, and passes it into our pre-trained machine learning pipeline (which handles both word vectorization and Naive Bayes classification automatically). The model evaluates the text and predicts whether the overall sentiment is 'Positive' or 'Negative' based on the patterns it learned during the training phase. This string result is packaged into a new JSON response and sent back to the frontend. Finally, the JavaScript code receives this response, changes the text color to green or red based on the sentiment, and dynamically updates the DOM to display the result on the user's screen without reloading the page.