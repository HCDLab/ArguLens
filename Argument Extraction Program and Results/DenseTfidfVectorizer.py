from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

class DenseTfidfVectorizer(TfidfVectorizer):

    def transform(self, raw_documents, copy=True):
        X = super().transform(raw_documents, copy=copy)
        df = pd.DataFrame(X.toarray(), columns=self.get_feature_names(), index=raw_documents.index)
        return df

    def fit_transform(self, raw_documents, y=None):
        X = super().fit_transform(raw_documents, y=y)
        df = pd.DataFrame(X.toarray(), columns=self.get_feature_names(), index=raw_documents.index)
        return df
    
class DenseCountVectorizer(CountVectorizer):

    def transform(self, raw_documents, copy=True):
        X = super().transform(raw_documents, copy=copy)
        df = pd.DataFrame(X.toarray(), columns=self.get_feature_names(), index=raw_documents.index)
        return df

    def fit_transform(self, raw_documents, y=None):
        X = super().fit_transform(raw_documents, y=y)
        df = pd.DataFrame(X.toarray(), columns=self.get_feature_names(), index=raw_documents.index)
        return df

