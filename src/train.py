import pandas as pd

from catboost import CatBoostClassifier
from sklearn.base import BaseEstimator
from sklearn.metrics import accuracy_score, roc_auc_score, average_precision_score
from sklearn.model_selection import train_test_split


def train_model(
    train: pd.DataFrame,
    model: BaseEstimator=CatBoostClassifier,
    model_params: dict = { "iterations":1000, 
                           "learning_rate": 0.1, 
                           "depth" : 6,  
                           "reg_lambda":0.10, 
                           "early_stopping_rounds" : 100},
) -> CatBoostClassifier:
    """
    Function to train a model on the training data.

    Parameters
    ----------
    model : BaseEstimator, optional
        The model to train, by default CatBoostClassifier.
    train : pd.DataFrame
        The training data to train the model on.

    Returns
    -------
    CatBoostClassifier
        The trained model.
    """

    cat_cols = ["sex" , "cp" , "fbs" , "restecg" , "exang" , "slope" , "ca" , "thal" ] 
    train_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    train, val = train_test_split(train, train_size=0.75 , random_state=42 , stratify=train["target"])

    clf = model(**model_params)
    clf.fit(X = train[train_cols] , y= train.target , eval_set=(val[train_cols] , val.target), cat_features=cat_cols)
    return clf


def evaluate_model(
    model: CatBoostClassifier, test: pd.DataFrame
) -> tuple:
    """
    Function to evaluate the model on the test data.

    Parameters
    ----------
    model : RandomForestClassifier
        The trained model to evaluate.
    test : pd.DataFrame
        The test data to evaluate the model on.

    Returns
    -------
    tuple
        The accuracy? roc_auc, average precision of the model on the test data.
    """
    X = test.drop("target", axis=1)
    y = test["target"]
    y_pred = model.predict_proba(X)[:,1]
    
    return accuracy_score(y, (y_pred>=0.5) ), roc_auc_score(y, y_pred) , average_precision_score(y, y_pred)