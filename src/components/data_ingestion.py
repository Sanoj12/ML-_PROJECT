import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import  dataclass



@dataclass ### decorater uses -directly define class variable 
class DataIngestionConfig: ##data ingestion component 
     
     train_data_path: str = os.path.join('datasets',"train.csv")  ###output stored artifacts folder
     test_data_path: str = os.path.join('datasets',"test.csv")
     raw_data_path: str = os.path.join('datasets',"data.csv")


class DataIngestion:
     def __init__(self):
          self.ingestion_config = DataIngestionConfig()

     def initiate_data_ingestion(self):
          ##data read from different differennt sources like databases or utils fn
          logging.info("entered the data ingestion method or component")
          try:
              
              df=pd.read_csv('notebook\data\stud.csv')
              logging.info("Read the dataset as dataframe")

              os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

              df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

              logging.info("Train test split initiated")


              train_set , test_set = train_test_split(df,test_size=0.2 ,random_state=42)


              train_set.to_csv(self.ingestion_config.train_data_path,index=False ,header=True)

              test_set.to_csv(self.ingestion_config.test_data_path ,index=False ,header=True)

              logging.info("ingestion of the data completed!!")

              return(
                   #data transformation uses
                   self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path
              )


          except Exception as e:
               raise CustomException(e,sys)
        
              
if __name__=="__main__":
     obj=DataIngestion()
     obj.initiate_data_ingestion()
   


