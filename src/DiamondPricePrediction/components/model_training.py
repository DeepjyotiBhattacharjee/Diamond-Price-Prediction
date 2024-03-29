import sys
import os
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder 

from src.DiamondPricePrediction.utils.utils import save_object, evaluate_model
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet

# os.chdir('/Users/deepjyotibhattacharj ee/Developer/Diamond_Price_Prediction')

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")



class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training (self,train_array,test_array):
        try:
            logging.info("Splitting data into train and test data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
            'LinearRegression':LinearRegression(),
            'Lasso':Lasso(),
            'Ridge':Ridge(),
            'ElasticNet':ElasticNet()
            }

            model_report:dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print("\n=================================================================\n")
            logging.info(f"Model Report : {model_report}")

            # To get the best model from the dictionary
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
                ]
            
            best_model = models[best_model_name]

            print(f"Best model found , Model Name : {best_model_name}, R2 Score : {best_model_score}")
            print("\n=================================================================\n")
            logging.info(f"Best model found , Model Name : {best_model_name}, R2 Score : {best_model_score}")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )
    
        except Exception as e:
            logging.info("Error occured at model  training")
            raise CustomException(e,sys)