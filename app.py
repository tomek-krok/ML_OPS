from fastapi import FastAPI

import model_classifier

from api.models.iris import PredictRequest, PredictResponse

model = model_classifier.load_model()
app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    prediction = model_classifier.predict(
        model,
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    )
    return PredictResponse(prediction=prediction)
