import re

raw_numbers = [
    "     067\\t123 4567",
    " +380099-34851-16",
    "   0050-948-51-70   !",
    "  00067-929-9999   ",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "це не номер зовсім",
    "     0503451234",
    "   050//456//11/ок",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "478555",
    "25252545542525455225544444525"
]

num = input("Додайте номер телефону в форматі +38: ")
raw_numbers.insert(0, num)

edited_numbers = []  #створений порожній список для занесення виправлених номерів
invalid_numbers = [] #Створений порожній список для додавання невиправлених номерів

def normalize_phone(phone_number):
    figures = re.sub(r'\D', '', phone_number)
    if figures.startswith("3800") and len(figures) == 13: # частий життєвий приклад з баз даних банків
        return "+" + (figures[:3] + figures[4:])
    if figures.startswith("380") and len(figures) == 12:
        return "+" + figures
    if figures.startswith("80") and len(figures) == 11:
        return "+3" + figures
    if figures.startswith("000") and len(figures) == 12: # частий життєвий приклад з баз даних банків
        return "+38" + figures[2:]    
    if figures.startswith("00") and len(figures) == 11: # частий життєвий приклад з баз даних банків
        return "+38" + figures[1:]
    if figures.startswith("0") and len(figures) == 10:
        return "+38" + figures
    if len(figures) == 12:
        return "+" + figures
    return None # Якщо довжина нв співпала повертаємо None

# Сортуємо номери по списках: ті що можемо використовувати (привели до стандарту) і ті що не вдалося привести (вхідна інфа непорозуміла) 
for phone_number in raw_numbers:
    normalized = normalize_phone(phone_number) # запускаємо функцію виправлення номерів
    if normalized:
        edited_numbers.append(normalized) # наповнюємо список виправленими номерами
    else:
        invalid_numbers.append(phone_number.strip()) # додаємо послідовно кожний незрозумілий "оригінал номеру" до списку помилок   

# Виводимо результати фільтрації:
print("Нормалізовані номери телефонів клієнтів для SMS-розсилки:", edited_numbers)
print("Помилкові номери клієнтів, що вилучені зі списку:", invalid_numbers)

# Тепер би навчитися це імпортувати з файлу бази телефонів клієнтів: abs_bank_phones.db телефони, прокачати через цю функцію і повернути два файли після виправлення: "correct.db" та "invalid.db"))
