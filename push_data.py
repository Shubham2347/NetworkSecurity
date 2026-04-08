
import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import numpy as np
import pandas as pd
import pymongo
from pymongo import MongoClient
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract:
    def __init__(self):
        try:
            self.mongo_client = MongoClient("mongodb+srv://slangade68_db_user:Admin2347@cluster0.uoz9uoj.mongodb.net/?appName=Cluster0") 
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = self.mongo_client[database]        # ✅ correct
            self.collection = self.database[collection]       # ✅ correct
            
            self.collection.insert_many(records)
            
            return len(records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)
            
if __name__ == '__main__':
    FILE_PATH = "network_data/phisingData.csv"
    DATABASE = "networksecuritydata"
    Collection = "NetworkData"

    networkobj = NetworkDataExtract()   

    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)

    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)
        