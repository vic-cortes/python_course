import os
from pathlib import Path

slidev_dir = Path(__file__).resolve().parent.parent / "slidev"


def get_all_presentations_files() -> tuple[list[Path], dict[str, list[Path]]]:
    """
    Returns a list of all presentation files in the slidev directory.
    """
    all_files = []
    all_dict = {}

    for file_path in slidev_dir.rglob("*"):
        if not file_path.is_file():
            continue

        if not all_dict.get(file_path.suffix):
            all_dict[file_path.suffix] = [file_path]
        else:
            all_dict[file_path.suffix].append(file_path)

        all_files.append(file_path)

    return all_files, all_dict
