import pandas as pd

from src.preprocessing import load_data, split_data


def test_load_data() -> None:
    df = load_data()
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1025, 14)
    assert df['target'].nunique() == 2


def test_split_data() -> None:
    df = load_data()
    train, test = split_data(df)
    assert train is not None
    assert test is not None
    assert isinstance(train, pd.DataFrame)
    assert isinstance(test, pd.DataFrame)
    assert train.shape == (768, 14)
    assert test.shape == (257, 14)