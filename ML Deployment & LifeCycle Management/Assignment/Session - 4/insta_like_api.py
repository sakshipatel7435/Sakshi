# Task 2 & 4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class LikeRequest(BaseModel):
    current_likes: Optional[int] = None
    new_likes: Optional[int] = None

@app.get('/')
def read_root():
    return {'message': 'Instagram Like Counter API running'}

@app.post('/predict-likes')
def predict_likes(request: LikeRequest):
    if request.current_likes is None or request.new_likes is None:
        raise HTTPException(status_code=400, detail="Both 'current_likes' and 'new_likes' are required.")
    total_likes = request.current_likes + request.new_likes
    return {'total_likes': total_likes}