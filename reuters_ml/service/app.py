from fastapi import FastAPI

from reuters_ml.service.inference import Inference
from reuters_ml.service.pydantic_models import Output

app = FastAPI()


@app.get("/check_response")
async def service_health():
    return {"Service is available"}


@app.post("/predict", response_model=Output)
async def model_predict(text: str):
    inference = Inference()
    response = inference.run(text)
    return {"prediction": response}
