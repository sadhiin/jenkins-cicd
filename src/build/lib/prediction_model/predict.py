import os
import pandas as pd
import numpy as np
import joblib
from prediction_model.config import config
from prediction_model.processing.data_handling import load_pipeline

calssification_pipeline = load_pipeline(
    os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME))


def generate_prediction(data_input):
    data = pd.DataFrame(data_input)
    pred = calssification_pipeline.predict(data[config.FEATURES])

    output = np.where(pred == 1, 'Y', 'N')
    return {'prediction': output}


def generate_test_prediction():
    test_data = pd.read_csv(os.path.join(
        config.DATAPATH, config.TESTING_DATA_FILE))
    pred = calssification_pipeline.predict(test_data[config.FEATURES])

    output = np.where(pred == 1, 'Y', 'N')
    return output


if __name__ == "__main__":
    print(generate_test_prediction())