import sys, os

# 1. Находим путь к папке Projects (на уровень выше, чем текущий файл)
 
# 2. Добавляем этот путь в список поиска Python
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from module06_env.calculations import salary_calculation


salary = 1000
bonus = 50
salary_with_bonus = salary_calculation.add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015

from module06_env.calculations.salary_calculation import add_bonus

salary = 1000
bonus = 15
salary_with_bonus = add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015