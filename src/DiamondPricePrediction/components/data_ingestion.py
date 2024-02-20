import os
import sys 
import pandas as pd
import numpy as np
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


class DataIngestionConfig:
    raw_data_path:str = os.path.join("/Users/deepjyotibhattacharjee/Developer/Diamond_Price_Prediction/artifacts","raw.csv")
    train_data_path:str = os.path.join("/Users/deepjyotibhattacharjee/Developer/Diamond_Price_Prediction/artifacts","train.csv")
    test_data_path:str = os.path.join("/Users/deepjyotibhattacharjee/Developer/Diamond_Price_Prediction/artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started.")
        try:
            data = pd.read_csv(Path(os.path.join("/Users/deepjyotibhattacharjee/Developer/Diamond_Price_Prediction/notebooks/data","gemstone.csv")))
            logging.info("Read the dataset as a dataframe.")

            print(os.path.join(self.ingestion_config.raw_data_path))

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Saved raw data in artifacts folder")

            logging.info("Performed train test split.")

            train_data, test_data = train_test_split(data, test_size=0.25)  # Splitting into training and testing sets 
            logging.info("Train test split completed.")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data ingestion completed.")

        except Exception as e:
            logging.info("Exception occured at data ingestion stage.")
            raise CustomException(e,sys)
