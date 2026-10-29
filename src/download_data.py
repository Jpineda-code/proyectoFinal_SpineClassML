from pathlib import Path

from ucimlrepo import fetch_ucirepo


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "raw"
OUTPUT_FILE = DATA_DIR / "vertebral_column.csv"


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    dataset = fetch_ucirepo(id=212)

    features = dataset.data.features.copy()
    targets = dataset.data.targets.copy()

    df = features.copy()
    df["class"] = targets.iloc[:, 0].astype(str).str.strip()

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Dataset guardado en: {OUTPUT_FILE}")
    print(f"Dimensiones: {df.shape}")
    print("\nDistribución de clases:")
    print(df["class"].value_counts())


if __name__ == "__main__":
    main()