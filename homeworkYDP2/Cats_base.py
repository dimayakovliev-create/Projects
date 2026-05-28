import json
from pathlib import Path

def get_cats_info(f_path):
    cats_dict = []
    try:
        with Path(f_path).open("r", encoding="utf-8") as cats_file:
            for cats in cats_file:
                id, name, age = cats.strip().split(",")
                cat_info = {
                    "id": id,
                    "name": name,
                    "age": int(age),
                }
                cats_dict.append(cat_info)
            return cats_dict
    except FileNotFoundError:
        print(f"Файл, що знаходиться за адресою: '{f_path}' має іншу назву, або не існує.")
        exit()

f_path = Path("homeworkYDP2/Cats.txt")
abs_path = Path(f_path).absolute()

cats_info = get_cats_info(f_path)
print(cats_info)
print(json.dumps(cats_info, indent=4)) # спробував перевести в формат json