import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer


class Log1pImputer(BaseEstimator, TransformerMixin):
    def __init__(self, strategy="median"):
        self.strategy = strategy
        self.imputer_ = SimpleImputer(strategy=self.strategy)

    def fit(self, X: pd.DataFrame, y=None):
        self.imputer_.fit(X)
        return self

    def transform(self, X: pd.DataFrame):
        X_out = self.imputer_.transform(X)

        if np.nanmin(X_out) < -1:
            raise ValueError("Log1pImuter values must be >= -1")
        return np.log1p(X_out)

    def get_feature_names_out(self, input_features=None):
        return np.asarray(input_features, dtype=object)


class RatioInteractionImputer(BaseEstimator, TransformerMixin):
    def __init__(self, strategy="median"):
        self.strategy = strategy
        self.imputer_ = SimpleImputer(strategy=self.strategy)

    def fit(self, X: pd.DataFrame, y=None):
        self.imputer_.fit(X)
        return self

    def transform(self, X: pd.DataFrame):
        X_out = self.imputer_.transform(X)
        X_out["rate_per_score"] = X_out["intrest_rate"] / X_out["credit_score"]
        X_out["inter_cs_ir"] = X_out["intrest_rate"] * X_out["credit_score"]

        return X_out

    def get_feature_names_out(self, input_features=None):
        input_features = list(input_features)
        return np.asarray(
            input_features + ["rate_per_score", "inter_cs_ir"],
            dtype=object,
        )


one_hot_pipe = Pipeline(
    steps=[
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("one_hot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ]
)

ord_categories = [
    [
        "F5",
        "F4",
        "F3",
        "F2",
        "F1",
        "E5",
        "E4",
        "E3",
        "E2",
        "E1",
        "D5",
        "D4",
        "D3",
        "D2",
        "D1",
        "C5",
        "C4",
        "C3",
        "C2",
        "C1",
        "B5",
        "B4",
        "B3",
        "B2",
        "B1",
        "A5",
        "A4",
        "A3",
        "A2",
        "A1",
    ],
]
ordinal_pipe = Pipeline(
    steps=[
        ("impute", SimpleImputer(strategy="most_frequent")),
        (
            "ord_enc",
            OrdinalEncoder(
                categories=ord_categories,
                handle_unknown="use_encoded_value",
                unknown_value=-1,
            ),
        ),
    ]
)

log1p_pipe = Pipeline(steps=[("log1p", Log1pImputer(strategy="median"))])

numeric_pipe = Pipeline(
    steps=[("impute", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
)

one_hot_cols = [
    "gender",
    "marital_status",
    "education_level",
    "employment_status",
    "loan_purpose",
]
ordinal_cols = ["grade_subgrade"]
numeric_cols = [
    "annual_income",
    "debt_to_income_ratio",
    "credit_score",
    "loan_amount",
    "interest_rate",
]
log1p_cols = [
    "annual_income",
    "debt_to_income_ratio",
    "credit_score",
    "loan_amount",
    "interest_rate",
]
preprocess = ColumnTransformer(
    transformers=[
        ("onehot", one_hot_pipe, one_hot_cols),
        ("ordinal", ordinal_pipe, ordinal_cols),
        ("log1p", log1p_pipe, log1p_cols),
        ("num", numeric_pipe, numeric_cols),
    ],
    remainder="drop",
    verbose_feature_names_out=True,
)
