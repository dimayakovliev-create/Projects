from pathlib import Path
log_path = Path(__file__).parent / "logs.txt"

with open(log_path, "r") as log_file:
    res = log_file.read()
    print(res)
