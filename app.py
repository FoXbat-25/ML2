import os
import sys
import certifi
ca=certifi.where()
from decouple import config
mongo_db_url=config('URL')
print(mongo_db_url)
 
import pymongo
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd
from networkSecurity.utils.utils import load_obj
from networkSecurity.components.exception import customException
from networkSecurity.components.training_pipeline import TrainingPipeline
from networkSecurity.utils.estimator import NetworkModel

client=pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from networkSecurity.components.constants import DATA_INGESTION_COLLECTION_NAME, DATA_INGESTION_DATABASE_NAME
from fastapi.templating import Jinja2Templates
templates=Jinja2Templates(directory="./templates")
database=client[DATA_INGESTION_DATABASE_NAME]
collection=database[DATA_INGESTION_COLLECTION_NAME]

app=FastAPI()
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline=TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training successful")
    except Exception as e:
        raise customException(e,sys)

@app.post("/predict") 
async def predict_route(request:Request,file:UploadFile=(...)):
    try:
        df=pd.read_csv(file.file)
        preprocessor=load_obj("final_models/preprocessor.pkl")   
        model=load_obj("final_models/model.pkl")    
        network_model=NetworkModel(preprocessor=preprocessor, model=model)
        y_pred=network_model.predict(df)
        df['predicted_column'] =y_pred
        print(df['predicted_column'])
        df.to_csv('prediction_output/output.csv') 
        table_html=df.to_html(classes='table table-striped')
        return templates.TemplateResponse("table.html", {"request":request, 'table':table_html})
    except Exception as e:
        raise customException(e,sys)
if __name__=="__main__":
    app_run(app,host='localhost', port=8000)