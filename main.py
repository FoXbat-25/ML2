from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.components.exception import customException
from networkSecurity.components.config import DataIngestionConfg, TrainingPipelineConfg, DataValidationConfg
import sys

if __name__=='__main__':
    try:
        training_pipeline_confg=TrainingPipelineConfg()
        dataInconfg=DataIngestionConfg(training_pipeline_confg)
        dataIngestion=DataIngestion(dataInconfg)
        dataIngestionArtifact=dataIngestion.initiate_data_ingestion()
        print(dataIngestionArtifact)
        
        dataValidConfg=DataValidationConfg(training_pipeline_confg)
        dataValidation=DataValidation(dataIngestionArtifact, dataValidConfg)
        dataValidationArtifact=dataValidation.initiate_data_validation()
        print(dataValidationArtifact)
        

    except Exception as e:
        raise customException(e,sys)