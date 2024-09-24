import pytest
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_prediction

@pytest.fixture
def single_prediction():
    test_data = load_dataset(config.TESTING_DATA_FILE)
    single_row = test_data[:1]
    result = generate_prediction(single_row)
    
    return result

def test_single_prediction_not_none(single_prediction):
    assert single_prediction is not None, "prediction should not be None"
    
def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get('prediction')[0], str), "prediction should be a string"
    
    
def test_single_pred_validate(single_prediction):
    assert single_prediction.get('prediction')[0] in ['Y', 'N'], "prediction should be Y or N"