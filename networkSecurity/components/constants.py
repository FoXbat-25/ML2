import os
import sys
import pandas as pd

TARGET_COLUMN="Result"
PIPELINE_NAME="NetworkSecurity"
ARTIFACT_DIR="Artifacts"
FILE_NAME="phisingData.csv"
TRAIN_FILE="Train.csv"
TEST_FILE="Test.csv"

DATA_INGESTION_COLLECTION_NAME:str="networkData"
DATA_INGESTION_DATABASE_NAME:str="charlie"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2