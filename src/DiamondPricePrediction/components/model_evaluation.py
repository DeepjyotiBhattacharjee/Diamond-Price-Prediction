import os
import sys
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.DiamondPricePrediction.utils.utils import load_object
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

# os.chdir("/Users/deepjyotibhattacharjee/Developer/Diamond_Price_Prediction")

class ModelEvaluation:
    def __init__(self):
        pass

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual,pred)
        return rmse,mae,r2
    
    def initiate_model_evaluation(self,train_array,test_array):
        try:
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            model_path = os.path.join("artifacts","model.pkl")
            model = load_object(model_path)

            mlflow.set_registry_uri("https://dagshub.com/DeepjyotiBhattacharjee/Diamond-Price-Prediction.mlflow")

            tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme
            mlflow.end_run()
            with mlflow.start_run():
                predicted_qualities = model.predict(X_test)
                print("here")
                rmse,mae,r2 = self.eval_metrics(y_test,predicted_qualities)
                mlflow.log_metric("rmse",rmse)
                mlflow.log_metric("mae",mae)
                mlflow.log_metric("r2",r2)
                print(f"RMSE : {rmse}")
                print(f"MAE  : {mae}")
                print(f"R2 : {r2}")

                # Model registry does not work with file store
                if tracking_url_type_store!= "file":
                    # this condition is for dagshub
                    mlflow.sklearn.log_model(model,"model",registered_model_name="ml_model")
                else:
                    # this condition is for local
                    mlflow.sklearn.log_model(model,"model")
                

        except Exception as e:
            raise CustomException(e,sys)