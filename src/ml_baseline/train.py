import os
import json
import pandas as pd
from datetime import datetime
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score


def run_training_pipeline(target_column: str, seed: int = 42):
    """
    Executes the baseline training pipeline:
    Data loading, stratified splitting, dummy training, and artifact saving.
    """
    # 1. Load processed features
    data_path = Path("data/processed/features.csv")
    if not data_path.exists():
        raise FileNotFoundError(f"Processed features not found at {data_path}")

    df = pd.read_csv(data_path)

    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataset")

    # 2. Stratified Train-Test Split (80/20)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_holdout, y_train, y_holdout = train_test_split(
        X, y, test_size=0.20, random_state=seed, stratify=y
    )

    # 3. Train Baseline Model (Dummy Classifier)
    # This serves as the benchmark to beat in future days
    model = DummyClassifier(strategy="most_frequent")
    model.fit(X_train, y_train)

    # 4. Evaluate Performance
    y_pred = model.predict(X_holdout)
    metrics = {
        "accuracy": float(accuracy_score(y_holdout, y_pred)),
        "recall": float(recall_score(y_holdout, y_pred, zero_division=0)),
        "precision": float(precision_score(y_holdout, y_pred, zero_division=0)),
        "run_date": datetime.now().isoformat(),
        "target": target_column,
        "seed": seed,
    }

    # 5. Save Artifacts (Versioned Run)
    run_id = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    run_dir = Path(f"models/runs/{run_id}")
    metrics_dir = run_dir / "metrics"

    metrics_dir.mkdir(parents=True, exist_ok=True)

    with open(metrics_dir / "baseline_holdout.json", "w") as f:
        json.dump(metrics, f, indent=4)

    # Update latest run pointer
    registry_path = Path("models/registry")
    registry_path.mkdir(parents=True, exist_ok=True)
    with open(registry_path / "latest.txt", "w") as f:
        f.write(run_id)

    return run_id
