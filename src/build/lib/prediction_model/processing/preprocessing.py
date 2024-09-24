import numpy as np
from prediction_model.config import config
from sklearn.base import BaseEstimator, TransformerMixin


class MeanImputer(BaseEstimator, TransformerMixin):
    """Fill missing values with the mean value of the column
    Note: This imputer only applicable for numerical columns.
    """

    def __init__(self, cols: list = []):
        super().__init__()
        self.cols = cols

    def fit(self, X, y=None):
        self.mean_dict = {}

        if isinstance(self.cols, list) and len(self.cols) > 0:
            for col in self.cols:
                if col not in X.columns:
                    raise ValueError(f'Column {col} does not exist in the DataFrame.')
                self.mean_dict[col] = X[col].mean()
        else:
            raise ValueError('No columns to impute. Received cols={}'.format(self.cols))
        return self

    def transform(self, X):
        X = X.copy()
        print('MeanImputer: ', self.cols)
        for col in self.cols:
            X[col] = X[col].fillna(self.mean_dict[col])  # Not using inplace=True
        return X



class ModeImputer(BaseEstimator, TransformerMixin):
    """Fill missing values with the mode value of the column.
    Note: This imputer is only applicable for categorical columns.
    """

    def __init__(self, cols: list = []):
        super().__init__()
        self.cols = cols

    def fit(self, X, y=None):
        self.mode_dict = {}

        if isinstance(self.cols, list) and len(self.cols) > 0:
            for col in self.cols:
                if col not in X.columns:
                    raise ValueError(f'Column {col} does not exist in the DataFrame.')
                self.mode_dict[col] = X[col].mode().iloc[0]  # Take the first mode
        else:
            raise ValueError('No columns to impute at ModeImputer class. Received cols={}'.format(self.cols))
        return self

    def transform(self, X):
        X = X.copy()
        print('ModeImputer: ', self.cols)
        for col in self.cols:
            X[col] = X[col].fillna(self.mode_dict[col])  # Avoid using inplace=True
        return X



class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, cols: list = []):
        self.cols = cols

    def fit(self, X, y=None):
        return self  # No fitting required for dropping columns.

    def transform(self, X):
        print('DropColumns: ', self.cols)
        # Check if self.cols is empty; if it is, just return the original DataFrame
        if not self.cols:
            return X.copy()

        # Check if the columns to drop exist in X
        missing_cols = [col for col in self.cols if col not in X.columns]
        if missing_cols:
            raise ValueError(f"Columns not found in the DataFrame: {missing_cols}")

        X = X.copy()
        X = X.drop(columns=self.cols)
        return X



class DomainProcessing(BaseEstimator, TransformerMixin):
    """Class for processing domain-specific features by modifying specified columns
    by adding the values of another column.
    """

    def __init__(self, variable_to_modify=None, variable_to_add=None) -> None:
        super().__init__()
        self.variable_to_modify = variable_to_modify if variable_to_modify is not None else []
        self.variable_to_add = variable_to_add

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        print('DomainProcessing: ', self.variable_to_modify, self.variable_to_add)

        X = X.copy()

        # Check if variable_to_add exists in X
        if self.variable_to_add not in X.columns:
            raise ValueError(f"Column {self.variable_to_add} does not exist in the DataFrame.")

        for col in self.variable_to_modify:
            if col not in X.columns:
                raise ValueError(f"Column {col} does not exist in the DataFrame.")
            X[col] = X[col] + X[self.variable_to_add]  # Assumes both columns are numeric or compatible types

        return X



class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, cols: list = []):
        self.cols = cols

    def fit(self, X, y=None):
        self.label_dict = {}
        for col in self.cols:
            if col not in X.columns:
                raise ValueError(f"Column {col} does not exist in the DataFrame.")
            t = X[col].value_counts().sort_values(ascending=True).index
            self.label_dict[col] = {k: i for i, k in enumerate(t, 0)}
        return self

    def transform(self, X):
        print('CustomLabelEncoder: ', self.cols)
        print('NaN values present: ', X.isnull().sum())
        X = X.copy()
        for col in self.cols:
            if col not in self.label_dict:
                raise ValueError(f"Column {col} not fitted yet.")
            X[col] = X[col].map(self.label_dict[col]).fillna(-1).astype(int)  # Fill unknowns with -1 or handle as needed
        return X


class CustomLogTransformation(BaseEstimator, TransformerMixin):
    def __init__(self, cols: list = []) -> None:
        super().__init__()
        self.cols = cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        print('CustomLogTransformation: ', self.cols)
        X = X.copy()
        for col in self.cols:
            if col not in X.columns:
                raise ValueError(f"Column {col} does not exist in the DataFrame.")
            if (X[col] <= 0).any():
                raise ValueError(f"Log transformation is undefined for non-positive values in column: {col}.")
            X[col] = np.log(X[col])
        return X
