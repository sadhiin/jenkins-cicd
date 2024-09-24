import os
import urllib.request
import pandas as pd
import joblib
from prediction_model.config import config
import urllib


def load_dataset(file_name: str):
    """Function to load the dataset

    Args:
        file_name (str): File name to load

    Returns:
        pd.DataFrame: Returns the loaded dataset
    """
    if 'train' in file_name:
        _df = pd.read_csv('https://raw.githubusercontent.com/shrikant-temburwar/Loan-Prediction-Dataset/master/train.csv')
        return _df
    else:
        _df = pd.read_csv('https://raw.githubusercontent.com/shrikant-temburwar/Loan-Prediction-Dataset/master/test.csv')
        return _df


def save_pipeline(pipeline_to_save):
    """Function to save the pipeline

    Args:
        pipeline: Pipeline object to save
    """

    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)

    joblib.dump(pipeline_to_save, save_path)
    print(f"Pipeline saved at: {config.MODEL_NAME}")


def load_pipeline(pipeline_to_load):
    """Function to load the pipeline

    Returns:
        Pipeline: Returns the loaded pipeline
    """
    if not os.path.isfile(pipeline_to_load):
        raise FileNotFoundError(f"File not found at: {config.MODEL_NAME}")

    model_loaded = joblib.load(pipeline_to_load)
    return model_loaded
