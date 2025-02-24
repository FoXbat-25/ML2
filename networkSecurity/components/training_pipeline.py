import os
import sys
from networkSecurity.components.exception import customException
from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.data_transformation import DataTransformation
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.components.model_trainer import ModelTrainer
from networkSecurity.components.config import TrainingPipelineConfg,DataIngestionConfg, DataTransformationConfg, DataValidationConfg, ModelTrainerConfg
from networkSecurity.components.artifiact_config import DataIngestionArtifact, DataTransformationArtifact, DataValidationArtifact, ModelTrainerArtifact

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_confg=TrainingPipelineConfg() 

    def start_data_ingestion(self):
        try:
            self.data_ingestion_confg=DataIngestionConfg(training_pipeline_confg=self.training_pipeline_confg)
            dataIngestion=DataIngestion(data_ingestion_confg=self.data_ingestion_confg)
            dataIngestionArtifact=dataIngestion.initiate_data_ingestion()
            return dataIngestionArtifact

        except Exception as e:
            raise customException(e,sys)

    def start_data_validation(self, data_ingestion_artifact:DataIngestionArtifact):
        try:
            dataValidConfg=DataValidationConfg(training_pipeline_confg=self.training_pipeline_confg)
            dataValidation=DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_confg=dataValidConfg)
            dataValidationArtifact=dataValidation.initiate_data_validation()
            return dataValidationArtifact
        except Exception as e:
            raise customException(e,sys)

    def start_data_transformation(self, data_validation_artifact:DataValidationArtifact):
        try:
            dataTransConfg=DataTransformationConfg(training_pipeline_confg=self.training_pipeline_confg)
            dataTransformation=DataTransformation(data_validation_artifact=data_validation_artifact, data_transformation_confg=dataTransConfg)
            dataTransformationArtifact=dataTransformation.initiate_data_transformation()
            return dataTransformationArtifact
        except Exception as e:
            raise customException (e,sys)
        
    def start_model_trainer(self, data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifact:
        try:
            self.model_trainer_confg:ModelTrainerConfg=ModelTrainerConfg(training_pipeling_confg=self.training_pipeline_confg)
            modelTrainer=ModelTrainer(data_transformation_artifact=data_transformation_artifact,model_trainer_confg=self.model_trainer_confg, )
            modelTrainerArtifact=modelTrainer.initiate_model_trainer()
            return modelTrainerArtifact
        except Exception as e:
            raise customException (e,sys)
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            return model_trainer_artifact
        except Exception as e:
            raise customException(e,sys)