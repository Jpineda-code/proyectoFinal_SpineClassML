from src.train_model import load_dataset, calculate_metrics

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def test_dataset_has_expected_shape():
    X, y = load_dataset()

    assert X.shape == (310, 6)
    assert len(y) == 310
    assert y.nunique() == 3


def test_dataset_has_no_missing_values():
    X, y = load_dataset()

    assert not X.isnull().any().any()
    assert not y.isnull().any()


def test_model_can_train_and_predict():
    X, y = load_dataset()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    model = DecisionTreeClassifier(
        max_depth=4,
        min_samples_leaf=5,
        random_state=42,
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    assert len(predictions) == len(y_test)
    assert set(predictions).issubset(set(y.unique()))


def test_metrics_are_in_valid_range():
    metrics = calculate_metrics(
        ["Normal", "Hernia", "Normal"],
        ["Normal", "Normal", "Normal"],
    )

    for value in metrics.values():
        assert 0.0 <= value <= 1.0