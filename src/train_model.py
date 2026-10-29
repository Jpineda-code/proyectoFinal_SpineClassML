from pathlib import Path

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = ROOT / "data" / "raw" / "vertebral_column.csv"
REPORT_DIR = ROOT / "reports"
FIGURE_DIR = REPORT_DIR / "figures"


def load_dataset():
    """Carga y valida el dataset local."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            "No se encuentra el dataset. "
            "Ejecuta primero: python -m src.download_data"
        )

    df = pd.read_csv(DATA_FILE)

    if "class" not in df.columns:
        raise ValueError("Falta la columna objetivo 'class'.")

    if df.isnull().any().any():
        raise ValueError("El dataset contiene valores faltantes.")

    X = df.drop(columns=["class"])
    y = df["class"].astype(str).str.strip()

    if not all(pd.api.types.is_numeric_dtype(X[c]) for c in X.columns):
        raise ValueError("Todas las variables predictoras deben ser numéricas.")

    return X, y


def calculate_metrics(y_true, y_pred):
    """Calcula métricas generales para clasificación multiclase."""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_macro": precision_score(
            y_true, y_pred, average="macro", zero_division=0
        ),
        "recall_macro": recall_score(
            y_true, y_pred, average="macro", zero_division=0
        ),
        "f1_macro": f1_score(
            y_true, y_pred, average="macro", zero_division=0
        ),
    }


def run_experiment():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    X, y = load_dataset()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    models = {
        "baseline_dummy": DummyClassifier(strategy="most_frequent"),
        "decision_tree": DecisionTreeClassifier(
            max_depth=4,
            min_samples_leaf=5,
            random_state=42,
        ),
    }

    all_metrics = []
    all_reports = []

    for model_name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        metrics = calculate_metrics(y_test, predictions)
        metrics["model"] = model_name
        all_metrics.append(metrics)

        report = classification_report(
            y_test,
            predictions,
            output_dict=True,
            zero_division=0,
        )

        for class_name, values in report.items():
            if isinstance(values, dict):
                all_reports.append({
                    "model": model_name,
                    "class": class_name,
                    **values,
                })

        if model_name == "decision_tree":
            labels = sorted(y.unique())
            matrix = confusion_matrix(
                y_test,
                predictions,
                labels=labels,
            )

            pd.DataFrame(
                matrix,
                index=labels,
                columns=labels,
            ).to_csv(REPORT_DIR / "confusion_matrix.csv")

            pd.DataFrame({
                "actual": y_test.to_numpy(),
                "predicted": predictions,
            }).to_csv(
                REPORT_DIR / "predictions.csv",
                index=False,
            )

    metrics_df = pd.DataFrame(all_metrics)
    metrics_df.to_csv(REPORT_DIR / "metrics.csv", index=False)

    pd.DataFrame(all_reports).to_csv(
        REPORT_DIR / "classification_report.csv",
        index=False,
    )

    print("\nResultados de evaluación:")
    print(metrics_df.round(3).to_string(index=False))

    print("\nMatriz de confusión del árbol de decisión:")
    print(pd.read_csv(
        REPORT_DIR / "confusion_matrix.csv",
        index_col=0,
    ))

    return metrics_df


if __name__ == "__main__":
    run_experiment()