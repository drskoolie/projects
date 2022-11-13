## Part 0: Intialization
import numpy as np
import pandas as pd
from seaborn import load_dataset

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

seed = 123

df = load_dataset('tips').drop(columns=['tip', 'sex']).sample(n=5, random_state=seed)
df.iloc[[1, 2, 4], [2, 4]] = np.nan

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['total_bill', 'size']),
                                                    df['total_bill'],
                                                    test_size=0.2,
                                                    random_state=seed)

## Part 1: No Pipeline
imputer = SimpleImputer(strategy='constant', fill_value='missing')
X_train_imputed = imputer.fit_transform(X_train)

encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
X_train_encoded = encoder.fit_transform(X_train_imputed)

model = LinearRegression()

model.fit(X_train_encoded, y_train)
y_train_pred = model.predict(X_train_encoded)
print(f"Predictions on training data: {y_train_pred}")

X_test_imputed = imputer.transform(X_test)
X_test_encoded = encoder.transform(X_test_imputed)
y_test_pred = model.predict(X_test_encoded)
print(f"Predictions on test data: {y_test_pred}")

## Part 2: Pipeline
pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False)),
    ('model', LinearRegression())
    ])

pipe.fit(X_train, y_train)

y_train_pred = pipe.predict(X_train)
print(f"Predictions on training data: {y_train_pred}")

y_test_pred = pipe.predict(X_test)
print(f"Predictions on test data: {y_test_pred}")
