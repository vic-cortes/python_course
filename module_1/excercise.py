import os
from pathlib import Path

slidev_dir = Path(__file__).resolve().parent.parent / "slidev"

all_files = []
all_dict = {}

for file_path in slidev_dir.rglob("*"):
    if not file_path.is_file():
        continue

    if not all_dict.get(file_path.suffix):
        all_dict[file_path.suffix] = [file_path]
    else:
        all_dict[file_path.suffix].append(file_path)


all_js_files = [file for file in all_files if file.suffix == ".js"]
all_js_files_2 = [file for file in all_files if str(file).endswith(".js")]

unique_extensions = {file.suffix for file in all_files}
