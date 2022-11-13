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
X_train_encoder = encoder.fit_transform(X_train_imputed)
X_train_encoder

print("******************** Training Data ********************")
display(X_train)
display(pd.DataFrame(X_train_imputed, columns=X_train.columns))
display(pd.DataFrame(X_train_encoder, columns=encoder.get_feature_names_out(X_train.columns)))

X_test_imputed = imputer.transform(X_test)
X_test_encoded = encoder.transform(X_test_imputed)

print("******************** Testing Data ********************")
display(X_test)
display(pd.DataFrame(X_test_imputed, columns=X_train.columns))
display(pd.DataFrame(X_test_encoded, columns=encoder.get_feature_names_out(X_train.columns)))
