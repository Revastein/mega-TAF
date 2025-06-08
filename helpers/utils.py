from pathlib import Path


def get_file_abs_path(relative_path: str) -> Path:
    project_root = Path(__file__).resolve().parents[1]
    return project_root / relative_path
