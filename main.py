# Basic file organizer structure
from pathlib import Path

path_workspace = Path("workspace")
path_workspace.mkdir(exist_ok=True)

files = ["notes.txt", "report.txt", "data.csv",
         "config.json", "image.png"]

directories = ["text", "data", "images"]

for name in files:
    path = path_workspace / name
    path.touch()

for name in directories:
    path = path_workspace / name
    path.mkdir(exist_ok=True)

for path in path_workspace.iterdir():
    if path.is_file():
        if path.suffix == ".txt":
            destination = path_workspace / "text" / path.name
            path.replace(destination)

        elif path.suffix == ".csv" or path.suffix == ".json":
            destination = path_workspace / "data" / path.name
            path.replace(destination)

        elif path.suffix == ".png":
            destination = path_workspace / "images" / path.name
            path.replace(destination)
