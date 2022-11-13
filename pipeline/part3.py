## Part 0: Importing
import numpy as np
import pandas as pd

from nltk.tokenize import RegexpTokenizer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import MinMaxScaler

## Part 1: Loading Data
data_in = {'document': ['Food was good.',
                        'Superb food :)',
                        'Absolutely superb!']}

X_train = pd.DataFrame(data = data_in)

## Part 2: Custom Transformers
class CharacterCounter(BaseEstimator, TransformerMixin):
    """Count the number of characters in a document"""
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        n_characters = X.str.len()
        return n_characters.values.reshape(-1,1)

class TokenCounter(BaseEstimator, TransformerMixin):
    """Count the number of tokens in a document"""
    def __init__(self):
        pass

    def fit(self, X, y=None):
        self.tokeniser = RegexpTokenizer(r'[A-Za-z]+')
        return self

    def transform(self, X, y=None):
        n_tokens = X.apply(lambda 
                           document: len(self.tokeniser.tokenize(document)))
        return n_tokens.values.reshape(-1, 1)

## Part 3: DIY FeatureUnion
text = 'document'

vectoriser = TfidfVectorizer(token_pattern=r'[a-z]+', stop_words='english')

character_pipe = Pipeline([
    ('character_counter', CharacterCounter()),
    ('scaler', MinMaxScaler()),
    ])

token_pipe = Pipeline([
    ('token_counter', TokenCounter()),
    ('scaler', MinMaxScaler()),
    ])

preprocessor = FeatureUnion([
    ('vectoriser', vectoriser),
    ('character', character_pipe),
    ('token', token_pipe),
    ])

preprocessor.fit(X_train[text])

columns = list(preprocessor.transformer_list[0][1].get_feature_names_out()) + ['n_characters', 'n_tokens']

X_train_transformed = pd.DataFrame(preprocessor.transform(X_train[text]).toarray(),
                                   columns=columns)

X_train_transformed
