import os
import sys
import json
from decouple import config
from networkSecurity.components.exception import customException

mongo_db_url=config('URL')

import certifi
ca=certifi.where()

import pandas as pd
import pymongo
from pymongo.mongo_client import MongoClient
from networkSecurity.components.exception import customException
from networkSecurity.components.logger import logging

class networkDataExtract():
    def __init__(self):
        pass

    def csv_to_json(self, file_path):  #file_path to file to be converted to json
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise customException(e, sys)    
        
    def data_insertion(self, records, database, collection):
        try:
            self.database=database
            self.records=records
            self.collection=collection

            self.mongo_client=pymongo.MongoClient(mongo_db_url)
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        
        except Exception as e:
            raise customException(e, sys)
        
if __name__=='__main__':
    data_file='networkSecurity\data\phisingData.csv'
    database="charlie"
    collection='networkData'
    networkObj=networkDataExtract()
    records=networkObj.csv_to_json(file_path=data_file)
    insertion=networkObj.data_insertion(records,database,collection)
    print(f'Insertion complete- total insertion {insertion}')