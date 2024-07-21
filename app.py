from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to my Hugging Face demo API"}

@app.post("/predict/")
def predict(input_data: InputData):
    text = input_data.text
    # For demonstration purposes, we just return the received text.
    # Replace this part with your model inference code.
    return {"predicted_text": text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
