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
