from pathlib import Path

slidev_dir = Path(__file__).resolve().parent.parent / "slidev"


for file_path in slidev_dir.rglob("*"):
    if file_path.is_file():
        print(file_path)
