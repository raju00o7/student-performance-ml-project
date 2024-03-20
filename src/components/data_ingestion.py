import os
import sys
import src.exception
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingesion_config=DataIngestionConfig()#function to get the data ingestion configuration

    def initiate_data_ingestion(self):#function to initiate the data ingestion
        logging.info("Data Ingestion Started")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Dataset read successfully")
            os.makedirs(os.path.dirname(self.ingesion_config.train_data_path),exist_ok=True)#create the directory if it does not exist

            df.to_csv(self.ingesion_config.raw_data_path,index=False,header=True)#save the raw data

            logging.info("Train and Test data split started")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)#split the data into train and test

            train_set.to_csv(self.ingesion_config.train_data_path,index=False,header=True)#save the train data

            test_set.to_csv(self.ingesion_config.test_data_path,index=False,header=True)#save the test data

            logging.info("Ingestion completed successfully")

            return(
                self.ingesion_config.train_data_path,#return the train data path
                self.ingesion_config.test_data_path,#return the test data path
                


            )
        except Exception as e:#catch the exception
            raise CustomException(e,sys)#raise the custom exception
        
if __name__=="__main__":
    obj=DataIngestion()#create the object of the class
    train_data,test_data=obj.initiate_data_ingestion()#call the function to initiate the data ingestion

    data_transformation=DataTransformation()#create the object of the data transformation class
    data_transformation.initiate_data_transformation(train_data,test_data)#call the function to initiate the data transformation



