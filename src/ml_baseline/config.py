from pathlib import Path


class Paths:
    def __init__(self, root: Path):
        self.root = root

    @classmethod
    def from_repo_root(cls):
        return cls(root=Path.cwd())

    @property
    def data_processed_dir(self) -> Path:
        return self.root / "data" / "processed"

    @property
    def reports_dir(self) -> Path:
        return self.root / "reports"
