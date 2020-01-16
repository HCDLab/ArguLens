from sklearn.base import BaseEstimator, TransformerMixin

class GetDataRowByLabels(TransformerMixin, BaseEstimator):
    def __init__(self, label_list, cond_list):
        self.label_list = label_list
        self.cond_list = cond_list
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None, copy=None):
        for idx, val in enumerate(self.label_list):
            X = X.loc[X[val] == self.cond_list[idx]].copy()
        return X

class GetDataColByNames(TransformerMixin, BaseEstimator):
    def __init__(self, columns):
        self.columns = columns
    def fit(self, X, y=None):
        self.x = X
        return self
    def transform(self, X, y=None, copy=None):
        self.x = X[self.columns]
        return self.x
    def get_feature_names(self):
        return self.x.columns
