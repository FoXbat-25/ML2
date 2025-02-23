import os
import sys
import numpy as np
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

DATA_VALIDATION_DIR_NAME="data_validation"
VALID_DATA_DIR="valid"
INVALID_DATA_DIR="invalid"
DRIFT_DATA_DIR="drift_report"
DRIFT_REPORT_NAME="drift_report.yaml"

SCHEMA_FILE_PATH=os.path.join("data_schema", "schema.yaml")

DATA_TRANSFORMATION_DIR="data_transformation"
DATA_TRANSFORMED_TRAIN_FILE=""
DATA_TRANSFORMED_TEST_FILE=""
TRANSFORMED_DATA_DIR="transformed"
TRANSFORMED_OBJECT_DIR="transformed_object"
DATA_TRANSFORMATION_IMPUTER_PARAMS:dict={
    "missing_values":np.nan,
    "n_neighbors":3,
    "weights":"uniform"
}

PREPROCESSING_OBJ_FILE_NAME="Preprocessing.pkl"