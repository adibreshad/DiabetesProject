import os 
import sys
import numpy as np
import pandas as pd
import dill 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
        

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)
        
    

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report ={}
        for i in range(len(list(models))):
            model =list(models.values())[i]
            para = param[list(models.keys())[i]]

            #gridsearch cv for hyperparameter tunning
            gs = GridSearchCV(model, para, cv=3, scoring='r2')
            gs.fit(X_train, y_train)

            #set best parameters and train
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            #predictions
            y_train_pred= model.predict(X_train)
            y_test_pred= model.predict(X_test)

            #Evaluate
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]]=test_model_score

        return report


    except Exception as e:
        raise CustomException(e, sys)
        
        


def calculate_metrics(y_true, y_pred):
    """Calculate comprehensive regression metrics"""
    try:
        metrics = {
            'r2_score': r2_score(y_true, y_pred),
            'mae': mean_absolute_error(y_true, y_pred),
            'mse': mean_squared_error(y_true, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_true, y_pred))
        }
        return metrics
    except Exception as e:
        raise CustomException(e, sys)
        

