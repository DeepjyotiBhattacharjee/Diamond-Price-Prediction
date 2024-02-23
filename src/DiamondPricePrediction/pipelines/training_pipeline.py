from src.DiamondPricePrediction.components.data_ingestion import DataIngestion
from src.DiamondPricePrediction.components.data_transformation import DataTransformation
from src.DiamondPricePrediction.components.model_training import ModelTrainer

import os
import sys
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException
import pandas as pd

data_ingestion_obj = DataIngestion()

train_data_path, test_data_path =  data_ingestion_obj.initiate_data_ingestion()

data_transformation_obj = DataTransformation()
train_arr, test_arr =  data_transformation_obj.initiate_data_transformation(train_data_path,test_data_path)

model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_training(train_arr,test_arr)
 