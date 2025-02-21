import os
import sys
from datetime import datetime
from networkSecurity.components.exception import customException
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from networkSecurity.components.config import DataIngestionConfg, DataValidationConfg
from decouple import config
from pymongo.mongo_client import MongoClient
from networkSecurity.components.artifiact_config import DataIngestionArtifact, DataValidationArtifact
from scipy.stats import ks_2samp # For data drift check
from networkSecurity.components.constants import SCHEMA_FILE_PATH
from networkSecurity.utils.utils import read_yaml_file, write_yaml_file

class DataValidation:
    def __init__(self, data_ingestion_artifact:DataIngestionArtifact, data_validation_confg:DataValidationConfg):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_confg=data_validation_confg
            self._schema_confg=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise customException (e, sys)

    def validate_num_of_cols(self,dataframe:pd.DataFrame)->bool:
        try:
            num_of_df_col=len(dataframe.columns)
            num_of_schema_cols=len(self._schema_confg['columns'])
            if num_of_df_col==num_of_schema_cols :
                return True
            return False
        except Exception as e:
            raise customException (e,sys)        

    def validate_numerical_cols(self, dataframe:pd.DataFrame)->bool:
        try:
            df_total_numcols=sum(dataframe.dtypes!='O')
            schema_total_numcols=len(self._schema_confg['numerical_columns'])
            if df_total_numcols==schema_total_numcols: return True
            return False
        except Exception as e:
            raise customException(e,sys)
        
    def data_drift_check(self, base_df, current_df, threshold=0.05)->bool:
        try:
            status=True
            report={}
            for column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                sample_dist_check=ks_2samp(d1,d2)
                if threshold<=sample_dist_check.pvalue:
                    drift=False
                else: 
                    drift=True
                    status=False
                report.update({column:{
                    "p_value":float(sample_dist_check.pvalue),
                    "drift_status":drift
                }})
            drift_report_path=self.data_validation_confg.drift_report_path
            dir_path=os.path.dirname(drift_report_path)   
            os.makedirs(dir_path, exist_ok=True)
            write_yaml_file(file_path=drift_report_path, content=report)
        except Exception as e:
            raise customException(e,sys)

    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path=self.data_ingestion_artifact.trained_file_path
            test_file_path=self.data_ingestion_artifact.tested_file_path

            train_df=pd.DataFrame(pd.read_csv(train_file_path))
            test_df=pd.DataFrame(pd.read_csv(test_file_path))

            status=self.validate_num_of_cols(dataframe=train_df)
            if status==False: 
                print("Train df doesnt contain all columns.\n")

            status=self.validate_num_of_cols(dataframe=test_df)
            if status==False: 
                print("Testrain df doesnt contain all columns.\n")

            status=self.validate_numerical_cols(dataframe=train_df)
            if status==False: print("Train df doesnt contain all numerical columns.\n") 

            status=self.validate_numerical_cols(dataframe=test_df)
            if status==False: print("Test df doesnt contain all numerical columns.\n")        

            status=self.data_drift_check(base_df=train_df, current_df=test_df)
            dir_path=os.path.dirname(self.data_validation_confg.valid_train_file_path)
            os.makedirs(dir_path, exist_ok=True)
            train_df.to_csv(os.path.join(dir_path, 'Train.csv'), index=False, header=True)
            test_df.to_csv(os.path.join(dir_path, 'Test.csv'), index=False, header=True)

            data_validation_artifact=DataValidationArtifact(
                validationStatus=status,
                valid_train_data_path=self.data_ingestion_artifact.trained_file_path,
                valid_test_data_path=self.data_ingestion_artifact.tested_file_path,
                invalid_train_data_path=None,
                invalid_test_data_path=None,
                drift_report_path=self.data_validation_confg.drift_report_path
            )
            return data_validation_artifact
        except Exception as e:
            raise customException(e, sys)

