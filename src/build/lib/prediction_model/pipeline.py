from sklearn.pipeline import Pipeline
from prediction_model.config import config
from prediction_model.processing import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression


classifcation_pipeline = Pipeline(
    [
        ('MeanImputer', preprocessing.MeanImputer(cols=config.NUM_FEATURES)),
        ('ModeImputer', preprocessing.ModeImputer(cols=config.CAT_FEATURES)),
        ('DomainProcessing', preprocessing.DomainProcessing(
            variable_to_modify=config.FEATURE_TO_MODIFY, variable_to_add=config.FEATURES_TO_ADD)),
        ('DropFeatures', preprocessing.DropColumns(cols=config.DROP_FEATURES)),
        ('LabelEncoder', preprocessing.CustomLabelEncoder(cols=config.FEATURES_TO_ENCODE)),
        ('LogTransformer', preprocessing.CustomLogTransformation(cols=config.LOG_FEATURES)),
        ('MinMaxScaler', MinMaxScaler()),
        ('Classifier', LogisticRegression(random_state=0))
    ]
)
