from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from prediction_model.predict import generate_prediction

app = FastAPI(
    title="Loan Prediction API using CI/CD Jenkins project.",
    description="API for Loan Prediction",
    version="0.2",
)

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoanPrediction(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Loan Prediction API using CI/CD Jenkins in EC2 [Version 0.2]"}

@app.post("/predict")
def predict(loan_data: LoanPrediction):
    data = loan_data.model_dump()
    prediction = generate_prediction([data])['prediction'][0]
    if prediction[0] == 'Y':
        result = 'Approved'
    else:
        result = 'Rejected'
    return {"status": result}

@app.post('/predict_ui')
def predict_gui(Gender: str,
    Married: str,
    Dependents: str,
    Education: str,
    Self_Employed: str,
    ApplicantIncome: float,
    CoapplicantIncome: float,
    LoanAmount: float,
    Loan_Amount_Term: float,
    Credit_History: float,
    Property_Area: str):
    input_data = [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]

    cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']

    data_dict = dict(zip(cols, input_data))
    prediction = generate_prediction([data_dict])['prediction']
    if prediction[0] == 'Y':
        result = 'Approved'
    else:
        result = 'Rejected'

    return {"status": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)


