from pathlib import Path, PurePath
import time

p = PurePath("/usr107/bin/simple.jpg")
print("Name:", p.name)  
print("Suffix:", p.suffix) 
print("Parent:", p.parent)

p = Path("example.txt")
p.write_text("Hello, world2222222!")
print(p.read_text()) 
print("Exists:", p.exists())

path_windows = Path(r"D:\Projects\folder.txt")
base_path = Path("/usr/bin")
full_path = base_path / "subdir" / "script.py"
print(full_path)  # Виведе: /usr/bin/subdir/script.py

relative_path = Path("module05/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)

absolute_path = Path("D:/Projects/module05/example.txt")
relative_path = absolute_path.relative_to("D:/Projects/")
print(relative_path)

original_path = Path("example.txt")
new_path = original_path.with_name("report.txt")
new_file = original_path.replace("module05/report2.txt")
new_path = original_path.with_suffix(".cdp")
fh = open("module05/report2.txt", "r")
print(fh.read())

file_path = Path("module05/example30.txt")
file_path.write_text("Привіт світ!", encoding="utf-8")

file_path = Path("example.bin")
# Бінарні дані для запису
data = b"Python is great!"
# Запис байтів у файл
file_path.write_bytes(data)
binary_data = file_path.read_bytes()
print(binary_data)

directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=False)
directory = Path('/my_directory/new_folder')
directory.rmdir()

file_path = Path("D:/Projects/OlegAndrus/module05/picture/icons/utilities-terminal-icon.png")

# Час створення та модифікації
creation_time = file_path.stat().st_birthtime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")
file_path1 = Path("D:/Projects/raw_data.bin")
file_path1.unlink()