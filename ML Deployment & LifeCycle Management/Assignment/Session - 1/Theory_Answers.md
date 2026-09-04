# Session 1 - Introduction to ML Deployment

## Task 1: Training vs. Deployment
Training is the process where a machine learning model learns patterns by analyzing historical data, which is computationally heavy and done offline. Deployment is the process of taking that finalized, trained model and integrating it into a live production environment so it can make predictions on new, unseen data in real-time. For example, in Zomato, the model is trained offline on millions of past orders to learn food preferences; it is then deployed to the live app where it instantly predicts and ranks restaurant recommendations for you the moment you open the app.

## Task 2: Real-World ML Deployment Examples
1. **Spam Detection in WhatsApp/Gmail:** Users interact with this invisibly. When a user receives a message, the deployed model analyzes the text in the background and automatically diverts flagged messages to a 'Spam' folder or displays a scam warning before the user clicks on it.
2. **Personalized Playlists in Spotify (e.g., Discover Weekly):** Users interact by simply pressing play on a custom playlist. The deployed recommendation model generates this playlist weekly by comparing the user's recent listening history against millions of other users' patterns.
3. **Fraud Detection in Paytm:** Users experience this when completing a transaction. If a user tries to transfer an unusually large amount of money from a new device, the deployed ML model detects the anomaly in milliseconds and triggers a two-factor authentication prompt or temporarily blocks the transaction to protect the user.

## Task 3: Movie Recommendations (BookMyShow)
For a BookMyShow-like app, I would choose an **offline (batch) deployment** for the core movie recommendation engine. Movie tastes and catalogs do not change drastically by the minute, so it is highly efficient to run a heavy machine learning job overnight to pre-compute and cache a list of recommended movies for every user. When a user opens the app the next day, the server simply fetches the pre-computed list instantly, avoiding the massive server costs and latency associated with running complex real-time predictions every time someone loads the homepage.

## Task 5: Deployment Challenge in E-Commerce (Flipkart)
A major challenge when deploying ML models in a Flipkart-like app is **latency during high-traffic events** (like Big Billion Days), where the recommendation model gets overwhelmed by millions of simultaneous user requests and slows down the entire app. A reliable solution is to implement an API Gateway with load balancing to distribute requests across multiple servers, and to cache frequent predictions using Redis so the model doesn't have to recalculate recommendations for identical queries.