from os import name
from pathlib import Path

def total_salary(f_path):
    salaries_dict = {}
    try:
        with Path(f_path).open("r", encoding="utf-8") as empl_file:
            for persons in empl_file:
                name, salary_str = persons.strip().split(",", 1)
                salaries_dict[name] = int(salary_str)
        total = sum(salaries_dict.values())
        average = total / len(salaries_dict)
        return total, average
    except FileNotFoundError:
        print(f"Файл, що знаходиться за адресою: '{abs_path}' має іншу назву, або не існує.")
        exit()


f_path = "homeworkYDP2/Salar.txt"
abs_path = Path(f_path).absolute()

total, average = total_salary(f_path)
print(f"Загальна сума заробітної плати: {total} грн., Середня заробітна плата: {average} грн.")
