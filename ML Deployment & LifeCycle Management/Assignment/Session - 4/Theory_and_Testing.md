# Session 4 Testing and Theory

## Task 3: Postman Testing Instructions
1. Open your terminal in the `Session_4` folder and start the FastAPI server using Uvicorn:
   ```powershell
   uvicorn insta_like_api:app --reload
   ```
2. Open Postman.
3. Set the method to **POST**.
4. Enter the URL: `http://127.0.0.1:8000/predict-likes`
5. Go to the **Body** tab, choose **raw**, and select **JSON** from the dropdown.
6. Paste the payload:
   ```json
   {
       "current_likes": 1200,
       "new_likes": 350
   }
   ```
7. Click **Send**. You will receive `{"total_likes": 1550}`.
8. **To test Task 4**, remove the `"new_likes": 350` line from your JSON and click Send again. You will successfully receive the custom 400 Error Message we programmed!

## Task 5: FastAPI vs. Flask (IPL Fantasy Points Prediction)
If I were building an IPL fantasy points prediction API, I would absolutely choose **FastAPI** over Flask. FastAPI is significantly faster (built on Starlette and ASGI) which is crucial during live IPL matches where thousands of users are simultaneously requesting real-time point predictions. Additionally, FastAPI automatically uses Pydantic to validate the incoming request payloads (like player stats or match conditions) and instantly generates interactive Swagger UI documentation, saving hours of manual validation and documentation work that Flask would otherwise require.