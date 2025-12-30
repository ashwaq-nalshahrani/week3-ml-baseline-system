import pandas as pd
from pathlib import Path

def parquet_supported() -> bool:
    try:
        import pyarrow  # noqa
        return True
    except ImportError:
        return False

def write_tabular(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".csv":
        df.to_csv(path, index=False)
    elif path.suffix == ".parquet":
        df.to_parquet(path, index=False)
    else:
        raise ValueError(f"Unsupported format: {path.suffix}")