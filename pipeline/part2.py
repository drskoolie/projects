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

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['total_bill']),
                                                    df['total_bill'],
                                                    test_size=0.2,
                                                    random_state=seed)

## Part 1: ColumnTransformer
categorical = list(X_train.select_dtypes('category').columns)
numerical = list(X_train.select_dtypes('number').columns)

cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False))
    ])

num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', MinMaxScaler)
    ])

preprocessor = ColumnTransformer([
    ('cat', cat_pipe, categorical),
    ('num', num_pipe, numerical),
    ])

preprocessor.fit(X_train)

cat_columns = preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(categorical)
columns = np.append(cat_columns, numerical)

display(X_train)
display(pd.DataFrame(preprocessor.transform(X_train), columns=columns))

display(X_test)
display(pd.DataFrame(preprocessor.transform(X_test), columns=columns))
