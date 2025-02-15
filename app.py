from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.textsummarizer.pipeline.prediction_pipeline import PredictionPipeline

text = "what is text summarization"

app = FastAPI()

@app.get("/",tags=["authentication"])
async def index():

    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():

    try:
        os.system("python main.py")

    except Exception as e:
        print(f"Error while training: {e}")
        return Response(status_code=500, content=f"Error while training: {str(e)}")
    

@app.post("/predict")
async def predict_route(text):

    try:
        pipeline = PredictionPipeline()
        summary = pipeline.predict(text)
        return {"summary": summary}
    except Exception as e:

        raise e
    

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8080)