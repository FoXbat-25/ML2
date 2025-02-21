import os
import sys
from datetime import datetime
from networkSecurity.components.exception import customException
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from networkSecurity.components.config import DataIngestionConfg
from decouple import config
from pymongo.mongo_client import MongoClient
from networkSecurity.components.artifiact_config import DataIngestionArtifact

mongo_db_url = config('URL')

class DataIngestion:
    def __init__(self, data_ingestion_confg:DataIngestionConfg):
        try:
            self.data_ingestion_confg=data_ingestion_confg
        except Exception as e:
            raise customException(e,sys)

    def data_to_df(self):
        try:
            database_name=self.data_ingestion_confg.database_name
            collection_name=self.data_ingestion_confg.collection_name
            self.mongo_client=MongoClient(mongo_db_url)
            collection=self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"], axis=1)

            df.replace({"na":np.nan}, inplace=True)
            return df    
        except Exception as e:
            raise customException(e,sys)

    def data_to_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_confg.feature_store_file_path
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise customException(e,sys)

    def df_train_test_split(self, dataframe):
        try:
            train_file_path=self.data_ingestion_confg.training_file_path
            test_file_path=self.data_ingestion_confg.testing_file_path
            dir_path=os.path.dirname(train_file_path)
            os.makedirs(dir_path, exist_ok=True)
            train_set, test_set=train_test_split(dataframe, test_size=self.data_ingestion_confg.train_test_split_ratio)
            train_set.to_csv(train_file_path, index=False, header=True)
            test_set.to_csv(test_file_path, index=False, header=True)
        except Exception as e:
            raise customException(e,sys)        
    
    def initiate_data_ingestion(self):
        try:
            dataframe=self.data_to_df()
            dataframe=self.data_to_feature_store(dataframe)
            self.df_train_test_split(dataframe)
            DataInArtifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_confg.training_file_path, tested_file_path=self.data_ingestion_confg.testing_file_path)
            return DataInArtifact


        except Exception as e:
            raise customException(e,sys)