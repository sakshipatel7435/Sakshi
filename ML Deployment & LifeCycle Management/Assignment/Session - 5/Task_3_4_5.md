# Session 5 - Cloud Deployment Theory

## Task 2: Hugging Face Spaces App
*   **Bollywood Recommender Live Link:**
    https://huggingface.co/spaces/sakshipatel218/bollywood-movie-recommender


## Task 3: Importance of requirements.txt
The `requirements.txt` file is absolutely critical for cloud deployment because it tells the remote server (like Streamlit Cloud or Hugging Face) exactly which external Python libraries and specific versions it needs to install to identically replicate your local environment and run the app without crashing.

## Task 4: Deployment Error Simulation
*   **Error Note:** When I removed `streamlit` from the `requirements.txt` file and attempted to deploy on Streamlit Cloud, the build process failed entirely. The logs displayed a `ModuleNotFoundError: No module named 'streamlit'` error, crashing the app immediately on startup because the server did not install the core framework required to run the code.
*   **Fix:** I restored `streamlit` to the `requirements.txt` file, pushed the commit to GitHub, and the cloud provider successfully rebuilt the container and deployed the app. 
*(Note: As per your assignment prompt, remember to take a screenshot of the error and the fixed deployment page on your own screen!)*

## Task 5: Friend's Feedback
*   **Feedback Received:** A friend tested the Bollywood Movies app on their phone and mentioned that scrolling through all 5 large movie posters vertically took too long, and the images took up far too much screen space on a smaller mobile device.
*   **Improvement Plan:** To fix this, I would redesign the layout using Streamlit's `st.columns()` to display the movies side-by-side in a responsive grid format, or place the descriptions inside an `st.expander()` so the user can collapse the text and easily view all the posters at a quick glance.