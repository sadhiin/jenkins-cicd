import os
import pathlib
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent
# print(PACKAGE_ROOT)
# data
DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")
TRAINING_DATA_FILE = "train.csv"
TESTING_DATA_FILE = "test.csv"

# Model
MODEL_NAME = "classifier.pkl"
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

TARGET = 'Loan_Status'

# features
FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'CoapplicantIncome',
            'ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
                'Self_Employed', 'Credit_History', 'Property_Area']

# in this case it is the same as categorical features but it could be different in other project
FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education',
                      'Self_Employed', 'Credit_History', 'Property_Area']

FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURES_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = ['CoapplicantIncome']
# taking log of these features(neumerical)
LOG_FEATURES = ['ApplicantIncome', 'LoanAmount']
