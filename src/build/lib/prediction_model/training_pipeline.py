import os
import sys
import pathlib
# PACKAGE_ROOT = pathlib.Path(os.path.dirname(__file__)).resolve().parent
# sys.path.append(os.path.join(PACKAGE_ROOT, "prediction_model"))

from prediction_model.processing.data_handling import load_dataset, save_pipeline
import prediction_model.pipeline as pipe
from prediction_model.config import config

def perform_training():
    train_data = load_dataset(config.TRAINING_DATA_FILE)
    train_y = train_data[config.TARGET].map({'Y': 1, 'N': 0})
    print('Training data loaded successfully')

    print('Training features: ', config.FEATURES)
    pipe.classification_pipeline.fit(train_data[config.FEATURES], train_y)

    # saving the hole pipeline
    save_pipeline(pipe.classification_pipeline)


if __name__=='__main__':
    perform_training()