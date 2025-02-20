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
        self.data_ingestion_dir:str=os.path.join(training_pipeline_confg.artifact_dir, constants.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path:str = os.path.join(self.data_ingestion_dir, constants.DATA_INGESTION_FEATURE_STORE_DIR, constants.FILE_NAME)
        self.training_file_path:str=os.path.join(self.data_ingestion_dir, constants.DATA_INGESTION_INGESTED_DIR, constants.TRAIN_FILE)
        self.testing_file_path:str=os.path.join(self.data_ingestion_dir, constants.DATA_INGESTION_INGESTED_DIR, constants.TEST_FILE)
        self.train_test_split_ratio:float=constants.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name=constants.DATA_INGESTION_COLLECTION_NAME
        self.database_name=constants.DATA_INGESTION_DATABASE_NAME