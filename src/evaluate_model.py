from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports"
FIGURE_DIR = REPORT_DIR / "figures"


def main():
    matrix_file = REPORT_DIR / "confusion_matrix.csv"

    if not matrix_file.exists():
        raise FileNotFoundError(
            "Primero ejecuta: python -m src.train_model"
        )

    matrix = pd.read_csv(matrix_file, index_col=0)

    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(7, 5))
    sns.heatmap(
        matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=matrix.columns,
        yticklabels=matrix.index,
    )

    plt.title("Matriz de confusión - Árbol de decisión")
    plt.xlabel("Clase predicha")
    plt.ylabel("Clase real")
    plt.tight_layout()

    output = FIGURE_DIR / "confusion_matrix.png"
    plt.savefig(output, dpi=150)
    plt.close()

    print(f"Gráfica guardada en: {output}")


if __name__ == "__main__":
    main()