from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.exception import customException
from networkSecurity.components.config import DataIngestionConfg, TrainingPipelineConfg
import sys

if __name__=='__main__':
    try:
        training_pipeline_confg=TrainingPipelineConfg()
        dataInconfg=DataIngestionConfg(training_pipeline_confg)
        dataIngestion=DataIngestion(dataInconfg)
        dataArtifact=dataIngestion.initiate_data_ingestion()
        print(dataArtifact)

    except Exception as e:
        raise customException(e,sys)