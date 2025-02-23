import os
from networkSecurity.components import constants
from datetime import datetime

class TrainingPipelineConfg:
    def __init__(self, timestamp=datetime.now()):
        timestamp=timestamp.strftime('%d_%M_%Y_%H_%M_%S')
        self.pipeline_name=constants.PIPELINE_NAME
        self.artifact_dir=constants.ARTIFACT_DIR
        self.artifact_name=os.path.join(self.artifact_dir, timestamp)
        self.timestamp:str=timestamp

class DataIngestionConfg:
    def __init__(self, training_pipeline_confg:TrainingPipelineConfg):
        self.data_ingestion_dir:str=os.path.join(training_pipeline_confg.artifact_dir, constants.DATA_INGESTION_DIR_NAME) #Artifacts/data_ingestion
        self.feature_store_file_path:str = os.path.join(self.data_ingestion_dir, constants.DATA_INGESTION_FEATURE_STORE_DIR, constants.FILE_NAME) #Artifacts/data_ingestion/feature_store/phisingData.csv
        self.training_file_path:str=os.path.join(self.data_ingestion_dir, constants.DATA_INGESTION_INGESTED_DIR, constants.TRAIN_FILE) #Artifacts/data_ingestion/ingested/Train.csv
        self.testing_file_path:str=os.path.join(self.data_ingestion_dir, constants.DATA_INGESTION_INGESTED_DIR, constants.TEST_FILE) #Artifacts/data_ingestion/ingested/Test.csv
        self.train_test_split_ratio:float=constants.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name=constants.DATA_INGESTION_COLLECTION_NAME
        self.database_name=constants.DATA_INGESTION_DATABASE_NAME

class DataValidationConfg:
    def __init__(self, training_pipeline_confg:TrainingPipelineConfg):
        self.data_validation_dir:str=os.path.join(training_pipeline_confg.artifact_dir, constants.DATA_VALIDATION_DIR_NAME) #Artifacts/data_validation
        self.valid_data_dir:str=os.path.join(self.data_validation_dir, constants.VALID_DATA_DIR) #Artifacts/data_validation/valid
        self.invalid_data_dir:str=os.path.join(self.data_validation_dir, constants.INVALID_DATA_DIR) #Artifacts/data_validation/invalid
        self.valid_train_file_path:str=os.path.join(self.valid_data_dir, constants.TRAIN_FILE) #Artifacts/data_validation/valid/Train.csv
        self.valid_test_file_path:str=os.path.join(self.valid_data_dir, constants.TEST_FILE) #Artifacts/data_validation/valid/Train.csv
        self.invalid_train_file_path:str=os.path.join(self.invalid_data_dir, constants.TRAIN_FILE) #Artifacts/data_validation/invalid/Train.csv
        self.invalid_test_file_path:str=os.path.join(self.invalid_data_dir, constants.TEST_FILE) #Artifacts/data_validation/invaled/Test.csv
        self.drift_report_path:str=os.path.join(self.data_validation_dir, constants.DRIFT_DATA_DIR, constants.DRIFT_REPORT_NAME)  #Artifacts/data_validation/drift_report/drift_report.yaml.

class DataTransformationConfg:
    def __init__(self, training_pipeline_confg:TrainingPipelineConfg):
        self.data_transformation_dir:str=os.path.join(training_pipeline_confg.artifact_dir, constants.DATA_TRANSFORMATION_DIR)
        self.transformed_train_file_path=os.path.join(self.data_transformation_dir, constants.TRANSFORMED_DATA_DIR, constants.TRAIN_FILE.replace("csv", "npy"))
        self.transformed_test_file_path=os.path.join(self.data_transformation_dir, constants.TRANSFORMED_DATA_DIR, constants.TEST_FILE.replace("csv", "npy"))
        self.transformed_obj_file_path=os.path.join(self.data_transformation_dir, constants.TRANSFORMED_OBJECT_DIR, constants.PREPROCESSING_OBJ_FILE_NAME)

class ModelTrainerConfg:
    def __init__(self, training_pipeling_confg:TrainingPipelineConfg):
        self.model_trainer_dir:str=os.path.join(training_pipeling_confg.artifact_dir, constants.MODEL_TRAINER_DIR)
        self.trained_model_path=os.path.join(self.model_trainer_dir, constants.TRAINED_MODEL_DIR, constants.TRAINED_MODEL_NAME)
        self.expected_accuracy=constants.MODEL_TRAINER_EXPECTED_SCORE
        self.over_fitting_under_fitting_threshold=constants.MODEL_TRAINER_OVR_FTNG_UNDR_FTNG_THRSHLD
                